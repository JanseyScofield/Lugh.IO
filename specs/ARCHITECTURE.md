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

## 2. Arquitetura do Back-end (Vertical Slice)
O sistema é organizado por **Funcionalidades (Features)**. Isso garante alta coesão e facilita a manutenção do fluxo de IA.

### Estrutura de Diretórios
```text
backend/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── main.py                   # Ponto de entrada (CLI nas Sprints 1-3, FastAPI nas Sprints 4+)
│
├── core/                     # Infraestrutura base compartilhada
│   ├── config.py             # Gestão de variáveis de ambiente (.env)
│   └── llm/                  # Abstração de Inteligência Artificial
│       ├── ports.py          # A interface/contrato abstrato (ex: LlmProtocol)
│       └── gemini_adapter.py # Implementação concreta (Padrão Adapter)
│
├── features/                 # As fatias verticais (Casos de Uso)
│   └── generate_resume/      # Feature: Geração de Currículo
│       ├── models.py         # Estruturas de dados de entrada e saída
│       ├── prompts.py        # Templates de prompt (Regra de negócio da IA)
│       ├── file_reader.py    # Lógica de extração de texto
│       ├── service.py        # Orquestrador da feature
│       └── router.py         # Endpoints FastAPI para esta feature
│
└── tests/                    # Suíte de TDD (Cobertura mínima de 70%)
    ├── core/                 # Testes unitários para adaptadores
    └── features/             # Testes das funcionalidades

```

### Regras da Arquitetura Back-end

* **Isolamento de Feature:** Uma feature não deve depender da regra de negócio de outra feature. Código compartilhado desce para a pasta `core/`.
* **O Prompt é Regra de Negócio:** A engenharia de prompt reside junto da feature que a utiliza.

## 3. Arquitetura do Front-end

Separado logicamente entre a camada de comunicação de rede (API) e a de renderização (UI).

```text
frontend/
├── src/
│   ├── api/               # Comunicação com o Back-end
│   │   ├── client.ts      # Instância configurada do Axios
│   │   ├── commands/      # Mutações (POST, PUT, DELETE)
│   │   └── queries/       # Consultas (GET)
│   ├── components/        # UI reutilizável (Botões, Inputs)
│   ├── pages/             # Telas completas roteáveis
│   ├── types/             # Tipagem estática TypeScript
│   ├── App.tsx            # Roteamento e layouts base
│   └── index.css          # Setup do Tailwind

```

## 4. Padrões de Design Aplicados

* **Vertical Slicing:** Foco na entrega ponta a ponta da funcionalidade em pastas coesas.
* **Adapter Pattern (Ports and Adapters):** O sistema depende da interface `LlmProtocol`. Qualquer IA externa é traduzida por um adaptador.
* **Dependency Injection:** Serviços recebem instâncias via parâmetros, facilitando a injeção de Mocks na suíte de testes.