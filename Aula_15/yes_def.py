# desenvolva um sistema de pizzaria onde será recebido o preço do pedido, um desconto de 10%, e ao final exiba o valor total do pedido com esse desconto;

# Declarar uma função def(função)
def calcular_total(nome, preco, desconto=0.10):
    valor_desconto = preco * desconto
    total = preco - valor_desconto
    print(f"""
                💵 Recibo 💵
          Pedido do Cliente: {nome}
          Valor do Pedido: R$ {preco}
          Desconto aplicado: {desconto:.2f}
          Total: R$ {total:.2f}
          """)  #return é opcional

#invocação da def
calcular_total("Gabriel",45.90)
calcular_total("Ana",38.50)
calcular_total("Maria",40.50)
calcular_total("Pedro",54.20)