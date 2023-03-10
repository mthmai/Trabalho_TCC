import numpy as np
import pandas
import pandas as pd
from pathlib import Path
import os
from sklearn.metrics import cohen_kappa_score
import time

tempo_inicial = time.time()


#le a tabela (MODIFICAR A ENTRADA)
list_pastas= ['ABCD1', 'AR', 'ATP7A', 'ATRX', 'CDKL5', 'COL4A5', 'DMD', 'F8', 'F9', 'FLNA', 'GJB1', 'GLA', 'HNRNPH2', 'IDS', 'MECP2', 'OTC', 'PCDH19', 'PHEX', 'RS1']

for w in list_pastas:
    tabela= pd.read_csv((f'/home/matheus_mai/Desktop/dbNSFP4.2a/dbNSFP4.2a_complete/chrX_genes/{w}/{w}_limpa_final.csv'), sep= ",")

# modificando os types
    tabela.loc[tabela['MutPred_score'] == '-', 'MutPred_score'] = 1000
    tabela['VEST4_score'] = tabela['VEST4_score'].astype('float64')
    tabela['REVEL_score'] = tabela['REVEL_score'].astype('float64')
    tabela['MutPred_score'] = tabela['MutPred_score'].astype('float64')
    tabela['MVP_score'] = tabela['MVP_score'].astype('float64')
    tabela['MPC_score'] = tabela['MPC_score'].astype('float64')
    tabela['CADD_phred'] = tabela['CADD_phred'].astype('float64')
    tabela['CADD_phred_hg19'] = tabela['CADD_phred_hg19'].astype('float64')
    tabela['DANN_score'] = tabela['DANN_score'].astype('float64')
    tabela['Eigen-phred_coding'] = tabela['Eigen-phred_coding'].astype('float64')
    tabela['Eigen-PC-phred_coding'] = tabela['Eigen-PC-phred_coding'].astype('float64')
    tabela['GenoCanyon_score'] = tabela['GenoCanyon_score'].astype('float64')
    tabela['integrated_fitCons_score'] = tabela['integrated_fitCons_score'].astype('float64')
    tabela['integrated_confidence_value'] = tabela['integrated_confidence_value'].astype('float64')
    tabela['GM12878_fitCons_score'] = tabela['GM12878_fitCons_score'].astype('float64')
    tabela['GM12878_confidence_value'] = tabela['GM12878_confidence_value'].astype('float64')
    tabela['H1-hESC_fitCons_score'] = tabela['H1-hESC_fitCons_score'].astype('float64')
    tabela['H1-hESC_confidence_value'] = tabela['H1-hESC_confidence_value'].astype('float64')
    tabela['HUVEC_fitCons_score'] = tabela['HUVEC_fitCons_score'].astype('float64')
    tabela['HUVEC_confidence_value'] = tabela['HUVEC_confidence_value'].astype('float64')
    tabela['LINSIGHT'] = tabela['LINSIGHT'].astype('float64')
    tabela['GERP++_RS'] = tabela['GERP++_RS'].astype('float64')

# MODIFICANDO OS SCORES PARA 0 E 1
# SIFT_pred
    tabela.loc[tabela['SIFT_pred'] == 'D', 'SIFT_pred'] = 1
    tabela.loc[tabela['SIFT_pred'] == 'T', 'SIFT_pred'] = 0

# SIFT4G_pred
    tabela.loc[tabela['SIFT4G_pred'] == 'D', 'SIFT4G_pred'] = 1
    tabela.loc[tabela['SIFT4G_pred'] == 'T', 'SIFT4G_pred'] = 0

# Polyphen2_HDIV_pred
    tabela.loc[tabela['Polyphen2_HDIV_pred'] == 'D', 'Polyphen2_HDIV_pred'] = 1
    tabela.loc[tabela['Polyphen2_HDIV_pred'] == 'P', 'Polyphen2_HDIV_pred'] = 1
    tabela.loc[tabela['Polyphen2_HDIV_pred'] == 'B', 'Polyphen2_HDIV_pred'] = 0

# Polyphen2_HVAR_pred
    tabela.loc[tabela['Polyphen2_HVAR_pred'] == 'D', 'Polyphen2_HVAR_pred'] = 1
    tabela.loc[tabela['Polyphen2_HVAR_pred'] == 'P', 'Polyphen2_HVAR_pred'] = 1
    tabela.loc[tabela['Polyphen2_HVAR_pred'] == 'B', 'Polyphen2_HVAR_pred'] = 0

#  LRT_pred
    tabela.loc[tabela['LRT_pred'] == 'D', 'LRT_pred'] = 1
    tabela.loc[tabela['LRT_pred'] == 'N', 'LRT_pred'] = 0
    tabela.loc[tabela['LRT_pred'] == 'U', 'LRT_pred'] = 1000

# MutationTaster_pred
    tabela.loc[tabela['MutationTaster_pred'] == 'A', 'MutationTaster_pred'] = 1
    tabela.loc[tabela['MutationTaster_pred'] == 'D', 'MutationTaster_pred'] = 1
    tabela.loc[tabela['MutationTaster_pred'] == 'N', 'MutationTaster_pred'] = 0
    tabela.loc[tabela['MutationTaster_pred'] == 'P', 'MutationTaster_pred'] = 0

# MutationAssessor_pred
    tabela.loc[tabela['MutationAssessor_pred'] == 'H', 'MutationAssessor_pred'] = 1
    tabela.loc[tabela['MutationAssessor_pred'] == 'M', 'MutationAssessor_pred'] = 1
    tabela.loc[tabela['MutationAssessor_pred'] == 'L', 'MutationAssessor_pred'] = 0
    tabela.loc[tabela['MutationAssessor_pred'] == 'N', 'MutationAssessor_pred'] = 0

# FATHMM_pred
    tabela.loc[tabela['FATHMM_pred'] == 'D', 'FATHMM_pred'] = 1
    tabela.loc[tabela['FATHMM_pred'] == 'T', 'FATHMM_pred'] = 0

#PROVEAN_pred
    tabela.loc[tabela['PROVEAN_pred'] == 'D', 'PROVEAN_pred'] = 1
    tabela.loc[tabela['PROVEAN_pred'] == 'N', 'PROVEAN_pred'] = 0

# VEST4_score
    tabela.loc[tabela['VEST4_score'] > 0.5, 'VEST4_score'] = 1
    tabela.loc[tabela['VEST4_score'] <= 0.5, 'VEST4_score'] = 0

# MetaSVM_pred
    tabela.loc[tabela['MetaSVM_pred'] == 'D', 'MetaSVM_pred'] = 1
    tabela.loc[tabela['MetaSVM_pred'] == 'T', 'MetaSVM_pred'] = 0

# MetaLR_pred
    tabela.loc[tabela['MetaLR_pred'] == 'D', 'MetaLR_pred'] = 1
    tabela.loc[tabela['MetaLR_pred'] == 'T', 'MetaLR_pred'] = 0

# MetaRNN_pred
    tabela.loc[tabela['MetaRNN_pred'] == 'D', 'MetaRNN_pred'] = 1
    tabela.loc[tabela['MetaRNN_pred'] == 'T', 'MetaRNN_pred'] = 0

# M-CAP_pred
    tabela.loc[tabela['M-CAP_pred'] == 'D', 'M-CAP_pred'] = 1
    tabela.loc[tabela['M-CAP_pred'] == 'T', 'M-CAP_pred'] = 0

# REVEL_score
    tabela.loc[tabela['REVEL_score'] > 0.5, 'REVEL_score'] = 1
    tabela.loc[tabela['REVEL_score'] <= 0.5, 'REVEL_score'] = 0

# MutPred_score
    tabela.loc[tabela['MutPred_score'] > 0.5, 'MutPred_score'] = 1
    tabela.loc[tabela['MutPred_score'] <= 0.5, 'MutPred_score'] = 0

# MVP_score
    tabela.loc[tabela['MVP_score'] > 0.5, 'MVP_score'] = 1
    tabela.loc[tabela['MVP_score'] <= 0.5, 'MVP_score'] = 0

# MPC_score
    tabela.loc[tabela['MPC_score'] > 2.5, 'MPC_score'] = 1
    tabela.loc[tabela['MPC_score'] <= 2.5, 'MPC_score'] = 0

# PrimateAI_pred
    tabela.loc[tabela['PrimateAI_pred'] == 'D', 'PrimateAI_pred'] = 1
    tabela.loc[tabela['PrimateAI_pred'] == 'T', 'PrimateAI_pred'] = 0

# DEOGEN2_pred
    tabela.loc[tabela['DEOGEN2_pred'] == 'D', 'DEOGEN2_pred'] = 1
    tabela.loc[tabela['DEOGEN2_pred'] == 'T', 'DEOGEN2_pred'] = 0

# BayesDel_addAF_pred
    tabela.loc[tabela['BayesDel_addAF_pred'] == 'D', 'BayesDel_addAF_pred'] = 1
    tabela.loc[tabela['BayesDel_addAF_pred'] == 'T', 'BayesDel_addAF_pred'] = 0

# BayesDel_noAF_pred
    tabela.loc[tabela['BayesDel_noAF_pred'] == 'D', 'BayesDel_noAF_pred'] = 1
    tabela.loc[tabela['BayesDel_noAF_pred'] == 'T', 'BayesDel_noAF_pred'] = 0

# ClinPred_pred
    tabela.loc[tabela['ClinPred_pred'] == 'D', 'ClinPred_pred'] = 1
    tabela.loc[tabela['ClinPred_pred'] == 'T', 'ClinPred_pred'] = 0

# LIST-S2_pred
    tabela.loc[tabela['LIST-S2_pred'] == 'D', 'LIST-S2_pred'] = 1
    tabela.loc[tabela['LIST-S2_pred'] == 'T', 'LIST-S2_pred'] = 0

# CADD_phred (ainda não sei o score direito)
    tabela.loc[tabela['CADD_phred'] > 20, 'CADD_phred'] = 1
    tabela.loc[tabela['CADD_phred'] < 20, 'CADD_phred'] = 0

# CADD_phred_hg19 (ainda não sei o score direito)
    tabela.loc[tabela['CADD_phred_hg19'] > 20, 'CADD_phred_hg19'] = 1
    tabela.loc[tabela['CADD_phred_hg19'] < 20, 'CADD_phred_hg19'] = 0

# DANN_score
    tabela.loc[tabela['DANN_score'] > 0.5, 'DANN_score'] = 1
    tabela.loc[tabela['DANN_score'] <= 0.5, 'DANN_score'] = 0

# fathmm-MKL_coding_pred
    tabela.loc[tabela['fathmm-MKL_coding_pred'] == 'D', 'fathmm-MKL_coding_pred'] = 1
    tabela.loc[tabela['fathmm-MKL_coding_pred'] == 'N', 'fathmm-MKL_coding_pred'] = 0

# fathmm-XF_coding_pred
    tabela.loc[tabela['fathmm-XF_coding_pred'] == 'D', 'fathmm-XF_coding_pred'] = 1
    tabela.loc[tabela['fathmm-XF_coding_pred'] == 'N', 'fathmm-XF_coding_pred'] = 0

# Eigen-phred_coding (nao sei o score direito)
    tabela.loc[tabela['Eigen-phred_coding'] > 0.5, 'Eigen-phred_coding'] = 1
    tabela.loc[tabela['Eigen-phred_coding'] <= 0.5, 'Eigen-phred_coding'] = 0

# Eigen-PC-phred_coding (nao sei o score direito)
    tabela.loc[tabela['Eigen-PC-phred_coding'] > 0.5, 'Eigen-PC-phred_coding'] = 1
    tabela.loc[tabela['Eigen-PC-phred_coding'] <= 0.5, 'Eigen-PC-phred_coding'] = 0

# GenoCanyon_score (não sei o score direito)
    tabela.loc[tabela['GenoCanyon_score'] > 0.5, 'GenoCanyon_score'] = 1
    tabela.loc[tabela['GenoCanyon_score'] <= 0.5, 'GenoCanyon_score'] = 0

# integrated_fitCons_score (nao sei o score direito)
    tabela.loc[tabela['integrated_fitCons_score'] > 0.5, 'integrated_fitCons_score'] = 1
    tabela.loc[tabela['integrated_fitCons_score'] <= 0.5, 'integrated_fitCons_score'] = 0

# integrated_confidence_value (nao sei o score direito)


# GM12878_fitCons_score (nao sei o score direito)
    tabela.loc[tabela['GM12878_fitCons_score'] > 0.5, 'GM12878_fitCons_score'] = 1
    tabela.loc[tabela['GM12878_fitCons_score'] <= 0.5, 'GM12878_fitCons_score'] = 0

# GM12878_confidence_value (nao sei o score direito)


# H1-hESC_fitCons_score (nao sei o score direito)
    tabela.loc[tabela['H1-hESC_fitCons_score'] > 0.5, 'H1-hESC_fitCons_score'] = 1
    tabela.loc[tabela['H1-hESC_fitCons_score'] <= 0.5, 'H1-hESC_fitCons_score'] = 0

# H1-hESC_confidence_value (nao sei o score direito)


# HUVEC_fitCons_score
    tabela.loc[tabela['HUVEC_fitCons_score'] > 0.5, 'HUVEC_fitCons_score'] = 1
    tabela.loc[tabela['HUVEC_fitCons_score'] <= 0.5, 'HUVEC_fitCons_score'] = 0

# HUVEC_confidence_value (nao sei o score direito)


# LINSIGHT (nao sei o score direito)
    tabela.loc[tabela['LINSIGHT'] > 0.5, 'LINSIGHT'] = 1
    tabela.loc[tabela['LINSIGHT'] <= 0.5, 'LINSIGHT'] = 0

# GERP++_RS (nao sei o score direito)
    tabela.loc[tabela['GERP++_RS'] > -6.13, 'GERP++_RS'] = 1
    tabela.loc[tabela['GERP++_RS'] <= 6.13, 'GERP++_RS'] = 0

# clinvar_clnsig
    tabela.loc[tabela['clinvar_clnsig'] == 'drug_response', 'clinvar_clnsig'] = 1
    tabela.loc[tabela['clinvar_clnsig'] == 'Pathogenic', 'clinvar_clnsig'] = 1
    tabela.loc[tabela['clinvar_clnsig'] == 'Likely_pathogenic', 'clinvar_clnsig'] = 1
    tabela.loc[tabela['clinvar_clnsig'] == 'Pathogenic/Likely_pathogenic', 'clinvar_clnsig'] = 1
    tabela.loc[tabela['clinvar_clnsig'] == 'Likely_benign', 'clinvar_clnsig'] = 0
    tabela.loc[tabela['clinvar_clnsig'] == 'Benign', 'clinvar_clnsig'] = 0
    tabela.loc[tabela['clinvar_clnsig'] == 'Benign/Likely_benign', 'clinvar_clnsig'] = 0
    tabela.loc[tabela['clinvar_clnsig'] == 'Uncertain_significance', 'clinvar_clnsig'] = 1000
    tabela.loc[tabela['clinvar_clnsig'] == 'Conflicting_interpretations_of_pathogenicity', 'clinvar_clnsig'] = 1000
    tabela.loc[tabela['clinvar_clnsig'] == 'not_provided', 'clinvar_clnsig'] = 1000
    tabela.loc[tabela['clinvar_clnsig'] == 'risk_factor', 'clinvar_clnsig'] = 1
    tabela.loc[tabela['clinvar_clnsig'] == 'protective', 'clinvar_clnsig'] = 0
    tabela.loc[tabela['clinvar_clnsig'] == 'Conflicting_interpretations_of_pathogenicity,_other,_risk_factor', 'clinvar_clnsig'] = 1000
    tabela.loc[tabela['clinvar_clnsig'] == 'Conflicting_interpretations_of_pathogenicity,_risk_factor', 'clinvar_clnsig'] = 1000
    tabela.loc[tabela['clinvar_clnsig'] == 'Pathogenic/Likely_pathogenic,_other', 'clinvar_clnsig'] = 1
    tabela.loc[tabela['clinvar_clnsig'] == 'Pathogenic,_other', 'clinvar_clnsig'] = 1
    tabela.loc[tabela['clinvar_clnsig'] == 'Pathogenic,_risk_factor', 'clinvar_clnsig'] = 1
    tabela.loc[tabela['clinvar_clnsig'] == 'Benign/Likely_benign,_risk_factor', 'clinvar_clnsig'] = 1000
    tabela.loc[tabela['clinvar_clnsig'] == 'Benign/Likely_benign,_other'] = 0
    tabela.loc[tabela['clinvar_clnsig'] == 'Conflicting_interpretations_of_pathogenicity,_other'] = 1000
    tabela.loc[tabela['clinvar_clnsig'] == 'Uncertain_significance,_other'] = 1000
    tabela.loc[tabela['clinvar_clnsig'] == 'other'] = 1000
    tabela.loc[tabela['clinvar_clnsig'] == 'Pathogenic,_drug_response,_other'] = 1
    tabela.loc[tabela['clinvar_clnsig'] == 'Pathogenic/Likely_pathogenic,_drug_response'] = 1
    tabela.loc[tabela['clinvar_clnsig'] == 'Pathogenic,_drug_response'] = 1
    tabela.loc[tabela['clinvar_clnsig'] == 'Pathogenic,_Affects'] = 1
    tabela.loc[tabela['clinvar_clnsig'] == 'Affects'] = 1
    tabela.loc[tabela['clinvar_clnsig'] == 'Likely_pathogenic,_other'] = 1000
    tabela.loc[tabela['clinvar_clnsig'] == 'Benign,_other'] = 1000
    tabela.loc[tabela['clinvar_clnsig'] == 'Likely_pathogenic,_drug_response'] = 1
    tabela.loc[tabela['clinvar_clnsig'] == 'Uncertain_significance,_drug_response'] = 1000
    tabela.loc[tabela['clinvar_clnsig'] == 'association'] = 1000
    tabela.loc[tabela['clinvar_clnsig'] == 'Conflicting_interpretations_of_pathogenicity,_drug_response'] = 1000

    valores = []
    tabela_drop = tabela[tabela['clinvar_clnsig'] == 1000].index
    tabela.drop(tabela_drop, inplace=True)

    lista_kappa = list()
    #print(tabela.columns[14:55])
    for j in tabela.columns[14:55]:
        df_corte = tabela.loc[:, [j, 'clinvar_clnsig']]
        teste_drop = df_corte[df_corte[j] == '1000'].index
        df_corte.drop(teste_drop, inplace=True)
        cortado = df_corte[j].tolist()
        #print(cortado)
        print(w)
        clinvar_corte = df_corte['clinvar_clnsig'].tolist()
        print(clinvar_corte)
        kappa_list = cohen_kappa_score(cortado, clinvar_corte)
        lista_kappa.append((kappa_list))

# laço para valores de TP, FN, FP e TN
    for i in tabela.columns[14:55]:
        search_TP = (tabela[(tabela['clinvar_clnsig'] == 1) & (tabela[i] == 1)])
        TP = len(search_TP.index)
        search_FN = (tabela[(tabela['clinvar_clnsig'] == 1) & (tabela[i] == 0)])
        FN = len(search_FN.index)
        search_PAT_nao_class = (tabela[(tabela['clinvar_clnsig'] == 1) & (tabela[i] == 1000)])
        pat_nao_class = len(search_PAT_nao_class.index)

        search_FP = (tabela[(tabela['clinvar_clnsig'] == 0) & (tabela[i] == 1)])
        FP = len(search_FP.index)
        search_TN = (tabela[(tabela['clinvar_clnsig'] == 0) & (tabela[i] == 0)])
        TN = len(search_TN)
        search_BEN_nao_class = (tabela[(tabela['clinvar_clnsig'] == 0) & (tabela[i] == 1000)])
        ben_nao_class = len(search_BEN_nao_class)
        valores.append([TP, FN, FP, TN])

    sensibilidades = []
    especificidades = []
    acuracias = []

    for i in range(len(valores)):

    # sensibilidade/True Positive Rate (TPR)
    # TP/(TP+FN)
        if (valores[i][1] + valores[i][0]) != 0:
            sensibilidade = (valores[i][0]) / (valores[i][1] + valores[i][0])
        else:
            sensibilidade = 'Divisão por zero'
        sensibilidades.append(sensibilidade)

    # especificidade/True Negative Rate (TNR)
    # TN/(TN+FP)
        if (valores[i][3] + valores[i][2]) != 0:  # testa se a divisão é diferente de 0
            especificidade = valores[i][3] / (valores[i][3] + valores[i][2])
        else:
            especificidade = "Divisão por zero"
        especificidades.append(especificidade)

    # acuracia
    # (TP+TN)/(TP+TN+FN+FP)
        if (valores[i][0] + valores[i][1] + valores[i][2] + valores[i][3]) != 0:  # testa se a divisão é diferente de 0
            acuracia = (valores[i][0] + valores[i][3]) / (valores[i][0] + valores[i][1] + valores[i][2] + valores[i][3])
        else:
            acuracia = "Divisão por zero"
        acuracias.append(acuracia)

    lista_programas = tabela.columns[14:55].tolist()


# cria uma tabela as estatisticas de todos os preditores
    tabela_final = pd.DataFrame(
            data=zip(lista_programas, sensibilidades, especificidades, acuracias, lista_kappa),
            columns=['Programs', 'Sensitivity', 'Specificity', 'Accuracy', 'Kappa_Value']
    )
    tabela_final.to_csv((f'/home/matheus_mai/Desktop/dbNSFP4.2a/dbNSFP4.2a_complete/chrX_genes/{w}/{w}_estatisticas.csv'), index= False)

tempo_final= time.time()

print(f'O código demorou {tempo_final - tempo_inicial} segundos pra executar')
