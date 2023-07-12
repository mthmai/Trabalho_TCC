import os

import pandas as pd
import numpy as np
from typing import List

# Função que busca um ponto e virgula em meio a uma string e retorna a string até o ponto e virgula (ponto importante de limpeza)
def char_search (string):
    c = ';'
    pos = string.find(c)
    return string[:pos]


# Função que recebe uma table em formato de dataframe e vai limpar a table, removendo os ';'
def semicolon_cleanup(table: pd.DataFrame) -> pd.DataFrame:
     
     table = table.astype(str)
     table_columns = table.columns
     table_lines = len(table.index)
     matrix = table.to_numpy()

     for lines in range (0, table_lines):
       for cols in range(0, len(table.columns)):
            if len(matrix[lines][cols]) != 1 and (matrix[lines][cols].find(';') != -1):
                 matrix[lines][cols] = char_search(matrix[lines][cols])
            
            else:
                 matrix[lines][cols] = matrix[lines][cols]

     df = pd.DataFrame(matrix)
     df.astype(object)

     return df

# Função que recebe uma table em formato de dataframe e vai limpar a table removendo os ' . ' 
def point_cleanup(table: pd.DataFrame) -> pd.DataFrame:
     
     table = table.astype(str)
     table_columns = table.columns
     table_lines = len(table.index)
     matrix = table.to_numpy()

     for lines in range (0, table_lines):
       for cols in range(0, len(table_columns)):
            if matrix[lines][cols] == '.':
                 matrix[lines][cols] = 10000
            
            else:
                 matrix[lines][cols] = matrix[lines][cols]

     df = pd.DataFrame(matrix)
     df.astype(object)

     return df


# Função que recebe uma table em formato de dataframe e vai modar os scores
def modify_scores(table: pd.DataFrame) -> pd.DataFrame:
     
    table.loc[table['MutPred_score'] == '-', 'MutPred_score'] = 1000
    table['VEST4_score'] = table['VEST4_score'].astype('float64')
    table['REVEL_score'] = table['REVEL_score'].astype('float64')
    table['MutPred_score'] = table['MutPred_score'].astype('float64')
    table['MVP_score'] = table['MVP_score'].astype('float64')
    table['MPC_score'] = table['MPC_score'].astype('float64')
    table['CADD_phred'] = table['CADD_phred'].astype('float64')
    table['CADD_phred_hg19'] = table['CADD_phred_hg19'].astype('float64')
    table['DANN_score'] = table['DANN_score'].astype('float64')
    table['Eigen-phred_coding'] = table['Eigen-phred_coding'].astype('float64')
    table['Eigen-PC-phred_coding'] = table['Eigen-PC-phred_coding'].astype('float64')
    table['GenoCanyon_score'] = table['GenoCanyon_score'].astype('float64')
    table['integrated_fitCons_score'] = table['integrated_fitCons_score'].astype('float64')
    table['integrated_confidence_value'] = table['integrated_confidence_value'].astype('float64')
    table['GM12878_fitCons_score'] = table['GM12878_fitCons_score'].astype('float64')
    table['GM12878_confidence_value'] = table['GM12878_confidence_value'].astype('float64')
    table['H1-hESC_fitCons_score'] = table['H1-hESC_fitCons_score'].astype('float64')
    table['H1-hESC_confidence_value'] = table['H1-hESC_confidence_value'].astype('float64')
    table['HUVEC_fitCons_score'] = table['HUVEC_fitCons_score'].astype('float64')
    table['HUVEC_confidence_value'] = table['HUVEC_confidence_value'].astype('float64')
    table['LINSIGHT'] = table['LINSIGHT'].astype('float64')
    table['GERP++_RS'] = table['GERP++_RS'].astype('float64')

# MODIFICANDO OS SCORES PARA 0 E 1
# SIFT_pred
    table.loc[table['SIFT_pred'] == 'D', 'SIFT_pred'] = 1
    table.loc[table['SIFT_pred'] == 'T', 'SIFT_pred'] = 0

# SIFT4G_pred
    table.loc[table['SIFT4G_pred'] == 'D', 'SIFT4G_pred'] = 1
    table.loc[table['SIFT4G_pred'] == 'T', 'SIFT4G_pred'] = 0

# Polyphen2_HDIV_pred
    table.loc[table['Polyphen2_HDIV_pred'] == 'D', 'Polyphen2_HDIV_pred'] = 1
    table.loc[table['Polyphen2_HDIV_pred'] == 'P', 'Polyphen2_HDIV_pred'] = 1
    table.loc[table['Polyphen2_HDIV_pred'] == 'B', 'Polyphen2_HDIV_pred'] = 0

# Polyphen2_HVAR_pred
    table.loc[table['Polyphen2_HVAR_pred'] == 'D', 'Polyphen2_HVAR_pred'] = 1
    table.loc[table['Polyphen2_HVAR_pred'] == 'P', 'Polyphen2_HVAR_pred'] = 1
    table.loc[table['Polyphen2_HVAR_pred'] == 'B', 'Polyphen2_HVAR_pred'] = 0

#  LRT_pred
    table.loc[table['LRT_pred'] == 'D', 'LRT_pred'] = 1
    table.loc[table['LRT_pred'] == 'N', 'LRT_pred'] = 0
    table.loc[table['LRT_pred'] == 'U', 'LRT_pred'] = 1000

# MutationTaster_pred
    table.loc[table['MutationTaster_pred'] == 'A', 'MutationTaster_pred'] = 1
    table.loc[table['MutationTaster_pred'] == 'D', 'MutationTaster_pred'] = 1
    table.loc[table['MutationTaster_pred'] == 'N', 'MutationTaster_pred'] = 0
    table.loc[table['MutationTaster_pred'] == 'P', 'MutationTaster_pred'] = 0

# MutationAssessor_pred
    table.loc[table['MutationAssessor_pred'] == 'H', 'MutationAssessor_pred'] = 1
    table.loc[table['MutationAssessor_pred'] == 'M', 'MutationAssessor_pred'] = 1
    table.loc[table['MutationAssessor_pred'] == 'L', 'MutationAssessor_pred'] = 0
    table.loc[table['MutationAssessor_pred'] == 'N', 'MutationAssessor_pred'] = 0

# FATHMM_pred
    table.loc[table['FATHMM_pred'] == 'D', 'FATHMM_pred'] = 1
    table.loc[table['FATHMM_pred'] == 'T', 'FATHMM_pred'] = 0

#PROVEAN_pred
    table.loc[table['PROVEAN_pred'] == 'D', 'PROVEAN_pred'] = 1
    table.loc[table['PROVEAN_pred'] == 'N', 'PROVEAN_pred'] = 0

# VEST4_score
    table.loc[table['VEST4_score'] > 0.5, 'VEST4_score'] = 1
    table.loc[table['VEST4_score'] <= 0.5, 'VEST4_score'] = 0

# MetaSVM_pred
    table.loc[table['MetaSVM_pred'] == 'D', 'MetaSVM_pred'] = 1
    table.loc[table['MetaSVM_pred'] == 'T', 'MetaSVM_pred'] = 0

# MetaLR_pred
    table.loc[table['MetaLR_pred'] == 'D', 'MetaLR_pred'] = 1
    table.loc[table['MetaLR_pred'] == 'T', 'MetaLR_pred'] = 0

# MetaRNN_pred
    table.loc[table['MetaRNN_pred'] == 'D', 'MetaRNN_pred'] = 1
    table.loc[table['MetaRNN_pred'] == 'T', 'MetaRNN_pred'] = 0

# M-CAP_pred
    table.loc[table['M-CAP_pred'] == 'D', 'M-CAP_pred'] = 1
    table.loc[table['M-CAP_pred'] == 'T', 'M-CAP_pred'] = 0

# REVEL_score
    table.loc[table['REVEL_score'] > 0.5, 'REVEL_score'] = 1
    table.loc[table['REVEL_score'] <= 0.5, 'REVEL_score'] = 0

# MutPred_score
    table.loc[table['MutPred_score'] > 0.5, 'MutPred_score'] = 1
    table.loc[table['MutPred_score'] <= 0.5, 'MutPred_score'] = 0

# MVP_score
    table.loc[table['MVP_score'] > 0.5, 'MVP_score'] = 1
    table.loc[table['MVP_score'] <= 0.5, 'MVP_score'] = 0

# MPC_score
    table.loc[table['MPC_score'] > 2.5, 'MPC_score'] = 1
    table.loc[table['MPC_score'] <= 2.5, 'MPC_score'] = 0

# PrimateAI_pred
    table.loc[table['PrimateAI_pred'] == 'D', 'PrimateAI_pred'] = 1
    table.loc[table['PrimateAI_pred'] == 'T', 'PrimateAI_pred'] = 0

# DEOGEN2_pred
    table.loc[table['DEOGEN2_pred'] == 'D', 'DEOGEN2_pred'] = 1
    table.loc[table['DEOGEN2_pred'] == 'T', 'DEOGEN2_pred'] = 0

# BayesDel_addAF_pred
    table.loc[table['BayesDel_addAF_pred'] == 'D', 'BayesDel_addAF_pred'] = 1
    table.loc[table['BayesDel_addAF_pred'] == 'T', 'BayesDel_addAF_pred'] = 0

# BayesDel_noAF_pred
    table.loc[table['BayesDel_noAF_pred'] == 'D', 'BayesDel_noAF_pred'] = 1
    table.loc[table['BayesDel_noAF_pred'] == 'T', 'BayesDel_noAF_pred'] = 0

# ClinPred_pred
    table.loc[table['ClinPred_pred'] == 'D', 'ClinPred_pred'] = 1
    table.loc[table['ClinPred_pred'] == 'T', 'ClinPred_pred'] = 0

# LIST-S2_pred
    table.loc[table['LIST-S2_pred'] == 'D', 'LIST-S2_pred'] = 1
    table.loc[table['LIST-S2_pred'] == 'T', 'LIST-S2_pred'] = 0

# CADD_phred (ainda não sei o score direito)
    table.loc[table['CADD_phred'] > 20, 'CADD_phred'] = 1
    table.loc[table['CADD_phred'] < 20, 'CADD_phred'] = 0

# CADD_phred_hg19 (ainda não sei o score direito)
    table.loc[table['CADD_phred_hg19'] > 20, 'CADD_phred_hg19'] = 1
    table.loc[table['CADD_phred_hg19'] < 20, 'CADD_phred_hg19'] = 0

# DANN_score
    table.loc[table['DANN_score'] > 0.5, 'DANN_score'] = 1
    table.loc[table['DANN_score'] <= 0.5, 'DANN_score'] = 0

# fathmm-MKL_coding_pred
    table.loc[table['fathmm-MKL_coding_pred'] == 'D', 'fathmm-MKL_coding_pred'] = 1
    table.loc[table['fathmm-MKL_coding_pred'] == 'N', 'fathmm-MKL_coding_pred'] = 0

# fathmm-XF_coding_pred
    table.loc[table['fathmm-XF_coding_pred'] == 'D', 'fathmm-XF_coding_pred'] = 1
    table.loc[table['fathmm-XF_coding_pred'] == 'N', 'fathmm-XF_coding_pred'] = 0

# Eigen-phred_coding (nao sei o score direito)
    table.loc[table['Eigen-phred_coding'] > 0.5, 'Eigen-phred_coding'] = 1
    table.loc[table['Eigen-phred_coding'] <= 0.5, 'Eigen-phred_coding'] = 0

# Eigen-PC-phred_coding (nao sei o score direito)
    table.loc[table['Eigen-PC-phred_coding'] > 0.5, 'Eigen-PC-phred_coding'] = 1
    table.loc[table['Eigen-PC-phred_coding'] <= 0.5, 'Eigen-PC-phred_coding'] = 0

# GenoCanyon_score (não sei o score direito)
    table.loc[table['GenoCanyon_score'] > 0.5, 'GenoCanyon_score'] = 1
    table.loc[table['GenoCanyon_score'] <= 0.5, 'GenoCanyon_score'] = 0

# integrated_fitCons_score (nao sei o score direito)
    table.loc[table['integrated_fitCons_score'] > 0.5, 'integrated_fitCons_score'] = 1
    table.loc[table['integrated_fitCons_score'] <= 0.5, 'integrated_fitCons_score'] = 0

# integrated_confidence_value (nao sei o score direito)


# GM12878_fitCons_score (nao sei o score direito)
    table.loc[table['GM12878_fitCons_score'] > 0.5, 'GM12878_fitCons_score'] = 1
    table.loc[table['GM12878_fitCons_score'] <= 0.5, 'GM12878_fitCons_score'] = 0

# GM12878_confidence_value (nao sei o score direito)


# H1-hESC_fitCons_score (nao sei o score direito)
    table.loc[table['H1-hESC_fitCons_score'] > 0.5, 'H1-hESC_fitCons_score'] = 1
    table.loc[table['H1-hESC_fitCons_score'] <= 0.5, 'H1-hESC_fitCons_score'] = 0

# H1-hESC_confidence_value (nao sei o score direito)


# HUVEC_fitCons_score
    table.loc[table['HUVEC_fitCons_score'] > 0.5, 'HUVEC_fitCons_score'] = 1
    table.loc[table['HUVEC_fitCons_score'] <= 0.5, 'HUVEC_fitCons_score'] = 0

# HUVEC_confidence_value (nao sei o score direito)


# LINSIGHT (nao sei o score direito)
    table.loc[table['LINSIGHT'] > 0.5, 'LINSIGHT'] = 1
    table.loc[table['LINSIGHT'] <= 0.5, 'LINSIGHT'] = 0

# GERP++_RS (nao sei o score direito)
    table.loc[table['GERP++_RS'] > -6.13, 'GERP++_RS'] = 1
    table.loc[table['GERP++_RS'] <= 6.13, 'GERP++_RS'] = 0

# clinvar_clnsig
    table.loc[table['clinvar_clnsig'] == 'drug_response', 'clinvar_clnsig'] = 1
    table.loc[table['clinvar_clnsig'] == 'Pathogenic', 'clinvar_clnsig'] = 1
    table.loc[table['clinvar_clnsig'] == 'Likely_pathogenic', 'clinvar_clnsig'] = 1
    table.loc[table['clinvar_clnsig'] == 'Pathogenic/Likely_pathogenic', 'clinvar_clnsig'] = 1
    table.loc[table['clinvar_clnsig'] == 'Likely_benign', 'clinvar_clnsig'] = 0
    table.loc[table['clinvar_clnsig'] == 'Benign', 'clinvar_clnsig'] = 0
    table.loc[table['clinvar_clnsig'] == 'Benign/Likely_benign', 'clinvar_clnsig'] = 0
    table.loc[table['clinvar_clnsig'] == 'Uncertain_significance', 'clinvar_clnsig'] = 10000
    table.loc[table['clinvar_clnsig'] == 'Conflicting_interpretations_of_pathogenicity', 'clinvar_clnsig'] = 10000
    table.loc[table['clinvar_clnsig'] == 'not_provided', 'clinvar_clnsig'] = 10000
    table.loc[table['clinvar_clnsig'] == 'risk_factor', 'clinvar_clnsig'] = 1
    table.loc[table['clinvar_clnsig'] == 'protective', 'clinvar_clnsig'] = 0
    table.loc[table['clinvar_clnsig'] == 'Conflicting_interpretations_of_pathogenicity,_other,_risk_factor', 'clinvar_clnsig'] = 10000
    table.loc[table['clinvar_clnsig'] == 'Conflicting_interpretations_of_pathogenicity,_risk_factor', 'clinvar_clnsig'] = 10000
    table.loc[table['clinvar_clnsig'] == 'Pathogenic/Likely_pathogenic,_other', 'clinvar_clnsig'] = 1
    table.loc[table['clinvar_clnsig'] == 'Pathogenic,_other', 'clinvar_clnsig'] = 1
    table.loc[table['clinvar_clnsig'] == 'Pathogenic,_risk_factor', 'clinvar_clnsig'] = 1
    table.loc[table['clinvar_clnsig'] == 'Benign/Likely_benign,_risk_factor', 'clinvar_clnsig'] = 10000
    table.loc[table['clinvar_clnsig'] == 'Benign/Likely_benign,_other'] = 0
    table.loc[table['clinvar_clnsig'] == 'Conflicting_interpretations_of_pathogenicity,_other'] = 10000
    table.loc[table['clinvar_clnsig'] == 'Uncertain_significance,_other'] = 10000
    table.loc[table['clinvar_clnsig'] == 'other'] = 10000
    table.loc[table['clinvar_clnsig'] == 'Pathogenic,_drug_response,_other'] = 1
    table.loc[table['clinvar_clnsig'] == 'Pathogenic/Likely_pathogenic,_drug_response'] = 1
    table.loc[table['clinvar_clnsig'] == 'Pathogenic,_drug_response'] = 1
    table.loc[table['clinvar_clnsig'] == 'Pathogenic,_Affects'] = 1
    table.loc[table['clinvar_clnsig'] == 'Affects'] = 1
    table.loc[table['clinvar_clnsig'] == 'Likely_pathogenic,_other'] = 10000
    table.loc[table['clinvar_clnsig'] == 'Benign,_other'] = 10000
    table.loc[table['clinvar_clnsig'] == 'Likely_pathogenic,_drug_response'] = 1
    table.loc[table['clinvar_clnsig'] == 'Uncertain_significance,_drug_response'] = 10000
    table.loc[table['clinvar_clnsig'] == 'association'] = 10000
    table.loc[table['clinvar_clnsig'] == 'Conflicting_interpretations_of_pathogenicity,_drug_response'] = 10000

    return table


# Função que recebe uma table em formato de dataframe e vai limpar a table removendo os valores de clinvar == 10000
def clinvar_null_drop(table: pd.DataFrame) -> pd.DataFrame:
     
     clinvar_null_drop = table[table['clinvar_clnsig'] == 10000].index
     table.drop(clinvar_null_drop, inplace=True)

     return table

# Função que pega os nomes de todos os arquivos dentro dos diretórios de cromossomo
def file_names_directories(path_directory: str) -> List[str]:

    general_directory = os.listdir(path_directory)
    general_directory.sort()
    list_file_names = list()
    unique_list_file_names = list()

    for child_directory in general_directory:
        try: 
            files = os.listdir(f'{path_directory}/{child_directory}')
        
            list_file_names.append(files)

        except NotADirectoryError:
         ...
    
    for list_name in list_file_names:
        unique_list_file_names.extend(list_name)


    return general_directory, unique_list_file_names


def apply_cleanup(path_directory: str)-> None:

    directory, list_file_names = file_names_directories(path_directory)

    for child_directory in range (0, len(directory)):
        
        for name in range (0, len(list_file_names)):
            try:
                # Verifica se o arquivo existe no diretório atual
                caminho_arquivo = os.path.join(directory[child_directory], list_file_names[name])
                try: 
                    table = pd.read_csv(f"{path_directory}/{directory[child_directory]}/{list_file_names[name]}", sep= "\t", low_memory=False)
                    cleanup_semicolon_table = semicolon_cleanup(table)
                    point_cleanup_table = point_cleanup(cleanup_semicolon_table)

                    columns_table = ['chr', 'pos(1-based)', 'ref', 'alt',	'aaref', 'aaalt', 'rs_dbSNP', 'hg19_chr', 'hg19_pos(1-based)', 'aapos', 'genename', 
                            'HGVSc_ANNOVAR', 'HGVSp_ANNOVAR', 'HGVSp_VEP', 'SIFT_pred', 'SIFT4G_pred', 'Polyphen2_HDIV_pred', 'Polyphen2_HVAR_pred',	'LRT_pred', 
                            'MutationTaster_pred', 'MutationAssessor_pred', 'FATHMM_pred', 'PROVEAN_pred', 'VEST4_score', 'MetaSVM_pred', 'MetaLR_pred', 'MetaRNN_pred', 
                            'M-CAP_pred', 'REVEL_score', 'MutPred_score', 'MVP_score', 'MPC_score', 'PrimateAI_pred', 'DEOGEN2_pred', 'BayesDel_addAF_pred', 'BayesDel_noAF_pred',
                            'ClinPred_pred', 'LIST-S2_pred', 'CADD_phred', 'CADD_phred_hg19', 'DANN_score', 'fathmm-MKL_coding_pred', 'fathmm-XF_coding_pred', 'Eigen-phred_coding',
                            'Eigen-PC-phred_coding', 'GenoCanyon_score', 'integrated_fitCons_score', 'integrated_confidence_value', 'GM12878_fitCons_score', 'GM12878_confidence_value', 
                            'H1-hESC_fitCons_score', 'H1-hESC_confidence_value', 'HUVEC_fitCons_score', 'HUVEC_confidence_value', 'LINSIGHT', 'GERP++_RS', '1000Gp3_AF', '1000Gp3_AFR_AF', 
                            '1000Gp3_EUR_AF', '1000Gp3_AMR_AF', '1000Gp3_EAS_AF', '1000Gp3_SAS_AF', 'gnomAD_exomes_flag', 'gnomAD_exomes_AF', 'gnomAD_exomes_AFR_AF', 'gnomAD_exomes_AMR_AF', 
                            'gnomAD_exomes_ASJ_AF', 'gnomAD_exomes_EAS_AF', 'gnomAD_exomes_FIN_AF', 'gnomAD_exomes_NFE_AF', 'gnomAD_exomes_SAS_AF', 'clinvar_id', 'clinvar_clnsig', 'clinvar_trait', 
                            'clinvar_var_source']
            
                    point_cleanup_table.columns = columns_table

                    table_modify = modify_scores(point_cleanup_table)
                    finish_table = clinvar_null_drop(table_modify)
                    pos = list_file_names[name].find('_')
                    new_name = list_file_names[name][:pos]
                    #print(new_name)

                    finish_table.to_csv(f"{path_directory}/{directory[child_directory]}/{new_name}_cleanup.csv", index= False)

                except (pd.errors.ParserError, ValueError):
                    table = pd.read_csv(f"{path_directory}/{directory[child_directory]}/{list_file_names[name]}", sep= " ", low_memory=False)
                    cleanup_semicolon_table = semicolon_cleanup(table)
                    point_cleanup_table = point_cleanup(cleanup_semicolon_table)

                    columns_table = ['chr', 'pos(1-based)', 'ref', 'alt',	'aaref', 'aaalt', 'rs_dbSNP', 'hg19_chr', 'hg19_pos(1-based)', 'aapos', 'genename', 
                            'HGVSc_ANNOVAR', 'HGVSp_ANNOVAR', 'HGVSp_VEP', 'SIFT_pred', 'SIFT4G_pred', 'Polyphen2_HDIV_pred', 'Polyphen2_HVAR_pred',	'LRT_pred', 
                            'MutationTaster_pred', 'MutationAssessor_pred', 'FATHMM_pred', 'PROVEAN_pred', 'VEST4_score', 'MetaSVM_pred', 'MetaLR_pred', 'MetaRNN_pred', 
                            'M-CAP_pred', 'REVEL_score', 'MutPred_score', 'MVP_score', 'MPC_score', 'PrimateAI_pred', 'DEOGEN2_pred', 'BayesDel_addAF_pred', 'BayesDel_noAF_pred',
                            'ClinPred_pred', 'LIST-S2_pred', 'CADD_phred', 'CADD_phred_hg19', 'DANN_score', 'fathmm-MKL_coding_pred', 'fathmm-XF_coding_pred', 'Eigen-phred_coding',
                            'Eigen-PC-phred_coding', 'GenoCanyon_score', 'integrated_fitCons_score', 'integrated_confidence_value', 'GM12878_fitCons_score', 'GM12878_confidence_value', 
                            'H1-hESC_fitCons_score', 'H1-hESC_confidence_value', 'HUVEC_fitCons_score', 'HUVEC_confidence_value', 'LINSIGHT', 'GERP++_RS', '1000Gp3_AF', '1000Gp3_AFR_AF', 
                            '1000Gp3_EUR_AF', '1000Gp3_AMR_AF', '1000Gp3_EAS_AF', '1000Gp3_SAS_AF', 'gnomAD_exomes_flag', 'gnomAD_exomes_AF', 'gnomAD_exomes_AFR_AF', 'gnomAD_exomes_AMR_AF', 
                            'gnomAD_exomes_ASJ_AF', 'gnomAD_exomes_EAS_AF', 'gnomAD_exomes_FIN_AF', 'gnomAD_exomes_NFE_AF', 'gnomAD_exomes_SAS_AF', 'clinvar_id', 'clinvar_clnsig', 'clinvar_trait', 
                            'clinvar_var_source']
            
                    point_cleanup_table.columns = columns_table

                    table_modify = modify_scores(point_cleanup_table)
                    finish_table = clinvar_null_drop(table_modify)
                    pos = list_file_names[name].find('_')
                    new_name = list_file_names[name][:pos]
                    #print(new_name)

                    finish_table.to_csv(f"{path_directory}/{directory[child_directory]}/{new_name}_cleanup.csv", index= False)
                
            except pd.errors.EmptyDataError:
                os.remove(f"{path_directory}/{directory[child_directory]}/{list_file_names[name]}")

            except IndexError:
                break
            
            except FileNotFoundError: 
                child_directory += 1




     


        

if __name__ ==  '__main__':

    apply_cleanup("/home/matheus_mai/Trabalho_TCC/dbNSFP4.2a/Genes")

    directory, list_file_names = file_names_directories("/home/matheus_mai/Trabalho_TCC/dbNSFP4.2a/Genes")
    print(list_file_names)
    print(len(list_file_names))
    """
    table_ = pd.read_csv("/home/matheus_mai/Trabalho_TCC/dbNSFP4.2a/Genes/chr_1/ABCA4_ocorrencias.csv", sep= "\t", low_memory=False)
    cleanup_semicolon_table = semicolon_cleanup(table_)
    point_cleanup_table = point_cleanup(cleanup_semicolon_table)

    # Colunas
    columns_table = ['chr', 'pos(1-based)', 'ref', 'alt',	'aaref', 'aaalt', 'rs_dbSNP', 'hg19_chr', 'hg19_pos(1-based)', 'aapos', 'genename', 
           'HGVSc_ANNOVAR', 'HGVSp_ANNOVAR', 'HGVSp_VEP', 'SIFT_pred', 'SIFT4G_pred', 'Polyphen2_HDIV_pred', 'Polyphen2_HVAR_pred',	'LRT_pred', 
           'MutationTaster_pred', 'MutationAssessor_pred', 'FATHMM_pred', 'PROVEAN_pred', 'VEST4_score', 'MetaSVM_pred', 'MetaLR_pred', 'MetaRNN_pred', 
           'M-CAP_pred', 'REVEL_score', 'MutPred_score', 'MVP_score', 'MPC_score', 'PrimateAI_pred', 'DEOGEN2_pred', 'BayesDel_addAF_pred', 'BayesDel_noAF_pred',
           'ClinPred_pred', 'LIST-S2_pred', 'CADD_phred', 'CADD_phred_hg19', 'DANN_score', 'fathmm-MKL_coding_pred', 'fathmm-XF_coding_pred', 'Eigen-phred_coding',
           'Eigen-PC-phred_coding', 'GenoCanyon_score', 'integrated_fitCons_score', 'integrated_confidence_value', 'GM12878_fitCons_score', 'GM12878_confidence_value', 
           'H1-hESC_fitCons_score', 'H1-hESC_confidence_value', 'HUVEC_fitCons_score', 'HUVEC_confidence_value', 'LINSIGHT', 'GERP++_RS', '1000Gp3_AF', '1000Gp3_AFR_AF', 
           '1000Gp3_EUR_AF', '1000Gp3_AMR_AF', '1000Gp3_EAS_AF', '1000Gp3_SAS_AF', 'gnomAD_exomes_flag', 'gnomAD_exomes_AF', 'gnomAD_exomes_AFR_AF', 'gnomAD_exomes_AMR_AF', 
           'gnomAD_exomes_ASJ_AF', 'gnomAD_exomes_EAS_AF', 'gnomAD_exomes_FIN_AF', 'gnomAD_exomes_NFE_AF', 'gnomAD_exomes_SAS_AF', 'clinvar_id', 'clinvar_clnsig', 'clinvar_trait', 
           'clinvar_var_source']
    point_cleanup_table.columns = columns_table

    finish_table = modify_scores(point_cleanup_table)
    table_fim = clinvar_null_drop(finish_table)
    print(table_fim)
"""




    #create_directory('/home/matheus_mai/Trabalho_TCC/dbNSFP4.2a/Genes/chr_1')
 