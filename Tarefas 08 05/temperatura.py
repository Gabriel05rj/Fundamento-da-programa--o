temperaturas = []

for temperatura in range (24):
    temperatura = float(input("Insira o valor das temperaturas diárias: "))
    temperaturas.append(temperatura)

temp_max = max(temperaturas)
temp_min = min(temperaturas)
media = sum(temperaturas) / 24

if media < 15:
    classificacao = "Frio"
elif media < 25:
    classificacao = "Agradável"
else:
    classificacao = "Quente"

# temperaturas acima de 30
acima_30 = 0

for temperatura in temperaturas:
    if temperatura > 30:
        acima_30 += 1

# Relatório Final
print("\n ===== Relatório de Temperaturas diárias =====")
print(f"Temperatura Máxima do dia: {temp_max:.1f} °C")
print(f"Temperatura Mínima do dia: {temp_min:.1f} °C")
print(f"Média de Temperatura diária: {media:.1f} °C")
print(f"Classificação diária: {classificacao:}")
print(f"Horas com Temperatura acima de 30°C: {acima_30:}")
