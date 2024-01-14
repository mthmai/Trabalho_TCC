import re
lista= []

with open('colunas_ficam.txt', 'r') as arquivo:
     for linha in arquivo:
        linha = linha.strip()
        numeros = re.findall(r'\d', linha[:3])
        numeros_formatados = ''.join(numeros)
        if numeros_formatados:
            lista.append(int(numeros_formatados))

print(lista)


