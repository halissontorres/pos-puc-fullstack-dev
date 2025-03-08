# Banco de Dados NoSQL

Repositório dedicado às atividades e projetos desenvolvidos na disciplina de `Banco de Dados NoSQL` do Curso de [Pós-Graduação em Desenvolvimento Full Stack da PUCRS](https://online.pucrs.br/pos-graduacao/desenvolvimento-full-stack).

## Sobre a Disciplina

Introdução aos conceitos e características de Big Data como: volume,
velocidade, variedade, validade, volatilidade e valência. Introdução aos conceitos de
cluster, domínios, agregados, distribuição, tolerância a falhas e sharding. Estudo do
Teorema CAP: consistência (Consistency), disponibilidade (Availability), tolerância de
partição (Partition). Introdução a Bancos de dados sem esquema prévio, a Banco de
dados baseado em documentos, a Banco de dados chave-valor, a Banco de dados
colunar e a Banco de dados baseado em grafos.


## Conceitos

- Entidades: Representam objetos da realidade: pessoas, objetos inanimados, documentos, locais, eventos

**1ª Forma Normal (1FN)**: Remover valores duplicados, garantindo que cada coluna contenha um único valor atômico. Exemplo: em vez de listar múltiplos telefones em uma única coluna, criamos linhas separadas para cada telefone.
    
- **2ª Forma Normal (2FN)**: ==Eliminar dependências parciais==: após estar na 1FN, todos os atributos não-chave dependam totalmente da chave primária, eliminando dependências parciais e redundâncias. 
    
- **3ª Forma Normal (3FN)**: Remover dependências transitivas, garante que todos os atributos não-chave sejam independentes entre si e dependam exclusivamente da chave primária, eliminando dependências transitivas

---

> O teorema CAP diz que um sistema distribuído pode fornecer apenas duas de três características desejadas: 

1. **consistência**, 
2. **disponibilidade**
3. **tolerância a partições** 

> Do inglês: Consistency, Availability e **partition tolerance**

**Consistência**

Consistência significa que todos os clientes veem os mesmos dados ao mesmo tempo, independentemente do nó ao qual se conectam. Para que isso aconteça, sempre que os dados forem gravados em um nó, eles deverão ser imediatamente encaminhados ou replicados para todos os outros nós no sistema antes que a gravação seja considerada "sucesso".

**Disponibilidade**

Disponibilidade significa que qualquer cliente que faça uma solicitação de dados recebe uma resposta, mesmo que um ou mais nós estejam inativos. Outra forma de afirmar isso: todos os nós em funcionamento no sistema distribuído retornam uma resposta válida para qualquer solicitação, sem exceção.

**Tolerância à partição**

Uma partição é uma quebra de comunicação dentro de um sistema distribuído — uma conexão perdida ou temporariamente atrasada entre dois nós. Tolerância de partição significa que o cluster deve continuar funcionando apesar de qualquer número de quebras de comunicação entre nós no sistema.

### Modelos de Transações de SGBDs

#### Requisitos ACID:

- Atomicidade: Cada transação é executada corretamente ou o processo é interrompido e o banco de dados
volta ao estado anterior ao início da transação. Isso garante que todos os dados no banco de dados sejam válidos.

- Consistência: Uma transação processada nunca colocará em risco a integridade estrutural do banco de dados.

- Isolamento: As transações não podem comprometer a integridade de outras transações interagindo com elas
enquanto ainda estão em andamento.

- Durabilidade - Os dados relacionados à transação concluída persistirão mesmo nos casos de queda de rede ou energia. Se uma transação falhar, ela não afetará os dados manipulados.

#### Requisitos BASE

- BAsicamente disponível: Em vez de impor consistência imediata, os bancos de dados NoSQL modelados em BASE
garantirão a disponibilidade dos dados, espalhando-os e replicando-os pelos nós do cluster de
banco de dados.

- Soft state: Devido à falta de consistência imediata, os valores dos dados podem mudar ao longo do tempo. O modelo BASE rompe com o conceito de banco de dados que impõe sua própria consistência,
delegando essa responsabilidade aos desenvolvedores.

- Eventualmente consistente: O fato de o BASE não impor consistência imediata não significa que nunca a alcance. No entanto, até que isso aconteça, as leituras de dados ainda são possíveis (mesmo que não
reflitam a realidade).

---

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



