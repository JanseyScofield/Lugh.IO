import pytest
from unittest.mock import MagicMock
from core.llm.ports import LlmProtocol
from core.llm.exceptions import LlmError
from core.llm.gemini_adapter import GeminiAdapter

def test_gemini_adapter_implements_protocol():
    mock_client = MagicMock()
    adapter = GeminiAdapter(api_key="valid_key", client=mock_client)
    assert isinstance(adapter, LlmProtocol)

def test_init_requires_api_key():
    with pytest.raises(ValueError, match="API key é obrigatória"):
        GeminiAdapter(api_key="")

    with pytest.raises(ValueError, match="API key é obrigatória"):
        GeminiAdapter(api_key="   ")

def test_generate_text_success():
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "Conteúdo do currículo gerado em HTML"
    mock_client.models.generate_content.return_value = mock_response

    adapter = GeminiAdapter(api_key="valid_key", client=mock_client)
    result = adapter.generate_text("Gere um currículo para a vaga X")

    assert result == "Conteúdo do currículo gerado em HTML"
    mock_client.models.generate_content.assert_called_once_with(
        model="gemini-3.6-flash",
        contents="Gere um currículo para a vaga X"
    )

def test_generate_text_with_custom_model():
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "Resposta com modelo customizado"
    mock_client.models.generate_content.return_value = mock_response

    adapter = GeminiAdapter(api_key="valid_key", client=mock_client)
    result = adapter.generate_text("Prompt de teste", model="gemini-1.5-pro")

    assert result == "Resposta com modelo customizado"
    mock_client.models.generate_content.assert_called_once_with(
        model="gemini-1.5-pro",
        contents="Prompt de teste"
    )

def test_generate_text_empty_prompt_fail_fast():
    mock_client = MagicMock()
    adapter = GeminiAdapter(api_key="valid_key", client=mock_client)

    with pytest.raises(ValueError, match="O prompt fornecido não pode ser nulo ou vazio"):
        adapter.generate_text("")

    with pytest.raises(ValueError, match="O prompt fornecido não pode ser nulo ou vazio"):
        adapter.generate_text("   ")

    with pytest.raises(ValueError, match="O prompt fornecido não pode ser nulo ou vazio"):
        adapter.generate_text(None)

    mock_client.models.generate_content.assert_not_called()

def test_generate_text_empty_response_raises_llm_error():
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.text = None
    mock_client.models.generate_content.return_value = mock_response

    adapter = GeminiAdapter(api_key="valid_key", client=mock_client)

    with pytest.raises(LlmError, match="resposta do modelo Gemini veio vazia"):
        adapter.generate_text("Prompt de teste")

def test_generate_text_value_error_re_raised():
    mock_client = MagicMock()
    mock_client.models.generate_content.side_effect = ValueError("Parâmetro inválido")

    adapter = GeminiAdapter(api_key="valid_key", client=mock_client)

    with pytest.raises(ValueError, match="Parâmetro inválido"):
        adapter.generate_text("Prompt de teste")

def test_generate_text_sdk_exception_raises_llm_error():
    mock_client = MagicMock()
    mock_client.models.generate_content.side_effect = Exception("Erro de conexão com o servidor Gemini")

    adapter = GeminiAdapter(api_key="valid_key", client=mock_client)

    with pytest.raises(LlmError, match="Falha na comunicação com a API do Gemini"):
        adapter.generate_text("Prompt de teste")
