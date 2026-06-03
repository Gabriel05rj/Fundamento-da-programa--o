# As funções podem ou naço receber propriedades
# def saudacao():
#     print("Seja Bem-vindo(a)!!!")

# saudacao()
# saudacao()
# saudacao()

#calcule o preço total de uma pizza onde será passado um dicionário com os tamanhos e valores. Além disso, o cliente pode solicitar ou nçao  a borda fechada. Ao final, retorne o preço total.
# 1. Pequena, Média ou Grande. Qualquer pizza terá o mesmo valor dependendo do tamanho.
# 2. Se o cliente optar pela borda recheada, deverá ser acrescido no valor da pizza + R$ 8.
def calcular_valor_pizza(tamanho, borda_recheada=False):
    "Calcule o preço final de uma pizza com opções"
    tabela = {"P": 25.0, "M": 35.0, "G": 45.0}
    preco = tabela[tamanho]
    if borda_recheada: #por padrão toda variavel é True
        preco = preco + 8.0
    return preco 

print(calcular_valor_pizza("P"))
print(calcular_valor_pizza("M",True))
print(calcular_valor_pizza("G",True))