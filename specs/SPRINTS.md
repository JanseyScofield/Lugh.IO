# Planejamento de Sprints - Projeto Lugh

Este documento define o roadmap de desenvolvimento do sistema. O projeto está dividido em sprints lógicas, começando pela validação do motor de IA em ambiente local estritamente via Docker, evoluindo até a plataforma web completa.

## Fluxo de Trabalho Multi-Agent (Instruções Operacionais)
O desenvolvimento de cada Sprint seguirá o pipeline de três agentes de IA:
1.  **Agente Planejador:** Lê o objetivo da Sprint atual neste documento, cruza com `ARCHITECTURE.md` e `BUSINESS_RULES.md`, e gera um arquivo `TASKS.md` contendo tarefas atômicas (Checklist) para a Sprint.
2.  **Agente Executor:** Consome o `TASKS.md` gerado. Escreve os testes (TDD) e, em seguida, escreve o código-fonte para passar nos testes. O Executor não altera as especificações, apenas implementa. **REGRA DE OURO: Para toda e qualquer mudança relevante no código (fechar uma task, introduzir um novo fluxo, alterar integrações), o Executor DEVE pausar e perguntar explicitamente ao usuário humano se deve prosseguir antes de aplicar/commitar a alteração.**
3.  **Agente Revisor:** Inspeciona os Pull Requests/Commits do Executor. Verifica a cobertura de testes, aderência à Arquitetura Vertical e gera um arquivo `REVIEW_REPORT.md` apontando bugs, falhas de segurança e dívidas técnicas para correção antes da aprovação final.

---

## Fase 1: Motor Local e CLI (Ambiente Dockerizado)

### Sprint 1: Setup Docker e Abstração do Motor LLM
**Objetivo:** Configurar o ambiente Python isolado em container, implementar o padrão Adapter para LLMs e validar a comunicação com a IA usando TDD.
*   Criar o `Dockerfile` inicial para o Back-end (Python 3.10+).
*   Criar o `docker-compose.yml` básico para rodar a suíte de testes e o script CLI.
*   Inicializar a estrutura Vertical Slice (`core`, `features`, `tests`).
*   Criar a interface abstrata `LlmProtocol` em `core/llm/ports.py`.
*   Implementar o `GeminiAdapter` em `core/llm/gemini_adapter.py`.
*   Escrever testes unitários e de integração para garantir a execução do prompt (Cobertura > 70%) rodando dentro do container.

### Sprint 2: Ingestão e Processamento de Arquivos Locais
**Objetivo:** Permitir que o sistema leia dados profissionais a partir de diretórios mapeados no container.
*   Atualizar o `docker-compose.yml` para mapear volumes locais (ex: `./data/input:/app/input`).
*   Implementar leitores de arquivos (`file_reader.py`) na feature `generate_resume` para extrair texto de `.pdf` e `.txt`.
*   Criar rotinas no `service.py` para varrer os diretórios de entrada.
*   Desenvolver a lógica de concatenação desses textos para formar o contexto bruto.

### Sprint 3: Engenharia de Prompt e Exportação HTML
**Objetivo:** Fechar o fluxo local, gerando e salvando o currículo formatado no volume de saída.
*   Atualizar o `docker-compose.yml` mapeando o volume de saída (`./data/output:/app/output`).
*   Desenvolver os templates no `prompts.py` para guiar a IA na geração de código HTML.
*   Implementar o fluxo completo no `service.py` que une a leitura de arquivos com a execução do LLM.
*   Criar o gerador que pega a string HTML retornada e salva na pasta de saída.

---

## Fase 2: Plataforma Web e Interface (Evolução para Servidor)

### Sprint 4: Refatoração para API (FastAPI) e Atualização da Infra
**Objetivo:** Expor o motor local através de endpoints HTTP.
*   Atualizar o `Dockerfile` do Back-end para expor a porta da API e rodar o servidor `uvicorn`.
*   Atualizar o `docker-compose.yml` para mapear a porta do host para o container.
*   Criar o arquivo `main.py` inicializando o FastAPI e configurando o Swagger.
*   Criar os endpoints em `router.py` da feature `generate_resume` para receber arquivos multipart.

### Sprint 5: Setup do Front-end (React) e Inclusão no Compose
**Objetivo:** Estruturar a base da aplicação cliente e orquestrá-la junto ao Back-end.
*   Inicializar o projeto React com Vite, TypeScript e Tailwind CSS.
*   Criar o `Dockerfile` dedicado para o Front-end.
*   Atualizar o `docker-compose.yml` adicionando o serviço `frontend` e mapeando a porta.
*   Criar a estrutura de pastas (`api`, `components`, `pages`, `types`).
*   Configurar o cliente Axios para se comunicar com o container do Back-end.

### Sprint 6: Interface de Geração de Currículo
**Objetivo:** Permitir a interação do usuário com a API através do navegador.
*   Criar componentes de UI (botões, inputs de arquivo, formulários).
*   Desenvolver a página principal para envio de dados profissionais e descrição da vaga.
*   Implementar o consumo do endpoint da API e renderizar/baixar o HTML retornado.

---

## Fase 3: Persistência, Contas e Orquestração Completa

### Sprint 7: Contas, Banco de Dados e Atualização de Infra
**Objetivo:** Adicionar a camada de persistência para salvar o histórico do usuário.
*   Atualizar o `docker-compose.yml` adicionando o serviço do PostgreSQL e volumes de dados.
*   Criar uma nova feature (ex: `manage_profile`) no Back-end.
*   Implementar acesso ao banco de dados no `core` e nas features necessárias.
*   Implementar autenticação JWT no Back-end e fluxo de login no Front-end.

### Sprint 8: Otimização de Imagens e Preparação para Produção
**Objetivo:** Refinar a infraestrutura Docker para garantir segurança e performance.
*   Refatorar os `Dockerfile`s para *multi-stage builds* (reduzindo o peso das imagens).
*   Configurar variáveis de ambiente estritas para produção.
*   Otimizar o build do Front-end para servir arquivos estáticos via Nginx.