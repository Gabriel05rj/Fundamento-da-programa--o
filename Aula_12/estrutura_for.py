#contar de 1 até 5 - 

# for numero in range(1,6):
#     print(f'Eu sou o número {numero}')

# Exemplo tabuado do 5
i = 5 # varável no excopo global
for numero in range(1,11):
    total = i * numero  #variável no escopo local
    print(f'5 x {numero} = {total}')