# Programação Orientada a Objetos

Repositório dedicado às atividades e projetos desenvolvidos na disciplina de `Programação Orientada a Objetos` do Curso de [Pós-Graduação em Desenvolvimento Full Stack da PUCRS](https://online.pucrs.br/pos-graduacao/desenvolvimento-full-stack).

## Sobre a Disciplina

Esta disciplina aborda conceitos fundamentais de programação e orientação a objetos, incluindo:

- Classes
- Herança
- Polimorfismo
- Interfaces
- Tipos Genéricos
- _Arrow functions_

## Conceitos

Paradigma: é uma forma de fazer algo.

No paradigma orientado a objeto o foco é em objetos do mundo real, ou seja, um estilo de programa. Por outro lado, a programação funcional o foco é em funções.

Dentre esses conceitos, aplicam-se: 
- `Abstração`: Capacidade de identificar os aspectos essenciais de um problema e ignorar detalhes irrelevantes  ;
- `Encapsulamento`: Permitir que os atributos e métodos sejam agrupados de certa forma em uma interface bem definida para manipular os dados de um objeto de forma eficiente. Saber o que o objeto faz e não como o faz;
- `Herança`: permite identificar e agrupar comportamentos generalizados ou especializados, e favorece o reaproveitamento de código; e
- `Polimorfismo`: princípio que permite que um mesmo método ou função tenha diferentes comportamentos dependendo do objeto que o invoca;
- `Protótipo`: Em javascript, é um mecanismo de herança entra objetos que fornece atributos e métodos.

> 💡 Visibilidade: O identificador prefixado `#atributo` torna-o privado.

```javascript
class Pessoa {
      #id;
      constructor(nome, idade, cpf){
        this.nome = nome;
        this.idade = idade;
        this.#id = cpf;
      }

      getCpf = () => this.#id.toString();
}
``` 

> 💡 Característica de `for-in` e `for-of`
 
Considere:

```javascript
var a = [];
a[0] = 'a';
a[1] = 'b';
a[9] = 'c';
console.log(a.length); // Imprime 10

for(let val in a)
console.log(" --> "+val); //Imprime os índices ocupados: 0,1 e 9
console.log('')

for(let val of a)
console.log(" --> "+val); //Imprime os valores existentes, inclusive undefined
```

## Estrutura do Repositório

- `/exercicios`: Diretório contendo as atividades práticas
- `/exemplos_da_aula`: Exemplos apresentados pelo Professor

## Tecnologias Utilizadas


## Aluno

[Halisson Torres - GitHub](https://github.com/halissontorres)

## Licença

Este projeto está sob a licença [MIT](../LICENSE).

## Links adicionais

- [PUC-RS | GitHUb](https://github.com/empucrs/DesenvolvimentoFullStack)
- [MDN Web docs](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)

## Referências bibliográficas

- Concepts of Programming language, Robert W. Sebesta
- Clean code, Robert Cecil Martin
- Refactoring | Martin Fowler

## Docente
- Alessandro Valério Dias
- Edson Ifarraguirre Moreno