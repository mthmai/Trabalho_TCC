from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField, DecimalField

db = SqliteDatabase('db_teste.db')


class BaseModel(Model):
    class Meta:
        database = db

class Gene(BaseModel):
    chr = IntegerField()
    gene_name = CharField(max_length=12)

class Alteracao(BaseModel):
    gene_name = ForeignKeyField(Gene)
    HGVSc_ANNOVAR = CharField(max_length=30)
    HGVSp_ANNOVAR = CharField(max_length=30)
    HGVSp_VEP = CharField(max_length=30)

class Classificacao(BaseModel):
    alteracao = ForeignKeyField(Alteracao)
    SIFT_pred = DecimalField(max_digits=8)
    SIFT4G_pred = DecimalField(max_digits=8)
    Polyphen2_HDIV_pred = DecimalField(max_digits=8)
    Polyphen2_HVAR_pred = DecimalField(max_digits=8)
    LRT_pred = DecimalField(max_digits=8)
    MutationTaster_pred = DecimalField(max_digits=8)
    MutationAssessor_pred = DecimalField(max_digits=8)
    FATHMM_pred = DecimalField(max_digits=8)
    PROVEAN_pred = DecimalField(max_digits=8)
    VEST4_score = DecimalField(max_digits=8)
    MetaSVM_pred = DecimalField(max_digits=8)
    MetaLR_pred = DecimalField(max_digits=8)
    MetaRNN_pred = DecimalField(max_digits=8)
    MCAP_pred = DecimalField(max_digits=8)
    REVEL_score = DecimalField(max_digits=8)
    MutPred_score = DecimalField(max_digits=8)
    MVP_score = DecimalField(max_digits=8)
    MPC_score = DecimalField(max_digits=8)
    PrimateAI_pred = DecimalField(max_digits=8)
    DEOGEN2_pred = DecimalField(max_digits=8)
    BayesDel_addAF_pred = DecimalField(max_digits=8)
    BayesDel_noAF_pred = DecimalField(max_digits=8)
    ClinPred_pred = DecimalField(max_digits=8)
    LISTS2_pred = DecimalField(max_digits=8)
    CADD_phred = DecimalField(max_digits=8)
    CADD_phred_hg19 = DecimalField(max_digits=8)
    DANN_score = DecimalField(max_digits=8)
    fathmmMKL_coding_pred = DecimalField(max_digits=8)
    fathmmXF_coding_pred = DecimalField(max_digits=8)
    Eigenphred_coding = DecimalField(max_digits=8)
    EigenPCphred_coding = DecimalField(max_digits=8)
    GenoCanyon_score = DecimalField(max_digits=8)
    integrated_fitCons_score = DecimalField(max_digits=8)
    GM12878_fitCons_score = DecimalField(max_digits=8)
    H1hESC_fitCons_score =DecimalField(max_digits=8)
    HUVEC_fitCons_score = DecimalField(max_digits=8)
    LINSIGHT = DecimalField(max_digits=8)
    GERP_RS = DecimalField(max_digits=8)
    clinvar_clnsig = DecimalField(max_digits=8)



if __name__ == '__main__':
    import csv

    db.connect()
    db.create_tables([Gene, Alteracao, Classificacao])
    # Leia o arquivo CSV e insira os dados no banco de dados
    csv_file = '/home/matheus_mai/Trabalho_TCC/teste_database.csv'

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