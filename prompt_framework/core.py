from typing import Dict, Any
import importlib.resources as pkg_res

class LogosModule:
    """
    Base class for all modules in the LOGOS pipeline.
    Subclasses must define `name` and implement `render`.
    """

    @property
    def name(self) -> str:
        """
        Returns the unique module identifier (e.g. "abstraction").
        """
        raise NotImplementedError("Subclasses must define a `name` property")

    def render(self, question: str, context: Dict[str, Any]) -> str:
        """
        Given the original question and prior context, returns
        the full prompt text for this module.
        """
        raise NotImplementedError("Subclasses must implement `render`")

class TemplateLogosModule(LogosModule):
    """
    Wraps an external template file with a fixed header/body structure.
    """

    WRAPPER = "{header}\n\n{body}"

    def __init__(self, tpl_pkg: str, tpl_file: str):
        # Load the .tpl content as the body template
        self._body = pkg_res.read_text(tpl_pkg, tpl_file)

    @property
    def header(self) -> str:
        """
        Returns the module's header (e.g. "#Step 1: Abstraction (s1)").
        Subclasses must override.
        """
        raise NotImplementedError("Subclasses must define a `header` property")

    def render(self, question: str, context: Dict[str, Any]) -> str:
        """
        Fill placeholders in the body (supports {question} & context keys),
        then wrap with header.
        """
        filled = self._body.format(question=question, **context)
        return self.WRAPPER.format(header=self.header, body=filled)
