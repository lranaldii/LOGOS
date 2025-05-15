from prompt_framework.core import TemplateLogosModule

class RoleModule(TemplateLogosModule):
    """
    Role module: defines the expert role instructions.
    """

    @property
    def name(self) -> str:
        return "role"

    @property
    def header(self) -> str:
        return "#Role"

    def __init__(self):
        super().__init__("prompt_framework.templates", "role.tpl")
