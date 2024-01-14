#!/bin/bash

# Pasta com os arquivos comprimidos .gz
pasta="$HOME/Trabalho_TCC/dbNSFP4.2a"
start=$(date +%s)

# Loop para descomprimir, cortar e excluir os arquivos
for arquivo_comprimido in "$pasta"/*.gz; do
    echo "Arquivo comprimido: $arquivo_comprimido"
    
    # Descomprimir o arquivo
    gzip -d "$arquivo_comprimido"

    # Nome do arquivo descomprimido (removendo a extensão .gz)
    arquivo_descomprimido="${arquivo_comprimido%.gz}"
    echo "Arquivo descomprimido: $arquivo_descomprimido"

    # Fazer o corte no arquivo descomprimido
    cut -f 1,2,3,4,5,6,7,8,9,12,13,19,20,24,39,42,45,48,51,55,60,63,66,67,71,74,78,81,82,84,89,91,95,98,101,104,107,110,119,122,123,127,131,134,137,138,140,142,143,145,146,148,149,151,152,155,175,177,179,181,183,185,244,247,251,255,259,263,267,271,275,630,631,632,635 "$arquivo_descomprimido" > "${arquivo_descomprimido}_cortado.csv"
    
    echo "Arquivo cortado: ${arquivo_descomprimido}_cortado.csv"

    # Excluir o arquivo descomprimido
    rm "$arquivo_descomprimido"
    
    echo "Arquivo descomprimido excluído."
done
# Parar cronômetro e calcular o tempo total
end=$(date +%s)
runtime=$((end-start))

echo "Tempo total de execução: $runtime segundos."
