from typing import Dict, Any
import importlib.resources as pkg_res

class LogosModule:
    """
    Base class for all modules in the LOGOS pipeline.
    Subclasses must override `name` and `render`.
    """

    @property
    def name(self) -> str:
        """
        Return the unique module identifier.
        Example: "abstraction", "formalization", etc.
        """
        raise NotImplementedError("Subclasses must define a `name` property")

    def render(self, question: str, context: Dict[str, Any]) -> str:
        """
        Render the module's prompt given the original question
        and any context from previous modules.
        """
        raise NotImplementedError("Subclasses must implement `render`")

class TemplateLogosModule(LogosModule):
    """
    Base class that wraps an external .tpl file with a fixed header/body structure.
    """

    # fixed wrapper template
    WRAPPER = "{header}\n\n{body}"

    def __init__(self, tpl_pkg: str, tpl_file: str):
        # load the body of this module's prompt from the given package resource
        self._body = pkg_res.read_text(tpl_pkg, tpl_file)

    @property
    def header(self) -> str:
        """
        Return the module header, e.g. "#Step 1: Abstraction (s1)".
        Subclasses must override this.
        """
        raise NotImplementedError("Subclasses must define a `header` property")

    def render(self, question: str, context: Dict[str, Any]) -> str:
        """
        Fill placeholders in the .tpl body with the question and context,
        then wrap with the header.
        """
        # allow templates to use {question} and any keys in context
        filled = self._body.format(question=question, **context)
        return self.WRAPPER.format(header=self.header, body=filled)
