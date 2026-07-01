def calcular_imc_diario (lista_imcs: list) -> list:
    media = sum(lista_imcs) / len(lista_imcs)
    if lista_imcs is None:
        return 0.0
    return media

def classificar_imc(imc) -> str:
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc <= 24.9:
        classificacao = "Peso normal ✅ "
    elif imc >= 25.0 and imc < 29.9:
        classificacao = "Sobrepeso ⚠️"
    elif imc >= 30:
        classificacao = "Obesidade ❌"
    return classificacao


def contar_classificacoes(lista_imcs: list) -> tuple:
    abaixo, normal, sobrepeso, obesidade = 0
    for imc in lista_imcs:
        classif, _ = classificar_imc(imc, False)
        if classif == "Abaixo do peso":
            abaixo += 1
        elif "Normal" in classif:
            normal += 1
        elif "Sobrepeso" in classif:
            sobrepeso += 1
        else:
            obesidade += 1
    return abaixo, normal, sobrepeso, obesidade

def relatorio_diario_clinica(nome_unidade: str, list_imcs: list):
    titulo = f"║   📊 RELATÓRIO — TURNO: {nome_unidade.upper()}   ║"
    linha = "=" * 36
    sep   = "-" * 36

    print(linha)
    print(titulo)
    print(linha)

    if not list_imcs:
        print("Nenhum paciente triado ainda.")
    else:
        media_g = calcular_imc_diario(list_imcs)
        abaixo, normal, sobrepeso, obesidade = contar_classificacoes(list_imcs)

        print(f"Pacientes triados: {len(list_imcs)}")
        print(f"IMC médio: {media_g}")
        print(sep)
        print(f"Abaixo do peso: {abaixo}")
        print(f"Normal: {normal}")
        print(f"Sobrepeso: {sobrepeso}")
        print(f"Obesidade: {obesidade}")

imcs_manha = [22.9, 32.9, 19.5, 27.3, 24.0, 35.1, 21.0]
relatorio_diario_clinica("Manhã", imcs_manha)

print()

relatorio_diario_clinica("Tarde", [])

