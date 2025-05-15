from prompt_framework.core import TemplateLogosModule

class FormalizationModule(TemplateLogosModule):
    """
    Step 2: Formalization. Translate abstractions into symbolic form.
    """

    @property
    def name(self) -> str:
        return "formalization"

    @property
    def header(self) -> str:
        return "#Step 2: Formalization (s2)"

    def __init__(self):
        super().__init__("prompt_framework.templates", "formalization.tpl")
