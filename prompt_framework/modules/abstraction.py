from prompt_framework.core import TemplateLogosModule

class AbstractionModule(TemplateLogosModule):
    """
    Step 1: Abstraction.
    Identifies predicates, variables, and constants in the question.
    """

    @property
    def name(self) -> str:
        return "abstraction"

    @property
    def header(self) -> str:
        return "#Step 1: Abstraction (s1)"

    def __init__(self):
        # load the template file from prompt_framework/templates/abstraction.tpl
        super().__init__("prompt_framework.templates", "abstraction.tpl")
