#Variáveis e tipos de dados:
# em Python vc não precisa declarar o tipo de uma variável antes usá-la.O tipo é inferido automaticamente pelo interpretador. 
#Em Python a váriavel é declarada no padrão snake_case.
#1 - String ->
#2 - numeber - Int (numero inteiro) ->
#3 - number - float (nnumero decimal) ->
#4 - boolen - True or False (Verdadeiro ou Falso) ->

nome = "Gabriel" # string
email = "gabriel@gmail.com" # string
cidade = "Rio de Janeiro" # string
cpf = 14358697220 # number-int
salario = 14000.65 # number-float
casado = False # boolen-False(nesse caso)

format = "formulário" 

#operadores matematicos 
# + soma
# - subtração
# * multiplicação
# / divisão
# ** potenciação(% resto da div 
#atribuir valores a uma variável e colocar dentro do print()
#ex:
a = 20
b = 25
print(a + b)
#existem prioridades para as contas ou seja, para diferentes contas deve se levar em consideração as prioridades ex: ()

a = 15 
b = 10
resultado = (a + b) * 2 + 10
print(resultado) 

#f-string = associa expressões e variáveis em uma só linha 
itens = 2
c = 7
custo = c + b
resultado = f"Total da sua compra eh R${custo} para {itens} itens"
print(resultado)

