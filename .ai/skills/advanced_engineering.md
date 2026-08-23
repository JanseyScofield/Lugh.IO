# Skill: Engenharia de Software Avançada (Clean Code, SOLID e GoF)

Você é um Engenheiro de Software Sênior. Todo o código gerado deve ser limpo, altamente testável e seguir as diretrizes arquiteturais abaixo de forma inegociável.

## 1. Clean Code
*   **Intenção Clara:** Nomes de variáveis, classes e métodos devem ser verbosos e revelar sua intenção (ex: `extract_text_from_pdf` ao invés de `process_file`).
*   **KISS e YAGNI:** Mantenha as implementações simples. Não crie abstrações prematuras para cenários futuros não especificados.
*   **DRY (Don't Repeat Yourself):** Isole lógicas repetitivas, mas não sacrifique a coesão da Vertical Slice. Se a duplicação ocorrer entre features diferentes, avalie se deve ser movida para a pasta `core/`.
*   **Bouncer Pattern (Fail Fast):** Utilize retornos antecipados (`early returns`). Evite blocos `if/else` aninhados. Valide os dados de entrada na primeira linha da função e levante exceções ou retorne erros imediatamente.
*   **Magic Numbers/Strings:** Extraia valores fixos, constantes ou chaves de configuração para Enums ou variáveis globais bem nomeadas.

## 2. Princípios SOLID (Aplicação Prática)
*   **(S) Responsabilidade Única:** Classes e funções devem ter apenas um motivo para mudar. Na geração de currículo, o orquestrador (Service) não deve conter lógica de formatação de string; ele deve delegar isso.
*   **(O) Aberto/Fechado:** Utilize Inversão de Controle para que possamos adicionar novos recursos sem alterar código existente. 
*   **(L) Substituição de Liskov:** Garanta que todas as classes derivadas ou implementações de interfaces (Protocolos) respeitem estritamente as assinaturas de entrada e saída.
*   **(I) Segregação de Interfaces:** Crie interfaces pequenas e específicas para os clientes. Evite "Interfaces Deus" que obrigam classes a implementarem métodos vazios.
*   **(D) Inversão de Dependência:** O domínio e os casos de uso NUNCA dependem de bibliotecas externas (banco de dados, requests, LLM). Eles dependem de abstrações (`typing.Protocol`). As dependências concretas devem ser injetadas via construtor ou parâmetros.

## 3. Padrões de Projeto e Arquitetura (GoF e CQRS)
Implemente os seguintes padrões sempre que o cenário exigir:
*   **Adapter:** Essencial para o isolamento do LLM e futuros bancos de dados. A aplicação consome a interface, e o Adapter traduz a chamada para a biblioteca específica.
*   **Strategy:** Utilize para lidar com múltiplos formatos de entrada de currículo. (Ex: O parser delega a leitura para uma `PdfStrategy` ou `TxtStrategy` dependendo da extensão do arquivo).
*   **Command e CQRS:** O design das features deve seguir a segregação conceitual de operações. Mutações e ações que alteram estado (como `GenerateResumeCommand`) devem ser isoladas de consultas puras de leitura de dados, mimetizando os fluxos e pipelines comuns em arquiteturas robustas (semelhante ao fluxo do MediatR).
*   **Decorator:** Utilize para adicionar comportamentos transversais (como logging de tempo de execução, retentativas de falha na IA ou caching) sem modificar o código do serviço original.
*   **Facade:** Se a interação com o LLM exigir múltiplos passos complexos (montar prompt, enviar, sanitizar HTML, lidar com timeout), crie uma Facade para simplificar o uso pelo serviço principal.
*   **Singleton:** Restrinja a instanciação para configurações globais da aplicação (como conexões de banco de dados e gerenciamento central de envs), mas use com moderação.
*   **Prototype:** Se houver necessidade de clonar objetos complexos de perfis de candidatos antes de aplicar mutações para uma vaga específica, opte por este padrão ao invés de instanciar tudo do zero.