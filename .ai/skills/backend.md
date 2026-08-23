# Skill Back-end: Python, FastAPI e Clean Code

## 1. Arquitetura (Vertical Slice)
*   O back-end é dividido em Funcionalidades (Features). Não crie dependências cruzadas entre pastas dentro de `features/`. Lógica compartilhada deve ir para a pasta `core/`.
*   O prompt do LLM é regra de negócio e deve residir no arquivo `prompts.py` da feature correspondente.

## 2. Código Pythonico e SOLID
*   **Tipagem Estrita:** O uso de *Type Hints* nativos é obrigatório (ex: `list[str]`, `dict[str, Any]`).
*   **Early Returns:** Valide condições de erro no início das funções e retorne/levante exceções imediatamente (Fail Fast).
*   **Padrão Adapter:** Obrigatório para integrações externas (como o Google Gemini). Use `typing.Protocol` para criar a interface que o serviço consumirá, aplicando Inversão de Dependência.

## 3. Testes (TDD)
*   Crie os testes no Pytest antes da implementação concreta, garantindo no mínimo 70% de cobertura para novos arquivos.

## 4. Controle de Versão e .gitignore
É fundamental manter o repositório limpo e seguro. Todo projeto Python deve garantir que os seguintes itens NUNCA sejam commitados:
*   **Segurança:** Arquivos de variáveis de ambiente (`.env`, `.env.local`).
*   **Caches e Compilados:** Pastas `__pycache__/`, arquivos `*.pyc`, `*.pyo`, e `*.pyd`.
*   **Testes e Cobertura:** Pastas `.pytest_cache/`, `htmlcov/` e arquivos `.coverage`.
*   **Ambientes Virtuais:** Pastas `venv/`, `.venv/`, `env/` ou `ENV/`.
*   **IDEs e SO:** Diretórios `.vscode/`, `.idea/` e arquivos `.DS_Store`.
O Agente Executor deve sempre configurar ou atualizar o `.gitignore` na raiz do projeto considerando estes padrões ao inicializar a infraestrutura.