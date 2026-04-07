idade_usuario = int(input("Qual a sua idade?"))
salario_usuario = float(input("Qual o seu salário?"))
tempo_usuario = int(input("Quantos anos de serviço?"))

# idade_usuario = 24 
# salario_usuario = 3000
# tempo_usuario = 4

# if idade_usuario < 18:
#      print("Empréstimo negado")
# elif salario_usuario < 2000:
#      print("Empréstimo negado: salário não atende os requisitos!")
# elif tempo_usuario < 2:
#      print("Empréstimo negado: tempo de trabalho insuficiente!")
# if salario_usuario >= 5000 and idade_usuario >= 18 and tempo_usuario >= 2:
#      print("Empréstimo aprovado automaticamento")
# else:
#      print(f"O cliente tem {idade_usuario} anos, salário de R${salario_usuario} e {tempo_usuario} anos de trabalho - empréstimo APROVADO!")

if idade_usuario >= 18 and salario_usuario >= 5000 and tempo_usuario >= 2:
    print("Condições atendidas, empréstimo APROVADO automaticamente!")
elif idade_usuario >= 18  and salario_usuario >= 2000 and tempo_usuario >= 2: 
    print("O cliente está apto a receber o empréstimo.")
else:
    print("Empréstimo NEGADO!")
