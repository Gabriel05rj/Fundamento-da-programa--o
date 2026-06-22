def cal_imc(peso: float, altura: float):
    imc = round(peso / altura ** 2, 1)
    if peso and altura <= 0:
        return - 1.0
    return (imc)

def classificar_imc(imc, verificar_risco: bool=True) -> tuple:
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc <= 24.9:
        classificacao = "Peso normal ✅ "
    elif imc >= 25.0 and imc < 29.9:
        classificacao = "Sobrepeso ⚠️"
    elif imc >= 30:
        classificacao = "Obesidade ❌"

    alerta = "Risco cardiovascular elevado 🚨" if (verificar_risco and imc >= 30) else ""
    return  classificacao, alerta
    
classif, alerta = classificar_imc(22.9)
print(f"{classif} {alerta}")

classif2, alerta2 = classificar_imc(32.9)
print(f"{classif2} {alerta2}")

classif3, alerta3 = classificar_imc(27.3, verificar_risco=False)
print(f"{classif3} {alerta3}")