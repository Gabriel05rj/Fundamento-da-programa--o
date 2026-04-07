idade = int(input("Qual a sua idade?"))
salario = float(input("Qual seu salário?"))
tempo = int(input("Tempo de contribuição:"))
emprestimo = float(input("Qual o valor do empréstimo?"))
meses = int(input("Quanto tempo para pagar o empréstimo?"))

limite_salario = salario * 0.30
prestação = emprestimo / meses


if prestação > limite_salario and idade < 18 and tempo < 2  and salario < 2000: 
    print("Empréstimo NEGADO!")
elif idade < 18 or tempo < 2:
    print("Empréstimo NEGADO!")
elif prestação <= limite_salario and idade > 18 and tempo >= 2 and salario >= 5000:
    print("Empréstimo APROVADO!")
elif prestação <= limite_salario and idade > 18 and tempo >= 2 and salario >= 2000:
    print("Cliente está apto a receber o empréstimo.")
elif prestação > limite_salario:
    print("Empréstimo negado, excede 30%")
