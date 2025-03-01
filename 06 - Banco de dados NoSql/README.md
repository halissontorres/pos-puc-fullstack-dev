# Banco de Dados NoSQL

Repositório dedicado às atividades e projetos desenvolvidos na disciplina de `Banco de Dados NoSQL` do Curso de [Pós-Graduação em Desenvolvimento Full Stack da PUCRS](https://online.pucrs.br/pos-graduacao/desenvolvimento-full-stack).

## Sobre a Disciplina


## Conceitos

- Entidades: Representam objetos da realidade: pessoas, objetos inanimados, documentos, locais, eventos


## Estrutura do Repositório

- `/exercicios`: Diretório contendo as atividades práticas

## Tecnologias e Ferramentas Utilizadas

> `Apache Cassandra`

**Tipo**: Banco de dados NoSQL orientado a colunas (wide-column store), distribuído e altamente escalável.

> Principais características:

- Arquitetura descentralizada: Modelo peer-to-peer sem single point of failure, ideal para alta disponibilidade.

- Escalabilidade horizontal: Adicione nós facilmente para lidar com grandes volumes de dados (PB-scale).

- Tolerância a falhas: Replicação automática de dados entre nós e datacenters.

- Consistência tunável: Permite ajustar o equilíbrio entre consistência e disponibilidade (PACELC).

- Desempenho em escritas: Otimizado para cargas de trabalho intensivas em gravação (ex: IoT, logs).

- Query Language: CQL (Cassandra Query Language), semelhante ao SQL, mas com limitações (ex: sem joins).

> Casos de uso:

- Sistemas de mensagens (ex: Instagram Direct), métricas em tempo real, catálogos de produtos, registros de transações.

- Empresas que usam: Netflix, Apple, Uber.

---

> `MongoDB`

**Tipo**: Banco de dados NoSQL orientado a documentos (JSON-like BSON).

> Principais características:

- Esquema flexível: Estrutura de documentos dinâmicos, ideal para modelos de dados evolutivos.

- Indexação avançada: Suporta índices compostos, geoespaciais e de texto.

- Escalabilidade horizontal: Sharding automático para distribuir dados.

- Aggregation Framework: Pipeline para transformações complexas de dados.

- Replicação: Replica sets para alta disponibilidade e recuperação de desastres.

- Query Language: MongoDB Query Language (MQL), com operações CRUD e suporte a JavaScript.

> Casos de uso:

- Aplicações web (ex: perfis de usuário), conteúdo gerado por usuários (CMS), análise em tempo real.

- Empresas que usam: eBay, Adobe, Forbes

---

> `Redis`

**Tipo**: Banco de dados in-memory de estrutura de dados (key-value store), usado também como cache e broker de mensagens.

>     Principais características:

- Baixa latência: Dados armazenados na RAM, com operações em microssegundos.

- Estruturas de dados ricas: Strings, listas, sets, sorted sets, hashes, streams, e módulos (ex: JSON, grafos).

- Persistência opcional: Snapshots (RDB) e logs append-only (AOF).

- Funcionalidades avançadas: Pub/Sub, transações, Lua scripting, clustering.

- Single-threaded: Evita concorrência complexa, mas otimizado para throughput.

> Casos de uso:

- Cache de sessão (ex: carrinhos de compra), leaderboards em tempo real (ex: jogos), filas de tarefas (Redis Streams).

- Empresas que usam: Twitter, GitHub, StackOverflow.

 ---

 > `Neo4j`

**Tipo** : Banco de dados de grafos nativo, focado em relacionamentos entre entidades.

> Principais características:

- Modelo de grafos: Armazena nós, relacionamentos e propriedades, com ênfase em conexões.

- Cypher Query Language: Linguagem declarativa para consultas complexas de grafos (ex: caminhos mais curtos).

- ACID-compliant: Transações seguras e consistência forte.

- Algoritmos de grafos: PageRank, Centralidade, Detecção de comunidades.

- Integração com IA: Compatível com frameworks como Graph Data Science Library.

> Casos de uso:

- Redes sociais (recomendações), detecção de fraudes (padrões suspeitos), gerenciamento de redes (ex: telecomunicações).

- Empresas que usam: NASA, Airbnb, Walmart.

---

> `ScyllaDB`

**Tipo**: Banco de dados NoSQL orientado a colunas (wide-column store), projetado para substituir o Apache Cassandra com desempenho superior.

>     Principais características:

- Alta performance: Escrito em C++ (em vez de Java, como o Cassandra), utiliza um modelo shared-nothing e arquitetura shard-per-core (cada núcleo da CPU gerencia uma fatia dos dados), reduzindo latência e aumentando throughput.

- Compatibilidade com Cassandra: Suporta o mesmo CQL (Cassandra Query Language), drivers, e formato de dados SSTable, permitindo migração simplificada.

- Escalabilidade horizontal: Adiciona nós sem downtime e escala linearmente para petabytes de dados.

- Arquitetura otimizada:

    - Usa o framework Seastar para operações assíncronas e não bloqueantes.

    - Auto-otimização: Balanceamento automático de carga e compactação de dados eficiente (ex: Incremental Compaction).

    - Consistência tunável: Similar ao Cassandra (PACELC), com suporte a níveis como ONE, QUORUM, e ALL.

    - Baixo custo operacional: Consome menos recursos (CPU/RAM) que o Cassandra, graças à otimização de garbage collection e alocação de memória.

    - Time-series nativo: Projetado para cargas de trabalho com alta ingestão de dados temporais (ex: IoT, métricas).

> Casos de uso:

- Aplicações que exigem baixa latência (<1 ms) e alta vazão (ex: jogos online, ad-tech, telecomunicações).

- Substituição do Cassandra em ambientes que demandam mais performance com menos hardware.

- Dados sensíveis ao tempo: Monitoramento em tempo real, telemetria, logs distribuídos.

- Empresas que usam: Discord, Comcast, Samsung, Bloomberg.

## Aluno

[Halisson Torres - GitHub](https://github.com/halissontorres)

## Licença

Este projeto está sob a licença [MIT](../LICENSE).

## Links adicionais

## Referências bibliográficas

## ferramentas

- [Astah](https://astah.net) Ferramenta de modelagem da UML - Unified Modeling Language


## Docente

- Prof. MSc. Eduardo Henrique Pereira Arruda
- Prof. Vinícius Kroth 



