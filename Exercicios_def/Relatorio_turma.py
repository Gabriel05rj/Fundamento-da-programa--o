
def cal_media_turmas (medias: list) -> list:
    if not medias:
        return 0.0
    return round(sum(medias) / len(medias), 1)

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
  
def contar_situacoes (medias: list) -> tuple:
    aprov = rec = repro = 0
    for m in medias:
        sit = verificar_situacao(m, False)
        if "aprovados" in sit:
            aprov += 1
        elif "recuperação" in sit:
            rec += 1
        elif "reprovados" in sit:
            repro += 1
    return aprov, rec, repro 

def relatorio_turma (nome_turma: str, medias: list) -> None:
    titulo = f"║   📊 RELATÓRIO DA TURMA — {nome_turma}   ║"
    linha = "=" * 36
    sep   = "-" * 36

    print(linha)
    print(titulo)
    print(linha)

    if not medias:
        print("Nenhum aluno avaliado ainda")
    else:
        media_g = cal_media_turmas(medias)
        aprov, rec, repro = contar_situacoes(medias)
        print(f" Alunos avaliados: {len(medias)}")
        print(f" Média da Turma: {media_g}")
        print(f" Maior média : {max(medias)}")
        print(f" Menor média: {min(medias)}")
        print("---------------------------------")
        print(f" Aprovados: {aprov}")
        print(f" Recuperação: {rec}")
        print(f" Reprovados: {repro}")

