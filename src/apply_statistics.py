import pandas as pd
import os

from typing import Dict, List
from alg_statistics import (drop_colums, true_positive, false_negative, false_positive, true_negative, 
                            get_list_FN, get_list_FP, get_list_TN, get_list_TP, calc_acuracy, calc_sensibility, 
                            calc_especificity, kappa_to_apply)


def apply_calcs_statistics_in_dataframe(table: pd.DataFrame, cromossomo: str, gene_name: str) -> Dict:
    
    list_columns = ['HUVEC_confidence_value','H1-hESC_confidence_value','GM12878_confidence_value',
                    'integrated_confidence_value', '1000Gp3_AF','1000Gp3_AFR_AF', '1000Gp3_EUR_AF', '1000Gp3_AMR_AF',
                    '1000Gp3_EAS_AF','1000Gp3_SAS_AF', 'gnomAD_exomes_flag', 'gnomAD_exomes_AF','gnomAD_exomes_AFR_AF', 
                    'gnomAD_exomes_AMR_AF', 'gnomAD_exomes_ASJ_AF','gnomAD_exomes_EAS_AF', 'gnomAD_exomes_FIN_AF', 'gnomAD_exomes_NFE_AF',
                    'gnomAD_exomes_SAS_AF', 'clinvar_id', 'clinvar_trait', 'clinvar_var_source']
    '''
    list_columns = ['HUVEC_confidence_value','H1-hESC_confidence_value','GM12878_confidence_value',
                    'integrated_confidence_value', 'clinvar_id', 'clinvar_source']
'''
    dictionary_calcs = {'TP': [], 'FN': [], 'FP': [], 'TN': []}
    table_drop = drop_colums(list_columns, table)
    print(table_drop.columns)
    for idx in table_drop.columns[14:52]:
        dictionary_calcs['TP'].append(true_positive(table_drop, 'clinvar_clnsig', idx))
        dictionary_calcs['FN'].append(false_negative(table_drop, 'clinvar_clnsig', idx))
        dictionary_calcs['FP'].append(false_positive(table_drop, 'clinvar_clnsig', idx))
        dictionary_calcs['TN'].append(true_negative(table_drop, 'clinvar_clnsig', idx))    

    list_TP = get_list_TP(dictionary_calcs)
    list_FN = get_list_FN(dictionary_calcs)
    list_FP = get_list_FP(dictionary_calcs)
    list_TN = get_list_TN(dictionary_calcs)
    programs_name = table_drop.columns[14:52]

    dictionary_statistics = {'chr': [], 'genename': [], 'programs': [], 'sensibility': [], 'especificity': [], 'acuracy': [], 'kappa_value': []}
    for idx in range(len(list_TP)):
        dictionary_statistics['chr'].append(cromossomo)
        dictionary_statistics['sensibility'].append(calc_sensibility(list_TP[idx], list_FN[idx]))
        dictionary_statistics['especificity'].append(calc_especificity(list_TN[idx], list_FP[idx]))
        dictionary_statistics['acuracy'].append(calc_acuracy(list_TP[idx], list_TN[idx], list_FN[idx], list_FP[idx]))
        dictionary_statistics['programs'].append(programs_name[idx])
        dictionary_statistics['genename'].append(gene_name)
    dictionary_statistics = kappa_to_apply(table_drop, 'clinvar_clnsig', dictionary_statistics)
    
    return dictionary_statistics


def processar_arquivos_cleanup(caminho_base):
    # Percorrer os diretórios de cromossomos
    list_dict_statistics = list()
    for cromossomo in os.listdir(caminho_base):
        cromossomo_path = os.path.join(caminho_base, cromossomo)

        # Verificar se é um diretório
        if os.path.isdir(cromossomo_path):
            # Percorrer as tabelas no diretório do cromossomo
            for tabela in os.listdir(cromossomo_path):
                # Verificar se a tabela contém '_cleanup.csv'
                if tabela.endswith('_cleanup.csv'):
                    file_path = os.path.join(cromossomo_path, tabela)
                    tabela = pd.read_csv(file_path)
                    print(file_path.replace((cromossomo_path + '/'), ''))
                    print('CROMOSSOMO PATH REPLACE: ', cromossomo_path.replace((caminho_base + '/'), ''))
                    print('FILE PATH REPLACE', file_path.replace((cromossomo_path + '/'), ''))
                    genename = file_path.replace((cromossomo_path + '/'), '')
                    dict_stats_temp = apply_calcs_statistics_in_dataframe(tabela, cromossomo_path.replace((caminho_base + '/'), ''), genename.replace(('_cleanup.csv'), ''))
                    list_dict_statistics.append(dict_stats_temp)
    return list_dict_statistics


def convert_list_dict_to_dataframe(list_dict: List[Dict]) -> pd.DataFrame:

    print("A lista de dicionarios: ", list_dict)
    data = {k: [item for sublist in [d[k] for d in list_dict] for item in sublist] for k in list_dict[0]}
    df = pd.DataFrame(data)

    return df

