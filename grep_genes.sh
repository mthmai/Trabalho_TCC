#!/bin/bash

# Pasta com os arquivos gerados
start=$(date +%s)
pasta="/home/matheus_mai/Trabalho_TCC/dbNSFP4.2a"
cd $pasta
mkdir Genes/


# Arquivo contendo os nomes a serem buscados
arquivo_nomes="/home/matheus_mai/Trabalho_TCC/genes_utilizados.csv"

while IFS=$',' read -r chr nome; do
    echo "Procurando por: $nome no arquivo relacionado ao chr $chr"

    # Nome do arquivo relacionado ao valor de "chr"
    arquivo="${pasta}/dbNSFP4.2a_variant.chr${chr}_cortado.csv"

    # Verificar se o arquivo existe
    if [ -f "$arquivo" ]; then
        # Nome da pasta para salvar o arquivo de ocorrências
        pasta_destino="${pasta}/Genes/chr_${chr}"

        # Criar a pasta de destino se ainda não existir
        mkdir -p "$pasta_destino"

        # Remover tudo após o primeiro ' ; ' na coluna 11
        awk -F'\t' '{gsub(/;.*$/, "", $11); if ($11 == "'"$nome"'") print}' "$arquivo" > "${pasta_destino}/${nome}_ocorrencia.csv"

        echo "Busca concluída para o nome: $nome"
    else
        echo "Arquivo não encontrado para o chr $chr"
    fi
done < "$arquivo_nomes"
end=$(date +%s)
runtime=$((end-start))
echo "Processo concluído."
echo "Tempo total de execução: $runtime segundos."
