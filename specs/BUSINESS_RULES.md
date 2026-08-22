# Regras de Negócio - Projeto Lugh

Este documento descreve as lógicas e diretrizes fundamentais que o sistema deve seguir. 

## Diretrizes para Agentes de IA
*   **Agente Planejador:** Ao planejar tarefas, certifique-se de que os fluxos de validação de dados atendam às regras de *Prevenção de Alucinação* e *Contexto Obrigatório*.
*   **Agente Executor:** Programe tratativas de erro explícitas para garantir que os requisitos abaixo sejam cumpridos pelo código. Não modifique as regras de negócio sem comando explícito. **Para toda alteração ou criação central de lógica de negócio (especialmente prompts da IA, validações e leitura de dados), você deve exibir um rascunho do código planejado e perguntar ao usuário se deve prosseguir com a aplicação.**
*   **Agente Revisor:** Audite as lógicas de engenharia de prompt (arquivos `prompts.py`) criadas pelo Executor. Gere um alerta no `REVIEW_REPORT.md` caso os prompts permitam que o LLM responda com formatações indevidas (como Markdown envelopando HTML) ou caso não instruam claramente contra alucinações de dados.

## 1. Geração de Currículo
*   **Contexto Obrigatório:** A geração do currículo exige a presença de dados do histórico do candidato e a descrição da vaga alvo. Se um deles faltar, o sistema deve abortar o fluxo e retornar um erro claro.
*   **Aderência à Vaga:** O LLM deve ser instruído a priorizar experiências e habilidades relacionadas aos requisitos da vaga, resumindo ou omitindo dados irrelevantes para manter a objetividade do documento final.
*   **Formato de Saída (Fase 1 e 2):** O artefato final gerado e salvo pelo motor de IA deve ser estritamente código HTML. É vedado o uso de invólucros de formatação Markdown (como ` ```html `) na string salva em disco.

## 2. Ingestão de Dados
*   **Formatos Suportados:** Na fase inicial, o sistema processará documentos `.pdf` e `.txt`.
*   **Prevenção de Alucinação:** O modelo de LLM externo deve ser instruído de forma estrita via prompt a não inventar cargos, habilidades, graduações ou períodos de tempo que não estejam presentes nos documentos originais fornecidos.

## 3. Persistência e Contas (A partir da Fase 3)
*   **Isolamento Multi-tenant:** Dados e arquivos de um usuário são estritamente isolados e acessíveis apenas através de seu identificador único ou token JWT.
*   **Reaproveitamento de Perfil:** Usuários com dados persistidos no banco de dados não precisam reenviar currículos base; o sistema compilará o contexto automaticamente, requerendo apenas a submissão da nova vaga alvo.