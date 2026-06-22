def calcular_media(n1, n2, n3):
    media = ((n1 * 2 + n2 * 3 + n3 * 5) / 10 )
    if media > 10 or media < 0:
        return -1.0
    return media

def verificar_situacao(media, verificar_honra=True):
    if media > 7.0:
        situacao = "Aprovado ✅"
    elif media >= 5.0 and media < 7.0:
        situacao = "Recuperação ⚠️"
    elif media < 5.0:
        situacao = "Reprovado ❌"
    mensagem_honra = ("Menção Honrosa🏅") if verificar_honra == True and media > 9.0 else ""
    return situacao, mensagem_honra 

def emitir_boletim(nome, turma, nota1, nota2, nota3):
    media = calcular_media(nota1, nota2, nota3)
    situacao, honra = verificar_situacao(media)
    return nome, turma, nota1, nota2, nota3, media, situacao, honra

nom, tur, n1, n2, n3, med, sit, honra = emitir_boletim("Maria Custódia","3ºA", 8.0, 7.9, 7.8)
print(f'''========================
          Colégio Byte - Boletim
         ========================
      
      Aluno: {nom}
      Turma: {tur}
      1º Bimestre: {n1}  2º Bimestre: {n2}  3º Bimestre: {n3}
      ---------------------------------------------------------
      Média: {med}
      Situação: {sit} {honra}''')

