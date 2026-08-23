from typing import Any
from google import genai
from core.llm.ports import LlmProtocol
from core.llm.exceptions import LlmError

class GeminiAdapter(LlmProtocol):
    """
    Adaptador concreto para integração com o SDK oficial do Google Gemini (google-genai).
    """

    def __init__(self, api_key: str, default_model: str = "gemini-3.6-flash", client: Any | None = None) -> None:
        if not api_key or not api_key.strip():
            raise ValueError("API key é obrigatória para inicializar o GeminiAdapter.")
        self.api_key = api_key.strip()
        self.default_model = default_model
        self.client = client or genai.Client(api_key=self.api_key)

    def generate_text(self, prompt: str, **kwargs: Any) -> str:
        # Bouncer pattern / Fail Fast: validação antecipada do prompt de entrada
        if not prompt or not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("O prompt fornecido não pode ser nulo ou vazio.")

        model = kwargs.pop("model", self.default_model)

        try:
            response = self.client.models.generate_content(
                model=model,
                contents=prompt,
                **kwargs
            )
            if not response or not response.text:
                raise LlmError("A resposta do modelo Gemini veio vazia.")
            return response.text
        except ValueError:
            raise
        except LlmError:
            raise
        except Exception as e:
            raise LlmError(f"Falha na comunicação com a API do Gemini: {str(e)}") from e
