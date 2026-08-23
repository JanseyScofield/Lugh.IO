# Padrão de Versionamento (Git Commits)

Sempre que você for sugerir a conclusão de uma task, você DEVE seguir estritamente o padrão de formatação abaixo. 

## 1. Fluxo de Submissão (NÃO EXECUTE O COMMIT)
*   **Apenas Sugestão:** Você está terminantemente PROIBIDO de executar o comando `git commit` no terminal.
*   **O seu papel:** Ao finalizar uma task, você deve escrever a mensagem de commit formatada no chat, exibi-la em um bloco de código bash (ex: `git commit -m "..."`) e pausar a execução.
*   **Revisão Humana:** O usuário humano lerá a sua sugestão. Se aprovada, o próprio usuário executará o comando no terminal dele ou pedirá para você rodar.

## 2. Estrutura Obrigatória da Mensagem
O formato da mensagem dentro das aspas deve ser: `<Tipo>(<Escopo>): <Mensagem curta>`

## 3. Tipos Permitidos
*   **Feat**: Para adição de novas funcionalidades ou features.
*   **Fix**: Para correção de bugs ou erros.
*   **Refact**: Para refatorações de código (mudanças que não adicionam features nem corrigem bugs, apenas melhoram a estrutura).

## 4. Escopos Permitidos
Você deve especificar a camada do software afetada entre parênteses:
*   **(Infra)**: Para arquivos de infraestrutura (Dockerfile, docker-compose.yml, CI/CD).
*   **(Back-end)**: Para arquivos da API, regras de negócio em Python, banco de dados ou adaptadores.
*   **(Front-end)**: Para arquivos de interface gráfica (React, Vite, Tailwind, UI/UX).
*   **(AI)**: Para alterações nas regras e skills (pasta `.ai/`) ou artefatos de coordenação criados por um agente para o consumo de outro (ex: `TASKS.md`, `REVIEW_REPORT.md`).

## 5. Regra da Mensagem
*   A mensagem explicativa deve conter **no máximo uma frase**.
*   Deve ser clara, direta e descrever exatamente o que foi alterado.

## Exemplos Válidos para o Chat
Quando for sugerir, entregue assim no chat para o usuário copiar:
`git commit -m "Feat(Back-end): Implementa a leitura de arquivos PDF no serviço de currículo."`
`git commit -m "Fix(Front-end): Corrige o alinhamento do botão de upload no mobile."`
`git commit -m "Refact(Infra): Otimiza a imagem do Docker com multi-stage build."`
`git commit -m "Feat(AI): Gera o checklist de tarefas da Sprint 1 para o executor."`