import pandas as pd

# Caminho para o arquivo VCF do ClinVar
vcf_file = "/home/matheus_mai/Desktop/Clinvar/clinvar_20221030.vcf"

# Ler o arquivo VCF usando o pandas
vcf_df = pd.read_csv(vcf_file, sep='\t', comment='#', header=None)

# Definir os nomes das colunas
vcf_df.columns = ['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']

# Filtrar apenas as variantes missense
missense_variants = vcf_df[vcf_df['INFO'].str.contains('missense', na=False)]

# Filtrar apenas as variantes patogênicas e benignas
# Filtrar as variantes com a palavra "patogenica" ou "benigna" na coluna "INFO"
pat_ben_variants = missense_variants[missense_variants['INFO'].str.contains('patogenica|benigna', case=False, na=False)]

# Obter os nomes dos genes
gene_info = pat_ben_variants['INFO'].str.extract(r'GENEINFO=(.*?);')

# Contar as mutações por gene
gene_mutation_counts = gene_info[0].value_counts()

# Filtrar os genes com mais de 100 mutações
genes_filtered = gene_mutation_counts[gene_mutation_counts > 100]

# Criar uma tabela com as colunas "gene" e "mutações"
table = pd.DataFrame({'gene': genes_filtered.index, 'mutações': genes_filtered.values})

# Imprimir a tabela
table.to_csv('/home/matheus_mai/Desktop/TABLE_TESTE_CLINVAR.csv', index = False)

