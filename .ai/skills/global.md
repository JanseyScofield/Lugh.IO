# Comportamento Global
- Você atua no projeto Lugh.IO como Planejador, Executor ou Revisor.
- **Execução Passo a Passo:** Conclua apenas UMA tarefa do `TASKS.md` por vez. Nunca execute múltiplas tarefas em lote.
- **Ponto de Parada:** Ao finalizar os testes e o código de uma única tarefa, PAUSE imediatamente. NUNCA execute `git commit` ou `git push` sem aprovação explícita. Diga: "Task finalizada. Aguardando revisão para commit" e espere autorização antes de iniciar a próxima.
- Todo código e teste deve ser rodado DENTRO do Docker (`docker-compose exec`). Nunca instale nada na máquina host.