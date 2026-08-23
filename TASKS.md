# Checklist de Tarefas - Sprint 1: Setup Docker e Abstração do Motor LLM

> **Papel:** Agente Planejador  
> **Status:** Pronto para Execução (Sprint 1)  
> **Regra de Ouro:** O Agente Executor DEVE pausar e solicitar autorização do usuário humano antes de aplicar mudanças ou criar novos arquivos/estruturas. Não realizar `git commit` sem aprovação prévia.

---

## 1. Configuração do Ambiente Docker e Dependências
- [x] **1.1. Arquivo de Dependências (`requirements.txt`)**
  - Declarar as dependências do Back-end (Python 3.10+):
    - `google-genai` (SDK oficial da API Gemini)
    - `python-dotenv` (carregamento de variáveis de ambiente do `.env`)
    - `pydantic` (validação de schemas e configurações)
    - `pytest`, `pytest-cov`, `pytest-mock` (suíte de testes TDD e medição de cobertura)
- [x] **1.2. Dockerfile do Back-end (`Dockerfile`)**
  - Criar Dockerfile utilizando imagem base `python:3.10-slim`.
  - Definir diretório de trabalho `/app`.
  - Instalar dependências via `requirements.txt`.
  - Configurar variáveis de ambiente do Python (`PYTHONUNBUFFERED=1`, `PYTHONDONTWRITEBYTECODE=1`).
  - Definir o comando de entrada para rodar a suíte `pytest`.
- [x] **1.3. Orquestração com Docker Compose (`docker-compose.yml`)**
  - Definir o serviço `backend`.
  - Configurar montagem de volume local (`.:/app`) para refatoração e desenvolvimento ágil dentro do container.
  - Carregar arquivo `.env` para disponibilizar a variável `GEMINI_API_KEY`.
- [x] **1.4. Arquivo de Exemplo de Ambiente (`.env.example`)**
  - Criar modelo contendo `GEMINI_API_KEY=sua_chave_aqui`.

---

## 2. Estrutura Base em Fatias Verticais (Vertical Slice)
- [x] **2.1. Criação dos Diretórios Arquiteturais**
  - Criar estrutura conforme `ARCHITECTURE.md`:
    - `core/` e `core/llm/` (infraestrutura compartilhada)
    - `features/` e `features/generate_resume/` (fatias verticais para casos de uso)
    - `tests/`, `tests/core/` e `tests/features/` (suíte TDD)
- [x] **2.2. Módulo de Configurações Globais (`core/config.py`)**
  - Implementar leitor de configurações centralizado via `dotenv`/`pydantic`.
  - **Fail Fast:** Lançar exceção clara se `GEMINI_API_KEY` não for encontrada ao carregar o ambiente.

---

## 3. Camada de Abstração do LLM (Padrão Adapter)
- [x] **3.1. Interface/Contrato Abstrato (`core/llm/ports.py`)**
  - Criar o protocolo `LlmProtocol` usando `typing.Protocol`.
  - Definir a assinatura do método: `generate_text(self, prompt: str, **kwargs) -> str`.
  - Garantir o princípio de Inversão de Dependência (DIP) e Segregação de Interface (ISP).
- [x] **3.2. Adaptador Concreto do Gemini (`core/llm/gemini_adapter.py`)**
  - Implementar a classe `GeminiAdapter` aderente a `LlmProtocol`.
  - **Bouncer Pattern (Fail Fast):** Validar se o prompt de entrada é válido (não nulo, não vazio) antes de disparar a requisição ao SDK.
  - Injetar dependências (API key / client) via construtor `__init__`.
  - Tratar potenciais exceções da API/rede convertendo para exceções de domínio tratáveis.

---

## 4. Suíte de Testes TDD e CLI (Executados via Docker)
- [ ] **4.1. Testes Unitários dos Adapters (`tests/core/test_gemini_adapter.py`)**
  - Escrever testes TDD com `pytest-mock` para isolar requisições externas:
    - Testar retorno bem-sucedido de resposta do LLM.
    - Testar validação antecipada (*Fail Fast*) para prompts vazios ou inválidos.
    - Testar tratamento de erro em caso de falha no serviço remoto.
- [ ] **4.2. Teste de Integração Real/Semireal (`tests/core/test_llm_integration.py`)**
  - Criar teste de integração para validação no container, pulando de forma limpa (*skip*) se a API Key não estiver configurada no ambiente.
- [ ] **4.3. Ponto de Entrada CLI Inicial (`main.py`)**
  - Criar script `main.py` básico como ponto de entrada da CLI da Fase 1 para instanciar o `GeminiAdapter` e validar uma execução simples.
- [ ] **4.4. Validação de Cobertura de Testes (> 70%)**
  - Executar comando dentro do container: `docker-compose exec backend pytest --cov=core --cov=features --cov-report=term-missing`.
  - Verificar se a cobertura mínima de 70% foi atingida.

---

## 5. Protocolo de Qualidade e Aprovação
- [ ] **5.1. Validação Humana Antes de Aplicações**
  - Para cada tarefa relevante, o Executor deve exibir o plano de alteração e solicitar autorização antes de criar arquivos ou aplicar códigos.
- [ ] **5.2. Conclusão sem Commit Automático**
  - Finalizar com a mensagem: `"Aguardando revisão para commit."` após a aprovação de todos os testes dentro do container Docker.
