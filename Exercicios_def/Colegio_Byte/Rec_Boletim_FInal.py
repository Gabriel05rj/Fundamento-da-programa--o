def cal_media (n1: float, n2: float, n3: float):
    media = round( (n1 + n2 + n3) / 3, 1)
    return (media)

def verificar_situacao(media: float, mostrar: bool = True):
    if media >= 7:
        situacao = "Aprovado"
        honra = "🏆 Honra ao Mérito" if media >= 9 else ""
    elif media >= 5:
        situacao = "Recuperação"
        honra = ""
    else:
        situacao = "Reprovado"
        honra = ""

    if mostrar:
        print(situacao)

    return situacao, honra

def precisa_recuperacao(media):
    if media >= 5 and media < 7:
        print("em recuperação")

def cal_media_final(situacao: str, media: float, nota_final: float):
    media_final = sum([media + nota_final])
    if situacao == "Reprovado":
        return round(media_final, 1)

    
def emitir_boletim_final(nome: str, nome_turma: str, n1, n2, n3,media_final) -> None:
    media = cal_media(n1, n2, n3)
    sit, _ = verificar_situacao(media, False)
    em_recup = precisa_recuperacao(media) 
    titulo = f"║   📊 Colégio Byte — Boletim Final   ║"
    linha = "=" * 36
    sep   = "-" * 36

    print(linha)
    print(titulo)
    print(linha)

    print(nome)
    print(nome_turma)
    print(f"1º Bim: {n1}  2º Bim: {n2}  3º Bim: {n3}")

    if em_recup and media_final is not None:
        media_fin    = cal_media_final(media, media_final)
        sit_fin, _   = verificar_situacao(media_fin, False)
        print(f"Média   : {media}   → {sit}")
        print(sep)
        print(f"Prova Final    : {media_final}")
        print(f"Média Final    : {media_fin}")
        print(f"Situação Final : {sit_fin}")
    else:
        sit_fin, honra = verificar_situacao(media)
        print(f"Média   : {media}")
        print(sep)
        print(f"Situação Final : {sit_fin}  {honra}")
    print(linha)

emitir_boletim_final(
    nome="Bruno Ramos",
    nome_turma="3ºA",
    n1=5.0,
    n2=6.0,
    n3=5.5,
    media_final=7.0,
)
print()
# Aluno aprovado direto, sem recuperação

emitir_boletim_final( 
    nome = "Ana Lima",
    nome_turma = "3ºA",
    n1=9.0,
    n2=9.5,
    n3=9.0,
    media_final=7.0,
)

