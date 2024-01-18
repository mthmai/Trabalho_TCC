import csv
from create_db import Gene, Alteracao, Classificacao, db

# Leia o arquivo CSV e insira os dados no banco de dados
csv_file = '/home/matheus_mai/Trabalho_TCC/teste_refactoring/Genes_teste_cleanup/chr_1/ABCA4_cleanup.csv'

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Crie ou obtenha o Gene associado
        gene, created = Gene.get_or_create(chr=row['chr'], gene_name=row['genename'])

        # Crie a Alteracao associada
        alteracao = Alteracao.create(gene_name=gene, **row)

        # Crie a Classificacao associada
        classificacao = Classificacao.create(alteracao=alteracao, **row)

# Feche a conexão com o banco de dados
db.close()