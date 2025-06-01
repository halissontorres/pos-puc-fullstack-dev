# Segurança de software

Repositório dedicado às atividades e projetos desenvolvidos na disciplina de `Segurança de software` do Curso de [Pós-Graduação em Desenvolvimento Full Stack da PUCRS](https://online.pucrs.br/pos-graduacao/desenvolvimento-full-stack).

## Sobre a Disciplina

Estudo sobre os métodos e utilização de criptografia para transmissão e armazenamento. Estudo sobre protocolo de comunicação em navegadores (`HTTPS`) ou aplicativos de conversa (`LibSignal`). Estudo sobre segurança no desenvolvimento de software. Estudo sobre os problemas mais frequentes indicados pela `OWASP`. Estudo sobre métodos de autenticação e autorização.


## Conceitos

### Organizações envolvidas na definição de padrões de segurança

> - ISO - Organização Internacional de Normalização
> - W3C - Consórcio World Wide Web
> - OWASP - Open Web Application Security Project
> - NIST - National Institute of Standards and Technology
> - IETF - Internet Engineering Task Force
> - PCI SSC - Payment Card Industry Security Standards Council

### Risco

> Acrônimo "CIO": 

- Capacidade
- Iniciativa
- Oportunidade

### Métodos de criptografia

> CRIPTOGRAFIA SIMÉTRICA: A mesma chave é usada para criptografar e descriptografar os
dados
- Geralmente mais rápida do que a criptografia assimétrica, pois não utiliza operações matemáticas com alto custo computacional.
- Depende da proteção adequada da chave secreta compartilhada. Se a chave secreta for comprometida, a segurança pode ser comprometida.
- Cenários em que a confidencialidade é o principal objetivo, como transações financeiras, comunicações militares e segurança de rede.

> CRIPTOGRAFIA ASSIMÉTRICA: Conhecida como criptografia de chave pública, é um método em que duas chaves diferentes são usadas para criptografar e descriptografar os dados.

- Utiliza um par de chaves: uma pública e uma privada.
- A chave pública é distribuída livremente e amplamente conhecida. Usada para criptografar os dados enviados.
- A chave privada é mantida em segredo pelo proprietário da chave e é usada para descriptografar os dados recebidos.

> FUNÇÕES HASH

- Emprega algoritmos matemáticos para transformar um conteúdo de tamanho variável em uma sequência de caracteres de tamanho fixa.
- Usadas principalmente para verificar a integridade dos dados.

### Modelo OSI

|Tipo | Camada    | Exemplo |
|---- | -------- | -------  |
|Dados   | 7 - Aplicação    | Interface com aplicativos    |
|Dados   | 6 - Apresentação | Formatos / criptografia     |
|Dados   | 5 - Sessão       | Controle de sessões entre aplicativos    |
|Segmento| 4 - Transporte   | Conexão entre hosts / ports
|Pacote  | 3 - Rede         | Endereço lógico / Roteadores
|Frame   | 2 - Enlace       | Endereço físico | switches e hubs
|Bit     | 1 - Física       | Hardware |

### Portas SMTPS

- portas 465 e 587

### AES-256

- Variação do AES que utiliza chave de 256 bits para a proteção de dados sensíveis

### LibSignal

- Biblioteca para criptografia de ponta a ponta para mensagens instantâneas


## Estrutura do Repositório

- `/exercicios`: Diretório contendo as atividades práticas


## Tecnologias e Ferramentas Utilizadas



## Aluno

- [Halisson Torres - GitHub](https://github.com/halissontorres)

- [Halisson Torres - Dockerhub](https://hub.docker.com/repository/docker/halissontorres/pos-graduacao-puc-rs/general)

## Licença

Este projeto está sob a licença [MIT](../LICENSE).

## Links adicionais


## Referências bibliográficas


## Docente

- Marcelo Brandalise
- Avelino Zorzo


