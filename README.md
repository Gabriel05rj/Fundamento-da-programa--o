# ANOTAÇÕES DE FUNDAMENTOS DA PROGRAMAÇÃO

## Tipos de dados em python
1. string
2. number int 
3. number float
4. boolean

## Operadores Matemáicos - basicos
+ -> adição
- -> subtração
* -> multiplicação
/ -> divisão 

## Métodos em python
1. print() -> exibe informações no terminal

## Format em pyhon

# Estrutura condicional
``#if (se)`` -> verifica se uma condição é true (verdade).Se for, ele executa o código.
``elif (senão se)`` -> é usado para testar várias condições.Ele só executa se todas as condições anteriores forem falsas.
``else (senão)`` -> Executa o código se a condição for false(falsa).

# Laços de Repetição
É um recurso de programação que permite executar um conjunto de comando várias vezes. Também são chamados de Loop, Laços de repetição ou iteração.
'FOR' -> Utilizamos quando sabemos quantas vezes queremos repetir algo.
sintax:
for (variável) in range(início,fim):
    comandos
[range()] -> Método que aceita geração de números
[início] -> é inclusivo, é o primeiro número a ser usado
[fim] -> é exclusivo, o penúltimo número é utilizado
## Escopo das Variáveis
`Escopo Local` -> a variável ela só é acessada dentro da estrutura que ela foi criada.
`Escopo Global` -> a variável pode ser acessado por todo mundo.

## Variações das variáveis
Variável em Memória -> é declarada quando você não pretende utilizar essa variável em outros cenários.
Variável Contador -> é utilizada para uma lógica onde a repetição irá ser alterada.

`WHILE` -> É utilizada quando não sabemos quantas vezes o programa vai repetir. Ele repete enquanto uma condição for verdadeira.
sintax:
while condicao:
    comandos


## Conversão de tipos em Python
1. int() -> a gente vai incluir qual variável/dado que queremos converter para número inteiro.
2. float() -> a gente vai incluir qual variável/dado que queremos converter para número decimal.
3. str() -> a gente vai incluir qual variável/dado que queremos converter para texto.