import os
import pytest
from core.config import load_config, Config

def test_load_config_success(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test_secret_key_12345")
    config = load_config(dotenv_path=None)
    assert isinstance(config, Config)
    assert config.gemini_api_key == "test_secret_key_12345"

def test_load_config_missing_key_raises_error(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    with pytest.raises(ValueError, match="GEMINI_API_KEY não foi encontrada"):
        load_config(dotenv_path=None)

def test_load_config_empty_key_raises_error(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "   ")
    with pytest.raises(ValueError, match="GEMINI_API_KEY não foi encontrada"):
        load_config(dotenv_path=None)

def test_load_config_placeholder_key_raises_error(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "sua_chave_aqui")
    with pytest.raises(ValueError, match="GEMINI_API_KEY não foi encontrada"):
        load_config(dotenv_path=None)

def test_load_config_with_custom_dotenv_file(monkeypatch, tmp_path):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    env_file = tmp_path / ".env"
    env_file.write_text("GEMINI_API_KEY=key_from_env_file\n")
    config = load_config(dotenv_path=str(env_file))
    assert config.gemini_api_key == "key_from_env_file"
