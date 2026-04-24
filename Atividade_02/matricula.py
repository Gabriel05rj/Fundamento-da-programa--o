idade = int(input("Digite sua idade: "))
nota = float(input("Digite sua nota: "))
presenca = int(input("Digite sua frequência escolar: "))

total_aulas = 200
frequencia = (presenca / total_aulas) * 100

if idade < 18:
    print("Matrícula negada, aluno menor de idade.")
elif idade < 18 and nota < 6 and frequencia < 75:
    print("Matrícula recusada.")
elif nota >= 9:
    print("Matrícula aprovada automaticamente.")
elif idade >= 18 and nota >= 6 and frequencia >= 75:
    print("Matrícula aprovada.")
else:
    print("Matrícula negada.")