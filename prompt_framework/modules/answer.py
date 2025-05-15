from prompt_framework.core import TemplateLogosModule

class AnswerModule(TemplateLogosModule):
    """
    Step 4: Answering. Extract the final answer concisely.
    """

    @property
    def name(self) -> str:
        return "answer"

    @property
    def header(self) -> str:
        return "#Step 4: Answering (s4)"

    def __init__(self):
        super().__init__("prompt_framework.templates", "answer.tpl")
