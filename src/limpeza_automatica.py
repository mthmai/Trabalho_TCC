import pandas as pd
import numpy as np


list_pastas= ['RYR2', 'LMNA', 'OBSCN', 'MFN2', 'ACTA1', 'ABCA4', 'CRB1', 'FLG', 'FH', 'MTOR', 'ALPL', 'USH2A', 'CACNA1E']

for w in list_pastas:
#chamada do arquivo, sep é como está separado o arquivo (tabulação ou ',' geralmente"
    tabela= pd.read_csv((f"/home/matheus_mai/Desktop/dbNSFP4.2a/dbNSFP4.2a_complete/chr1_genes/{w}/{w}_final.csv"), sep= ",", low_memory= False)


    tabela= tabela.astype(str)
    colunas= tabela.columns
    print(colunas)
    linhas= len(tabela.index)
    matriz= tabela.to_numpy()

    matrizes= []
    for i in range(0, linhas):
        for j in range(0, 58):
            if matriz[i][j] == '.':
                matriz[i][j]= 1000
            else: matriz[i][j] = matriz[i][j]

    df= pd.DataFrame(matriz)

    df.columns = ['#chr', 'pos(1-based)', 'ref', 'alt', 'aaref', 'aaalt', 'rs_dbSNP',
              'hg19_pos(1-based)', 'aapos', 'genename', 'HGVSc_ANNOVAR',
              'HGVSp_ANNOVAR', 'HGVSp_VEP', 'SIFT_pred', 'SIFT4G_pred',
              'Polyphen2_HDIV_pred', 'Polyphen2_HVAR_pred', 'LRT_pred',
              'MutationTaster_pred', 'MutationAssessor_pred', 'FATHMM_pred', 'PROVEAN_pred',
              'VEST4_score', 'MetaSVM_pred', 'MetaLR_pred', 'MetaRNN_pred',
              'M-CAP_pred', 'REVEL_score', 'MutPred_score', 'MVP_score', 'MPC_score',
              'PrimateAI_pred', 'DEOGEN2_pred', 'BayesDel_addAF_pred',
              'BayesDel_noAF_pred', 'ClinPred_pred', 'LIST-S2_pred', 'CADD_phred',
              'CADD_phred_hg19', 'DANN_score', 'fathmm-MKL_coding_pred',
              'fathmm-XF_coding_pred', 'Eigen-phred_coding', 'Eigen-PC-phred_coding',
              'GenoCanyon_score', 'integrated_fitCons_score',
              'integrated_confidence_value', 'GM12878_fitCons_score',
              'GM12878_confidence_value', 'H1-hESC_fitCons_score',
              'H1-hESC_confidence_value', 'HUVEC_fitCons_score',
              'HUVEC_confidence_value', 'LINSIGHT', 'GERP++_RS',
              'clinvar_id', 'clinvar_clnsig', 'clinvar_trait', 'clinvar_source'
              ]

    df= df.astype(object)
    teste_drop= df[df['clinvar_clnsig'] == 1000].index
    df.drop(teste_drop, inplace=True)
    df= df.astype(object)


    df.to_csv((f'/home/matheus_mai/Desktop/dbNSFP4.2a/dbNSFP4.2a_complete/chr1_genes/{w}/{w}_limpa_final.csv'), index= False)
