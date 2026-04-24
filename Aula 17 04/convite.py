# idade = int(input("Informe sua idade: "))
# convite = input("Possui convite? ")


# terminar = input("Deseja encerrar o sistema? ")
# while True:
#     nome = input("Informe seu nome ou (sair): ")
 
#     if idade < 16 and convite == "sim" or convite == "não":
#             print("Entrada negada.")
#     elif idade >= 16 and convite == "sim":
#             print("Entrada permitida.")
#     elif convite == "não":
#             print("Entrada negada.")
#     if terminar == "sim":
#         print("Sistema encerrado.")
#     break



while True:
    nome = input("Digite seu nome ou (sair)")
    
    if nome == "sair":
        print("Sistema encerrado.")
        break

    idade = int(input("Digite sua idade:"))
    convite = input("Possui convite? ")

    if idade < 16:
        print("Entrada negada.")
    elif idade >= 16 and convite == "sim":
        print("Entrada Permitida.")
    else:
        print("Entrada negada.")




