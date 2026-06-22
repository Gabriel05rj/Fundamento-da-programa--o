def cal_imc(peso: float, altura: float):
    imc = round(peso / altura ** 2, 1)
    if peso and altura <= 0:
        return - 1.0
    return imc

imc = cal_imc(70, 1.75)
print(f"IMC: {imc}")

imc2 = cal_imc(95, 1.70)
print(f"IMC: {imc2}")

invalido = cal_imc(-5, 1.70)
print(f"IMC: {invalido}")