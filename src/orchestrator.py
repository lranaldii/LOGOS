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
    Reads config.yaml to determine which core modules to load,
    and also discovers any external plugins via entry-points.
    """

    def __init__(self, config_path: str):
        self.cfg = load_config(config_path)
        self.module_paths = get_pipeline(self.cfg)
        self.registry = discover_modules()

    def load_modules(self) -> List[LogosModule]:
        """
        Dynamically import and instantiate each module listed in config.yaml,
        then append any discovered plugins.
        """
        instances: List[LogosModule] = []
        for path in self.module_paths:
            pkg, cls = path.rsplit(".", 1)
            module = importlib.import_module(pkg)
            ModuleClass = getattr(module, cls)
            instances.append(ModuleClass())
        # add external plugins, if any
        for ModuleClass in self.registry.values():
            instances.append(ModuleClass())
        return instances

class Orchestrator:
    """
    Executes each module in sequence, sending its prompt to the LLM client
    and collecting the responses.
    """

    def __init__(
        self,
        modules: List[LogosModule],
        llm_client: LLMClient,
        log_level: int = logging.INFO,
    ):
        self.modules = modules
        self.client = llm_client
        self.logger = setup_logger(__name__, level=log_level)

    def execute(self, question: str) -> Dict[str, str]:
        """
        Run the pipeline on the given question.
        Returns a mapping from module.name -> LLM response text.
        """
        context: Dict[str, Any] = {}
        outputs: Dict[str, str] = {}

        for mod in self.modules:
            prompt = mod.render(question, context)
            self.logger.info(f"Running module: {mod.name}")
            # always call the LLM; no caching
            response = self.client.call(prompt)
            outputs[mod.name] = response
            # optional: parse response to update context for downstream modules

        return outputs
