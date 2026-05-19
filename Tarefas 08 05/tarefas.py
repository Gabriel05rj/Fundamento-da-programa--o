# Calculadora de tarifas elétrica
consumo = int(input("Informe o consumo de energia: "))
print(''' --- Cálculo de Tarifas ---''')

if consumo <= 100:
    fatura01 = consumo * 0.40
    print(f"Seu consumo foi de {consumo} Kw, e a tarifa aplicada foi de 0.40 por Kw/h sua fatura é de R$ {fatura01:.2f}")
elif consumo <= 200:
    consumo_parcial = consumo - 100;
    fatura_parcial = consumo_parcial * 0.60;
    valor_final = (consumo - consumo_parcial) * 0.40
    fatura = valor_final + fatura_parcial
    print(f"Seu consumo foi de {consumo} Kw, e a tarifa aplicada foi de 0.60 por Kw/h e sua fatura é de R$ {fatura:.2f}")
elif consumo > 200:
    consumo_parcial = 100 * 0.40
    fatura_parcial = 100 * 0.60
    valor_final = (consumo - 200) * 0.90
    print(f"Seu consumo foi de {consumo} Kw,0.40 {consumo_parcial}, 0.60 {fatura_parcial} e a tarifa aplicada foi de 0.90 por Kw/h sua fatura é de R$ {valor_final:.2f}.")
elif consumo < 0:
    print("Você é um animal. Não sabe escrever um número positivo, melhore.")