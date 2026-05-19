senha = "ads2026"
correta = False
max_tentativas = 3

for tentativa in range (max_tentativas):
    login = input("Registre sua Senha: ") 

    if login == senha:
        correta = True
        print("Senha correta, acesso concedido.")
        break
    else:
        restantes = (max_tentativas - tentativa) - 1

        if restantes > 0: 
            print(f"Senha Incorreta, {restantes} tentativas restantes")
        elif restantes == 0:
            print("Conta bloqueada, número de tentativas excedidas.")
