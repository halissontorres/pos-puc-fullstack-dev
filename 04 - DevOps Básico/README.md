# DevOps Básico

Repositório dedicado às atividades e projetos desenvolvidos na disciplina de `DevOps Básico` do Curso de [Pós-Graduação em Desenvolvimento Full Stack da PUCRS](https://online.pucrs.br/pos-graduacao/desenvolvimento-full-stack).

## Sobre a Disciplina

Introdução aos fundamentos de gerência de configuração. Estudo sobre Integração contínua (CI). Utilização de contêineres, ferramentas e ambientes direcionados ao desenvolvimento de software como Git, GitHub, Maven, Gradle, Npm, Yarn, GitHub Actions, Jenkins, Travis e Docker.

## Conceitos

> Devops: Conjunto de práticas que integra os times de desenvolvimento (devs) e Operações (Ops), que busca maior colaboração, automação e eficiência para o produto e para a entrega.

Focado em três modos:

- `Fluxo`: Análise e otimização dos processos, testes, integração contínua e deploy contínuo, entregas de baixo risco;
- `Feedback`: Implementar e coletar métricas, Observabilidade, Testa A/B, Feedback dos resultados para replanejamento 
- `Aprendizado contínuo e Experimentação`: Aprender com os erros, Experimentação controlada, Disseminar o conhecimento e padronizar os acertos

> Observabilidade: Na teoria do controle, ela determina quão bem podem os estados de um sistema ser inferidos a partir do conhecimento de suas saídas

> Teste A/B: Métodos de testes de design mediante o qual são comparados elementos aleatórios com duas variáveis, A e B, em que estes são o controle e o tratamento de uma experiência controlada.

> **Twelve Factors App**: são um conjunto de boas práticas para o desenvolvimento de aplicações **SaaS** (Software as a Service) modernas, escaláveis e portáteis. Esse modelo foi criado por engenheiros da **Heroku** e define princípios para construir aplicações robustas, independentes da infraestrutura e fáceis de implantar e manter.
> - `Base de Código Única`: repositório único;
> - `Dependências Explícitas`: Todas as dependências devem ser declaradas explicitamente (maven, gradle, npm, pip);
> - `Configuração no Ambiente`: devem ser armazenadas em variáveis de ambiente e nunca no código-fonte;
> - `Serviços Externos como Recursos`: Serviços externos devem ser tratados como recursos consumíveis via URLs ou conexões
> - `Build, Release, Run (Ciclos Separados)` – O processo de build (compilação), release (configuração) e run (execução) deve ser separado para garantir previsibilidade nos deploys;
> - `Processes (Execução como Processos Independentes)` – A aplicação deve ser composta por processos stateless e independentes
> - `Port Binding (Vinculação a Portas)` – A aplicação deve expor serviços via uma porta (ex.: HTTP) e não depender de servidores externos como Apache ou Nginx embutidos;
> - `Concurrency (Escalabilidade via Processos)` – A escalabilidade deve ser feita aumentando o número de processos leves ao invés de depender de threads internas
> - `Disposability (Robustez e Restart Rápido)` – Processos devem ser rápidos para iniciar e terminar de forma graciosa para facilitar escalabilidade e recuperação de falhas
> - `Dev/Prod Parity (Paridade entre Ambientes)` – O ambiente de desenvolvimento deve ser o mais semelhante possível ao de produção para evitar surpresas nos deploys.
> - `Logs (Tratar Logs como Fluxo de Eventos)` – Logs devem ser escritos em `stdout` e gerenciados por um sistema externo, não armazenados localmente.
> - `Admin Processes (Tarefas Administrativas como Processos Únicos)` – Tarefas administrativas (como migrações de banco ou execução de scripts) devem ser executadas separadamente, sem impacto no ambiente principal.

> Containers

Características:
- Isolamento entre processos;
- Controle de processos;
- `Idempotência`: descreve uma operação que sempre leva ao mesmo resultado, não importando quantas vezes você a execute; 
- Portabilidade;
- Confiabilidade de comportamento

- `Imagem`: Elemento base para criar um container
- `Container`: Um container é um ambiente de software padronizado que inclui tudo o que um aplicativo precisa para ser executado

## Estrutura do Repositório

- `/exercicios`: Diretório contendo as atividades práticas

## Pipeline

> `Definição`: é uma sequência automatizada de processos que orquestra a construção, testes e implementação de software, desde a codificação até a produção, promovendo a colaboração entre desenvolvimento e operações

## Tecnologias e Ferramentas Utilizadas

- [Git](https://git-scm.com/)
- [GitHub](https://github.com)
- Conteiners ([Docker](https://www.docker.com/))
- Banco de Dados NOSql ([MongoDB](https://www.mongodb.com/pt-br))
- [Robot 3T](https://robomongo.org/)


## Aluno

- [Halisson Torres - GitHub](https://github.com/halissontorres)

- [Halisson Torres - Dockerhub](https://hub.docker.com/repository/docker/halissontorres/pos-graduacao-puc-rs/general)

## Licença

Este projeto está sob a licença [MIT](../LICENSE).

## Links adicionais

- [GitHub | Projeto da aula | Repositório do professor Veronez](https://github.com/KubeDev/conversao-temperatura)
- [GitHub | Clone do projeto | Repositório Halisson](https://github.com/halissontorres/conversao-temperatura)


## Referências bibliográficas

- The devops adoption playbook | Shajeev Sharman

## Docente

- [GitHub | Prof. Fabrício Veronez](https://github.com/fabricioveronez)
- Marco Aurélio Souza Mangan


