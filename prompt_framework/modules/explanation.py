from prompt_framework.core import TemplateLogosModule

class ExplanationModule(TemplateLogosModule):
    """
    Step 3: Explanation. Provide structured symbolic reasoning.
    """

    @property
    def name(self) -> str:
        return "explanation"

    @property
    def header(self) -> str:
        return "#Step 3: Explanation (s3)"

    def __init__(self):
        super().__init__("prompt_framework.templates", "explanation.tpl")
