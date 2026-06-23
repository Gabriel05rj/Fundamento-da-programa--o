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

def emitir_ficha(nome: str, idade: str, peso: float, altura: float) -> None:
    calcular = cal_imc(peso, altura)
    classificar, alerta = classificar_imc(calcular)
    linha = "=" * 36
    sep   = "-" * 36

    print("linha")
    print("🏥 CLÍNICA VIDA+ — TRIAGEM")
    print("linha")
    print(f"Paciente: {nome}")
    print(f"Idade   : {idade} anos ")
    print(f"Peso/Alt: {idade}Kg/ {altura}m")
    print("sep")
    print(f"IMC: {calcular}")
    if alerta:
        print(f"Classificação: {classificar} {alerta}")
    else:
        print(f"Classificação: {classificar}")




emitir_ficha("Maria Souza", 34, 70, 1.75)
print()
emitir_ficha("João Pedro", 45, 95, 1.70)