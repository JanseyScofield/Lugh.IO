from typing import Protocol, runtime_checkable

@runtime_checkable
class LlmProtocol(Protocol):
    """
    Protocolo abstrato para adaptadores de LLM (Inversão de Dependência - DIP).
    """

    def generate_text(self, prompt: str, **kwargs) -> str:
        """
        Gera texto a partir de um prompt fornecido ao LLM.

        :param prompt: O texto do prompt a ser enviado ao modelo.
        :param kwargs: Parâmetros opcionais adicionais para o modelo (ex: model, temperature).
        :return: Resposta em formato texto retornada pelo LLM.
        """
        ...
