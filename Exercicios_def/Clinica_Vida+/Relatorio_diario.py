def calcular_imc_diario (lista_imcs: float) -> list:
    media = sum(lista_imcs) / len(lista_imcs)
    if lista_imcs is None:
        return 0.0
    return media

def contar_classificacoes(lista_imcs) -> tuple:
    if lista_imcs < 18.5:
        classificacao = "Abaixo do peso"
    elif lista_imcs <= 24.9:
        classificacao = "Peso normal ✅ "
    elif lista_imcs >= 25.0 and lista_imcs < 29.9:
        classificacao = "Sobrepeso ⚠️"
    elif lista_imcs >= 30:
        classificacao = "Obesidade ❌"
    return lista_imcs