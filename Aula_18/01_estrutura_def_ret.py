# Parâmetro nomeados = Ao nomear os argumentos, a ordem não importa mais.

def registrar_cliente(nome, telefone, endereco):
    print(f"=== Dados do Cliente ===")
    print(f"Cliente: {nome}")
    print(f"Telefone: {telefone}")
    print(f"Endereço: {endereco}")

#aqui são parametros nomeados
# registrar_cliente(
#     telefone="21099543890",
#     nome="Ana Lima",
#     endereco="Rua das Pizzas, 42"
# )

# ---
# Retorno de Valores - desenpacotamento de retorno(unpacking) - Devolve uma tupla com os returns
def resumo_pedido(itens, desconto=0):
    subtotal = sum(itens)
    valor_desconto = subtotal * (desconto / 100)
    total = subtotal - valor_desconto
    return subtotal, valor_desconto, total # devolve uma tupla (subtotal, valor_desconto, total)

#Invocando e desempacotando a função/return
# print(resumo_pedido([35.0, 12.0, 8.5], desconto=10))
sub, desc, tot = resumo_pedido([35.0, 12.0, 8.5], desconto=10)
print(f"Subtotal: {sub:.2f}")
print(f"Desconto: {desc:.2f}")
print(f"Total: {tot:.2f}")
