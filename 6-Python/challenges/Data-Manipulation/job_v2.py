# Demonstração Prática 4 - Criação de Pipeline de Extração, Limpeza, Transformação e Enriquecimento de Dados
# Versão 2
# Regra de negócio: Carregar somente registros com quantidade produzida superior a 10.

# Imports
import csv
import sqlite3

# Abre o arquivo CSV com os dados da produção de alimentos
with open('producao_alimentos.csv', 'r') as file:
    
    # Cria um leitor de CSV para ler o arquivo
    reader = csv.reader(file)

    # Pula a primeira linha, que contém os cabeçalhos das colunas
    next(reader)

    # Conecta ao banco de dados
    conn = sqlite3.connect('dsadb.db')

    # Deleta a tabela existente, se houver
    conn.execute('DROP TABLE IF EXISTS producao')

    # Cria uma nova tabela para armazenar os dados de produção de alimentos
    conn.execute('''CREATE TABLE producao (
                    produto TEXT,
                    quantidade INTEGER,
                    preco_medio REAL,
                    receita_total REAL
                )''')

    # Insere cada linha do arquivo com quantidade maior que 10 na tabela do banco de dados
    for row in reader:
        if int(row[1]) > 10:
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?, ?, ?, ?)', row)

    conn.commit()
    conn.close()

print("Job Concluído com Sucesso!")
