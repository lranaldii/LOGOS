import logging
import importlib
from typing import List, Dict, Any

from prompt_framework.config import load_config, get_pipeline
from prompt_framework.registry import discover_modules
from prompt_framework.core import LogosModule
from prompt_framework.client import LLMClient
from prompt_framework.logger import setup_logger

class PipelineBuilder:
    """
    Builds the list of modules from config.yaml and any plugins.
    """

    def __init__(self, config_path: str):
        self.config = load_config(config_path)
        self.module_paths = get_pipeline(self.config)
        self.registry = discover_modules()

    def load_modules(self) -> List[LogosModule]:
        """
        Import and instantiate each module in the configured pipeline,
        then append discovered plugin modules.
        """
        modules: List[LogosModule] = []
        for path in self.module_paths:
            pkg_path, cls_name = path.rsplit(".", 1)
            mod = importlib.import_module(pkg_path)
            cls = getattr(mod, cls_name)
            modules.append(cls())
        # add plugins
        for cls in self.registry.values():
            modules.append(cls())
        return modules

class Orchestrator:
    """
    Executes the pipeline: for each module, render its prompt
    and call the LLM client.
    """

    def __init__(
        self,
        modules: List[LogosModule],
        client: LLMClient,
        log_level: int = logging.INFO,
    ):
        self.modules = modules
        self.client = client
        self.logger = setup_logger(__name__, level=log_level)

    def execute(self, question: str) -> Dict[str, str]:
        """
        Run each module in sequence on the question.
        Returns a dict mapping module.name -> response text.
        """
        context: Dict[str, Any] = {}
        outputs: Dict[str, str] = {}
        for mod in self.modules:
            prompt = mod.render(question, context)
            self.logger.info(f"Executing module: {mod.name}")
            response = self.client.call(prompt)
            outputs[mod.name] = response
            # optional: update context here for subsequent modules
        return outputs
