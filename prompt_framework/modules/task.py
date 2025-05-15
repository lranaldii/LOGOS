from prompt_framework.core import TemplateLogosModule

class TaskModule(TemplateLogosModule):
    """
    Task module: instructs step-by-step solving.
    """

    @property
    def name(self) -> str:
        return "task"

    @property
    def header(self) -> str:
        return "#Task"

    def __init__(self):
        super().__init__("prompt_framework.templates", "task.tpl")
