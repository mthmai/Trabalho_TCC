import os

def processar_arquivos_cleanup(caminho_base):
    # Percorrer os diretórios de cromossomos
    for cromossomo_dir in os.listdir(caminho_base):
        cromossomo_path = os.path.join(caminho_base, cromossomo_dir)
        if os.path.isdir(cromossomo_path):
            # Percorrer os diretórios de genes dentro de cada cromossomo
            for gene_dir in os.listdir(cromossomo_path):
                gene_path = os.path.join(cromossomo_path, gene_dir)
                if os.path.isdir(gene_path):
                    # Verificar se o arquivo cleanup.csv existe no diretório do gene
                    file_path = os.path.join(gene_path, f"{gene_dir}_cleanup.csv")
                    if os.path.isfile(file_path):
                        # Aplicar o algoritmo ao arquivo cleanup.csv
                        seu_algoritmo(file_path)



if __name__ == '__main__':
    processar_arquivos_cleanup('/home/ubuntu/Área de Trabalho/Genes_teste')