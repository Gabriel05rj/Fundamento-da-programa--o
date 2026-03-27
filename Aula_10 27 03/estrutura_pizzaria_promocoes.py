# variaveis da pizzaria
FRETE = 2 #constantr fake
pizza_sabor = input("Digite o sabor da pizza: [frango com requeijao], [calabresa], [portuguesa], [marguerita]: ")
pizza_tamanho = input("Digite o tamanho da pizza: [pequena], [média], [grande]: ")
dia_semana = input("Digite o dia da semana: [quarta-feira], [quinta-feira], [sexta-feira], [sábado], [domingo]: ")
 
print(f" o sabor escolhido da pizza é {pizza_sabor} o tamanho é {pizza_tamanho} e o dia da semana é {dia_semana}")
#promoções -> estruturas condicionais 

#comprar pizza de qualquer tamanho no sabado o refri é grátis.
if dia_semana == "sabado":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O Refri hoje é por conta da casa!")
elif dia_semana == "domingo"
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O Frete e o Refri hoje é por conta da casa!")
elif pizza_sabor == "calabresa" and pizza_tamanho == "média":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O Frete hoje é por conta da casa!") 

#comprar uma pizza de calabresa no tamanho medio pra cima em qualquer dia, o frete é grátis
#Comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri é grátis


