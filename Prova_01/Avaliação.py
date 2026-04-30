Nomes = []
quantidade = int(input("Informe a quantidade de alunos da turma: "))

i = 0
# while True:
while i < quantidade:
       print(f'\n Cadastro dos alunos {i + 1}')
    #    if quantidade == "0":
    #          break
       
       nome = input("Informe seu nome: ")
       nota01 = float(input("Digite sua nota: "))
       nota02 = float(input("Digite sua nota: "))
       nota03 = float(input("Digite sua nota: "))
       
       notas = [nota01, nota02, nota03]
       media = sum(notas) / 3
       
       print(f"{media:.2f}")
       
       print('''\n---Tabela de notas:
             [1] Aprovado (7,0 +)
             [2] Recuperação (5,0 - 6,9)
             [3] Reprovado( < 5,0)
             ---''')
       tabela = input("Escolha uma opção: ")

       situacao = "";
      
       if tabela == "1":
            if media >= 7.0:
                situacao = "Aprovado";
                registro = f"Aprovado. {media:.1f}"
                print("Aluno aprovado!!!")
            else:
                print("Nota em correção.")
                
       elif tabela == "2":
                if media >= 5.0 and media < 7.0:
                     situacao = "Recuperação";
                     registro = f"Em Recuperação.{media:.1f}"
                     print("Aluno em Recuperação. Estude mais.")
                else:
                     print("Notas em avaliação")
                     
       elif tabela == "3":
                    if media < 5.0:
                        situacao = "Reprovado";
                        registro = f"Reprovado.{media:.1f}"
                        print("❌Aluno reprovado ❌")
                    else:
                        print("Notas em avaliação")

       print(f"Aluno: {nome}")

       aluno = {
        "nome": nome,
        "nota1": nota01,
        "nota2": nota02,
        "nota3": nota03,
        "media": media,
        "situacao": situacao
       }
       Nomes.append(aluno) 

       i += 1

for aluno in Nomes:
    print("\n-----------------------")
    print(f"Nome: {aluno['nome']}")
    print(f"Nota 1: {aluno['nota1']:.2f}")
    print(f"Nota 2: {aluno['nota2']:.2f}")
    print(f"Nota 3: {aluno['nota3']:.2f}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"situacao: {aluno['situacao']}")