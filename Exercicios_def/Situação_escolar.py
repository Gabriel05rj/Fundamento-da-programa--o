def verificar_situacao(media, verificar_honra=True):
    if media > 7.0:
        situacao = "Aprovado ✅"
    elif media >= 5.0 and media < 7.0:
        situacao = "Recuperação ⚠️"
    elif media < 5.0:
        situacao = "Reprovado ❌"
    mensagem_honra = ("Menção Honrosa🏅") if verificar_honra == True and media > 9.0 else ""
    return situacao, mensagem_honra 

sit, honra = verificar_situacao(9.5)
print(f"{sit} {honra}")

sit2, honra2 = verificar_situacao(6.6)
print(f"{sit2} {honra2}")

sit3, honra3 = verificar_situacao(4.8)
print(f"{sit3} {honra3}")
