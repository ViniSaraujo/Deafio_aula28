from processamento_dados import filtrar_recuperacao, aluno_destaque, gerar_relatorio


alunos_senai = [
    ("Vinicius", [8.5, 9.0, 7.5]),
    ("Pedro", [6.0, 5.5, 4.0]),
    ("Fulana", [5.0, 9.5, 4.0]),
    ("Roberta", [7.0, 9.5, 3.5]),
    ("Maria Aparecida", [9.8, 4.5, 5.5]),
    ("Alice", [4.0, 6.5, 7.0]),
    ("Maria", [10.0, 9.5]),
    ("Ana", []),        
    ("João", [7.0, "erro", 8.0]) 
]


if __name__ == "__main__":
    
    recuperacao = filtrar_recuperacao(alunos_senai)
    
    
    destaque = aluno_destaque(alunos_senai)
    
    
    gerar_relatorio(recuperacao, destaque)
    
    
    print("Processamento finalizado com sucesso!")
    print(f"Alunos em recuperação encontrados: {len(recuperacao)}")
    print("Arquivo 'resultado.txt' criado.")