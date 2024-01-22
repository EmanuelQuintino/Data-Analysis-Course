# Demonstração Prática 4 - Criação de Pipeline de Extração, Limpeza, Transformação e Enriquecimento de Dados
# Versão 3
# Regra de negócio: Remover o caracter "ponto" na última coluna do arquivo para evitar que o número seja truncado 

# Imports
import csv
import sqlite3

# Função para remover o ponto nos dados da última coluna
def remove_ponto(valor):
    return int(valor.replace('.', ''))

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
                    receita_total INTEGER
                )''')

    # Insere cada linha do arquivo com quantidade maior que 10 na tabela do banco de dados
    for row in reader:
        if int(row[1]) > 10:
            
            # Remove o ponto do valor da última coluna e converte para inteiro
            row[3] = remove_ponto(row[3])

            # Insere o registro no banco de dados
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?, ?, ?, ?)', row)

    conn.commit()
    conn.close()

print("Job Concluído com Sucesso!")
