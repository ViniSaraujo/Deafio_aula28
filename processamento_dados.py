def calcular_media(notas):
    
    notas_validas = []
    for n in notas:
        if isinstance(n, (int, float)):
            notas_validas.append(n)
    
    
    if not notas_validas:
        return 0.0
    
    
    return sum(notas_validas) / len(notas_validas)

def filtrar_recuperacao(lista_alunos):
    alunos_recuperacao = []
    for nome, notas in lista_alunos:
        media = calcular_media(notas)
        if media < 7.0:
            alunos_recuperacao.append((nome, media))
    return alunos_recuperacao
    
def gerar_relatorio(recuperacao, destaque, nome_arquivo="resultado.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("--- RELATÓRIO ACADÊMICO SENAI ---\n\n")
        
        
        if destaque:
            nome_top, media_top = destaque
            arquivo.write(f"DESTAQUE: {nome_top} com média {media_top:.1f}\n")
        
        arquivo.write("-" * 30 + "\n")
        arquivo.write("ALUNOS EM RECUPERAÇÃO:\n")
        
        
        if not recuperacao:
            arquivo.write("Nenhum aluno em recuperação.\n")
        else:
            for nome, media in recuperacao:
                arquivo.write(f"- {nome}: {media:.1f}\n")

def aluno_destaque(lista_alunos):
    melhor_aluno = None
    maior_media = -1.0 
    
    for nome, notas in lista_alunos:
        media = calcular_media(notas)
        if media > maior_media:
            maior_media = media
            melhor_aluno = (nome, media)
            
    return melhor_aluno