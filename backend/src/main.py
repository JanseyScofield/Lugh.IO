import sys
from core.config import load_config
from core.llm.gemini_adapter import GeminiAdapter

def main() -> None:
    print("Iniciando Lugh.IO Backend CLI (Fase 1)...")
    try:
        config = load_config()
        adapter = GeminiAdapter(api_key=config.gemini_api_key)
        print("Módulo de Configuração e Adaptador Gemini inicializados com sucesso!")
    except Exception as e:
        print(f"Erro na inicialização: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
