# Arquitetura do Sistema - Projeto Lugh

Este documento detalha as decisões técnicas, a stack e a organização dos componentes do software. O projeto baseia-se na **Vertical Slice Architecture (Arquitetura em Fatias Verticais)**, otimizada para ecossistemas de IA em Python, aliada aos princípios **SOLID** e **TDD**.

## Diretrizes para Agentes de IA
*   **Agente Planejador:** Utilize esta estrutura de diretórios como mapa para organizar as tarefas de implementação. Não planeje modificações arquiteturais globais sem autorização prévia.
*   **Agente Executor:** Você deve respeitar estritamente a arquitetura de Fatias Verticais. Não crie dependências cruzadas entre as pastas dentro de `features/`. Qualquer código reutilizável deve ser alocado na pasta `core/`. **Sempre que for implementar um novo Adapter, criar novos arquivos ou introduzir uma nova biblioteca, apresente o plano e pergunte ao usuário humano se tem autorização para prosseguir.**
*   **Agente Revisor:** Sua função primária é auditar o código do Executor. Barre qualquer submissão que viole os princípios SOLID, que fure o isolamento das features ou que não possua testes unitários correspondentes em `tests/`.

## 1. Stack Tecnológica
*   **Back-end:** Python 3.10+, FastAPI (Servidor a partir da Sprint 4), Pytest (Testes).
*   **Front-end:** React, Vite, TypeScript, Tailwind CSS, React Router Dom, Axios.
*   **Banco de Dados:** PostgreSQL (A partir da Sprint 7).
*   **Infraestrutura:** Docker e Docker Compose (desde a Sprint 1).

## 2. Estrutura Geral do Monorepo

O projeto adota uma estrutura de **Monorepo** com separação clara de responsabilidades entre a raiz do projeto (orquestração e configs globais), o **Back-end** (Python com `src-layout` e Vertical Slice) e o **Front-end** (React / TypeScript).

```text
Lugh.IO/
├── .ai/                      # Configurações do Agente IA (skills, contexto e regras)
│   ├── config.yml            # Triggers de contexto (backend/**, frontend/**) e instruções
│   └── skills/               # Instruções especializadas por domínio (backend.md, frontend.md, etc.)
├── docker-compose.yml        # Orquestrador global dos serviços (backend e frontend)
├── .env                      # Variáveis de ambiente globais (GEMINI_API_KEY, etc.)
├── .env.example              # Modelo de variáveis de ambiente
├── TASKS.md                  # Checklist de sprints e tarefas
├── specs/                    # Documentação de arquitetura e especificações
│   └── ARCHITECTURE.md
│
├── backend/                  # Serviço de Back-end (Python 3.10+)
│   ├── Dockerfile            # Dockerfile exclusivo do serviço de Back-end
│   ├── requirements.txt      # Dependências Python
│   ├── tests/                # Suíte de testes TDD (pytest)
│   │   ├── core/             # Testes de infraestrutura e adaptadores
│   │   └── features/         # Testes de integração/casos de uso
│   └── src/                  # Código-fonte isolado (Padrão src-layout)
│       ├── main.py           # Ponto de entrada (CLI Sprints 1-3, FastAPI Sprints 4+)
│       ├── core/             # Infraestrutura compartilhada
│       │   ├── config.py     # Leitor de ambiente Fail-Fast (Pydantic/dotenv)
│       │   └── llm/          # Camada de abstração de IA (LlmProtocol & GeminiAdapter)
│       └── features/         # Fatias verticais (Casos de Uso)
│           └── generate_resume/ # Feature: Geração de Currículo
│               ├── models.py # Schemas Pydantic de entrada/saída
│               ├── prompts.py# Templates de Prompt (Regra de Negócio)
│               ├── service.py# Orquestrador do caso de uso
│               └── router.py # Endpoints FastAPI da feature
│
└── frontend/                 # Serviço de Front-end (React, Vite, TS) [Sprints futuras]
    ├── Dockerfile            # Dockerfile exclusivo do serviço de Front-end
    ├── package.json          # Dependências Node.js
    └── src/                  # Código-fonte do Front-end
        ├── api/              # Comunicação HTTP (Axios / TanStack Query)
        ├── components/       # Componentes de UI reutilizáveis
        ├── pages/            # Páginas e roteamento
        └── types/            # Tipagens TypeScript
```

### Regras da Arquitetura Back-end

* **Isolamento de Feature:** Uma feature não deve depender da regra de negócio de outra feature. Código compartilhado desce para a pasta `backend/src/core/`.
* **O Prompt é Regra de Negócio:** A engenharia de prompt reside junto da feature que a utiliza.
* **Padrão `src-layout`:** Todo o código Python executável reside dentro de `backend/src/`, mantendo a raiz do serviço focada em testes e configurações.

## 3. Padrões de Design Aplicados

* **Vertical Slicing:** Foco na entrega ponta a ponta da funcionalidade em fatias coesas dentro de `features/`.
* **Adapter Pattern (Ports and Adapters):** O sistema depende da interface `LlmProtocol`. Qualquer IA externa é traduzida por um adaptador.
* **Dependency Injection:** Serviços recebem instâncias via parâmetros, facilitando a injeção de Mocks na suíte de testes.