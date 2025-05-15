class LLMClient:
    """
    Abstract interface for an LLM client.
    """

    def call(self, prompt: str) -> str:
        """
        Send the prompt to the model and return its text response.
        """
        raise NotImplementedError

class OpenAIClient(LLMClient):
    """
    OpenAI API client implementation.
    """

    def __init__(self, api_key: str, model: str = "gpt-4"):
        import openai
        openai.api_key = api_key
        self.model = model

    def call(self, prompt: str) -> str:
        import openai
        resp = openai.Completion.create(
            model=self.model,
            prompt=prompt,
            max_tokens=1024,
        )
        return resp.choices[0].text.strip()
