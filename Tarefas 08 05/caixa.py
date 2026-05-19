quantidade = 0
total = 0

while True:
    produto = float(input("Informe o preço dos produtos, (digite '0' para sair): "))
    if produto == 0:
        break

    total += produto
    quantidade += 1


print(f"\nQuantidade de produtos: {quantidade}")
print(f"O valor da compra foi de R$ {total:.2f} ")
