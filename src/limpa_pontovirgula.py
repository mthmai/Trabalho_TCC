import pandas as pd
import numpy as np
from typing import List
# Colunas
columns = ['chr', 'pos(1-based)', 'ref', 'alt',	'aaref', 'aaalt', 'rs_dbSNP', 'hg19_chr', 'hg19_pos(1-based)', 'aapos', 'genename', 
           'HGVSc_ANNOVAR', 'HGVSp_ANNOVAR', 'HGVSp_VEP', 'SIFT_pred', 'SIFT4G_pred', 'Polyphen2_HDIV_pred', 'Polyphen2_HVAR_pred',	'LRT_pred', 
           'MutationTaster_pred', 'MutationAssessor_pred', 'FATHMM_pred', 'PROVEAN_pred', 'VEST4_score', 'MetaSVM_pred', 'MetaLR_pred', 'MetaRNN_pred', 
           'M-CAP_pred', 'REVEL_score', 'MutPred_score', 'MVP_score', 'MPC_score', 'PrimateAI_pred', 'DEOGEN2_pred', 'BayesDel_addAF_pred', 'BayesDel_noAF_pred',
           'ClinPred_pred', 'LIST-S2_pred', 'CADD_phred', 'CADD_phred_hg19', 'DANN_score', 'fathmm-MKL_coding_pred', 'fathmm-XF_coding_pred', 'Eigen-phred_coding',
           'Eigen-PC-phred_coding', 'GenoCanyon_score', 'integrated_fitCons_score', 'integrated_confidence_value', 'GM12878_fitCons_score', 'GM12878_confidence_value', 
           'H1-hESC_fitCons_score', 'H1-hESC_confidence_value', 'HUVEC_fitCons_score', 'HUVEC_confidence_value', 'LINSIGHT', 'GERP++_RS', '1000Gp3_AF', '1000Gp3_AFR_AF', 
           '1000Gp3_EUR_AF', '1000Gp3_AMR_AF', '1000Gp3_EAS_AF', '1000Gp3_SAS_AF', 'gnomAD_exomes_flag', 'gnomAD_exomes_AF', 'gnomAD_exomes_AFR_AF', 'gnomAD_exomes_AMR_AF', 
           'gnomAD_exomes_ASJ_AF', 'gnomAD_exomes_EAS_AF', 'gnomAD_exomes_FIN_AF', 'gnomAD_exomes_NFE_AF', 'gnomAD_exomes_SAS_AF', 'clinvar_id', 'clinvar_clnsig', 'clinvar_trait', 
           'clinvar_var_source']



#chamada do arquivo, sep é como está separado o arquivo (tabulação ou ',' geralmente"
table= pd.read_csv("/home/matheus_mai/Trabalho_TCC/dbNSFP4.2a/Genes/chr_1/ABCA4_ocorrencias.csv", sep= "\t", low_memory=False)

#table.drop(['Unnamed: 74', 'Unnamed: 75', 'Unnamed: 76', 'Unnamed: 77', 'Unnamed: 78', 'Unnamed: 79', 'Unnamed: 80'], axis=1, inplace=True)
table= table.astype(str)
colunas= table.columns
print(colunas)
linhas= len(table.index)
matriz= table.to_numpy()
print("TYPE:", type(matriz))

def char_search (string):
    c = ';'
    pos = string.find(c)
    return string[:pos]

print(linhas)
for i in range(0,linhas):
    for j in range(0,75):
       if len(matriz[i][j]) != 1 and (matriz[i][j].find(';') != -1):
              matriz[i][j]= char_search(matriz[i][j])
       else:
              matriz[i][j] = matriz[i][j]

df= pd.DataFrame(matriz)

df.columns= ['chr', 'pos(1-based)', 'ref', 'alt',	'aaref', 'aaalt', 'rs_dbSNP', 'hg19_chr', 'hg19_pos(1-based)', 'aapos', 'genename', 
           'HGVSc_ANNOVAR', 'HGVSp_ANNOVAR', 'HGVSp_VEP', 'SIFT_pred', 'SIFT4G_pred', 'Polyphen2_HDIV_pred', 'Polyphen2_HVAR_pred',	'LRT_pred', 
           'MutationTaster_pred', 'MutationAssessor_pred', 'FATHMM_pred', 'PROVEAN_pred', 'VEST4_score', 'MetaSVM_pred', 'MetaLR_pred', 'MetaRNN_pred', 
           'M-CAP_pred', 'REVEL_score', 'MutPred_score', 'MVP_score', 'MPC_score', 'PrimateAI_pred', 'DEOGEN2_pred', 'BayesDel_addAF_pred', 'BayesDel_noAF_pred',
           'ClinPred_pred', 'LIST-S2_pred', 'CADD_phred', 'CADD_phred_hg19', 'DANN_score', 'fathmm-MKL_coding_pred', 'fathmm-XF_coding_pred', 'Eigen-phred_coding',
           'Eigen-PC-phred_coding', 'GenoCanyon_score', 'integrated_fitCons_score', 'integrated_confidence_value', 'GM12878_fitCons_score', 'GM12878_confidence_value', 
           'H1-hESC_fitCons_score', 'H1-hESC_confidence_value', 'HUVEC_fitCons_score', 'HUVEC_confidence_value', 'LINSIGHT', 'GERP++_RS', '1000Gp3_AF', '1000Gp3_AFR_AF', 
           '1000Gp3_EUR_AF', '1000Gp3_AMR_AF', '1000Gp3_EAS_AF', '1000Gp3_SAS_AF', 'gnomAD_exomes_flag', 'gnomAD_exomes_AF', 'gnomAD_exomes_AFR_AF', 'gnomAD_exomes_AMR_AF', 
           'gnomAD_exomes_ASJ_AF', 'gnomAD_exomes_EAS_AF', 'gnomAD_exomes_FIN_AF', 'gnomAD_exomes_NFE_AF', 'gnomAD_exomes_SAS_AF', 'clinvar_id', 'clinvar_clnsig', 'clinvar_trait', 
           'clinvar_var_source']

df= df.astype(object)
df.to_csv('/home/matheus_mai/Desktop/uashduasdhusadsa.csv', index= False)
