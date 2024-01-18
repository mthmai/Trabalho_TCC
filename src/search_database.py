from peewee import JOIN

from create_db import Classificacao, Alteracao, Gene, db

if __name__ == '__main__':
    db.connect()
    nome_gene = 'ABCA4'
    hgvsp_vep = 'p.Arg1055Ter'
    # Consulta para buscar todas as Classificacoes associadas ao gene 'OR4F5'
    classificacoes = (
    Classificacao.select().join(Alteracao).join(Gene).where((Gene.gene_name == nome_gene) & (Alteracao.HGVSp_VEP == hgvsp_vep))
    )

    for classificacao in classificacoes:
        print(classificacao.GERP_RS)

    db.close()