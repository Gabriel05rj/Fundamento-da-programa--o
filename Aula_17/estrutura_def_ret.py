#Função que exibe os sabores, tamanhos e valores das pizzas
def exibir_cardapio():
    print("===CARDAPIO PIZZARIA DO CÓDIGO===")
    print("🍕 Marguerita - P: R$25 | M: R$35 | G: R$45🍕")
    print("🍕 Calabresa - P: R$28 | M: R$38 | G: R$48🍕")
    print("🍕 Frango - P: R$30 | M: R$40 | G: R$50🍕")

# exibir_cardapio()

# Função para aplicar desconto, onde o preço e o percentual de desconto será passado no momento da invocação da função.
valor_sem_desc = 40

def aplicar_desconto(preco, percentual):
    # preco * (1 - percentual /100)-> outra forma de escrever uma porcentagem 
    return preco * percentual

preco_final = valor_sem_desc - aplicar_desconto(valor_sem_desc, 0.10) #pode passar uma variavel nos parâmetros para puxar um valor, nesse caso seria 40 - 4
# print(f"Preço com desconto:R$ {preco_final:.2f}")

# Declarar função que receberá por padrãp que a borda não é recheada. Além disso, irá receber também o sabor e tamanho da pizza
def fazer_pedido(sabor, tamanho="M", borda_recheada=False):
    borda = "com borda recheada" if borda_recheada else "sem borda"
    #variável = valor se Vdd if condição lógoica eslse valor se falso
    print(f'Pedido: {sabor} | {tamanho} | {borda}')

fazer_pedido("Marguerita")
fazer_pedido( "Calabresa","G" ,True)
fazer_pedido("Frango", "P")