
def calcular_media(n1, n2, n3):
    media = ((n1 * 2 + n2 * 3 + n3 * 5) / 10 )
    if media > 10 or media < 0:
        return -1.0
    return media

med = round(calcular_media(7.6, 8.2, 8.0),1)
print(f"Média: {med}")

med2 = round(calcular_media(5.5, 8.5, 4.9),1)
print(f"Média: {med2}")

inv = round(calcular_media(10.4, 11.0, 9.5),1)
print(f"Média: {inv}")
