# Banco de Dados Relacional

Repositório dedicado às atividades e projetos desenvolvidos na disciplina de `Banco de Dados Relacional` do Curso de [Pós-Graduação em Desenvolvimento Full Stack da PUCRS](https://online.pucrs.br/pos-graduacao/desenvolvimento-full-stack).

## Sobre a Disciplina

Visão geral da abordagem de banco de dados. Estudo sobre modelagem conceitual (E/R). Estudo sob mapeamento objeto relacional (ORM). Desenvolvimento com SQL padrão (DDL e DML)

## Conceitos

`Banco de dados`: Coleção de informações coerentes e inter-relacionadas que podem ser armazenadas em um sistema computacional.

`SGBG`: Sistema de gerenciamento de Banco de Dados. Sistema computacional que permite criar e administrar um banco de dados

`Metadados`: São informações descritivas de um banco de dados, normalmente chamados de "Dados sobre os dados".

`Minimundo`: ambiente ou contexto específico para o qual o banco de dados foi projetado.

`Modelo de dados`: Principal característica de um banco de dados. Ele oferecerá correlação, coerência e abstração.

`Cardinalidade`: Define graus de relação entre duas entidades. Podem ser de três tipos:
 - Um para muitos;
 - Um para um;
 - Muitos para muitos. 

## Modelo de dados conceitual

- `Modelo entidade-relacionamento - MER`: modelagem conceitual que descreve objetos de um negócio, suas características e como eles se relacionam;
- `Diagrama entidade-relacionamento - DER`: Utilizado para representar graficamente o que foi descrito no MER;

> `Entidade`: uma representação de um conjunto de informações sobre um conceito; São representados por retângulo no DER;

> `Atributo`: Característica de uma entidade. Representado por uma elípse;

> `Relacionamento`:  são associações entre entidades. Representado por losangos. 

> `Constraints`: regras que definem limitações aos dados que podem ser inseridos ou modificados em uma tabela de um banco de dados. 

> `Chave primária`:  é um campo que identifica de forma única cada linha de uma tabela de banco de dados

> `Chave estrangeira`: é um campo que permite estabelecer uma relação entre tabelas de um banco de dados

> `Surrogate key`: Uma chave substituta (ou chave sintética, pseudochave, identificador de entidade, chave sem fatos ou chave técnica) em um banco de dados é um identificador exclusivo para uma entidade no mundo modelado ou um objeto no banco de dados


## Estrutura do Repositório

- `/exercicios`: Diretório contendo as atividades práticas

## Tecnologias e Ferramentas Utilizadas

 - [SQLite](https://www.sqlite.org/): biblioteca de linguagem C que implementa um mecanismo de banco de dados SQL pequeno, rápido, autocontido, de alta confiabilidade e completo. 

 - [Draw IO](https://www.drawio.com/): Editor online para diagramas 

 - [LiveSQL Oracle](ivesql.oracle.com) 

 - [Download brModelo 3.2](https://www.brmodeloweb.com/lang/pt-br/index.html)

## Aluno

[Halisson Torres - GitHub](https://github.com/halissontorres)

## Licença

Este projeto está sob a licença [MIT](../LICENSE).



## Referências bibliográficas

- BONEL, Claudio. Metodologia E Engenharia De Requisitos Para Projetos De Business Intelligence. Clube de Autores, 2021.
- COPELAND, Rick. Essential sqlalchemy. 2. ed. O'Reilly Media, Inc., 2016.
- ELMASRI, Ramez; NAVATHE, Shamkant B. Sistemas de banco de dados. 7 ed. São Paulo: Pearson Education do Brasil, 2018.
- SQLite. Datatypes in SQLIte. Disponível em https://www.sqlite.org/datatype3.html. Acesso: 25/07/2022



## Docente

- Prof. Azriel Majdenbaum
- [Prof. Claudio Bonel](https://github.com/claudiobonel/pucrs-banco_de_dados_relacional/)



