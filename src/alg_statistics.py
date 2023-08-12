import math

import pandas as pd

from sklearn.metrics import cohen_kappa_score
from typing import List, Dict


def drop_colums(list_columns: List[str], table: pd.DataFrame) -> pd.DataFrame:
    
    return table.drop(columns= list_columns)

def true_positive(table: pd.DataFrame, column_name: str, idx_int: int) -> int:

    search_TP = (table[(table[column_name] == 1) & (table[idx_int] == 1)])

    return len(search_TP.index)

def false_negative(table: pd.DataFrame, column_name: str, idx_int: int) -> int:

    search_FN = (table[(table[column_name] == 1) & (table[idx_int] == 0)])

    return len(search_FN.index)

def pat_no_class(table: pd.DataFrame, column_name: str, idx_int: int) -> int:

    search_pat_no_class = (table[(table[column_name] == 1) & (table[idx_int] == 10000)])

    return len(search_pat_no_class.index)

def false_positive(table: pd.DataFrame, column_name: str, idx_int: int) -> int:

    search_FP = (table[(table[column_name] == 0) & (table[idx_int] == 1)])

    return len(search_FP.index)

def true_negative(table: pd.DataFrame, column_name: str, idx_int: int) -> int:

    search_TN = (table[(table[column_name] == 0) & (table[idx_int] == 0)])

    return len(search_TN.index)

def ben_no_class(table: pd.DataFrame, column_name: str, idx_int: int) -> int:

    search_ben_no_class = (table[(table[column_name] == 0) & (table[idx_int] == 10000)])

    return len(search_ben_no_class.index)

# sensibilidade
# TP/(TP+FN)
def calc_sensibility(value_tp: int, value_fn: int) -> int:
    try:
        return value_tp / (value_tp + value_fn)
    except ZeroDivisionError:
        return None

# especificidade
# TN/(TN+FP)
def calc_especificity(value_tn: int, value_fp: int) -> int:
    try:
        return value_tn / (value_tn + value_fp)
    except ZeroDivisionError:
        return None

# acurácia
# (TP+TN)/(TP+TN+FN+FP)
def calc_acuracy(value_tp: int, value_tn: int, value_fn: int, value_fp: int) -> int:
    try:
        return (value_tp + value_tn) / (value_tp + value_tn + value_fn + value_fp)
    except ZeroDivisionError:
        return None


def get_list_TP(dictionary_calc: Dict[str, int]) -> List[int]:

    return dictionary_calc.get('TP')

def get_list_TN(dictionary_calc: Dict[str, int]) -> List[int]:

    return dictionary_calc.get('TN')

def get_list_FP(dictionary_calc: Dict[str, int]) -> List[int]:

    return dictionary_calc.get('FP')

def get_list_FN(dictionary_calc: Dict[str, int]) -> List[int]:

    return dictionary_calc.get('FN')

def teste_kappa(program_column: pd.core.series.Series, standard_column: pd.core.series.Series):
    col_1 = program_column.tolist()
    col_2 = standard_column.tolist()
    col_1_nan = list(filter(lambda x: not math.isnan(x), col_1))
    col_2_nan = list(filter(lambda x: not math.isnan(x), col_2))


    print(col_1_nan, col_2_nan)
    
    return cohen_kappa_score(col_1_nan, col_2_nan)

def kappa_to_apply(table: pd.DataFrame, standard_column: str ,dictionary: Dict) -> Dict:

    table_cut = table.drop(table[table[standard_column] == 10000].index)
    for idx in table.columns[14:52]:
        cut_df = table_cut.loc[:,[idx, standard_column]]
        drop_df = cut_df.drop(cut_df[cut_df[idx] == 10000].index)
        dictionary['kappa_value'].append(teste_kappa(drop_df[idx], drop_df[standard_column]))    
        
    return dictionary
# teste de kappa
def kappa_calculation(table: pd.DataFrame) -> List[int]:
    
    kappa_list = list()
    print('TABLE COLUMNS: ', table.columns[14:73])
    for idx in table.columns[14:55]:
        df_corte = table.loc[:, [idx, 'clinvar_clnsig']]
        teste_drop = df_corte[df_corte[idx] == '10000'].index
        df_corte.drop(teste_drop, inplace=True)
        cortado = df_corte[idx].tolist()
        #print(cortado)
        #print(w)
        clinvar_corte = df_corte['clinvar_clnsig'].tolist()
        print(clinvar_corte)
        kappa_list = cohen_kappa_score(cortado, clinvar_corte)
        kappa_list.append((kappa_list))




"""
def true_positive():
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
"""

if __name__ == '__main__':
    
    table = pd.read_csv('/home/ubuntu/Área de Trabalho/table_teste_TCC.csv')
    #kappa_calculation(table)
    #list_columns = ['HUVEC_confidence_value','H1-hESC_confidence_value','GM12878_confidence_value','integrated_confidence_value', '1000Gp3_AF','1000Gp3_AFR_AF', '1000Gp3_EUR_AF', '1000Gp3_AMR_AF', '1000Gp3_EAS_AF','1000Gp3_SAS_AF', 'gnomAD_exomes_flag', 'gnomAD_exomes_AF','gnomAD_exomes_AFR_AF', 
    #                'gnomAD_exomes_AMR_AF', 'gnomAD_exomes_ASJ_AF','gnomAD_exomes_EAS_AF', 'gnomAD_exomes_FIN_AF', 'gnomAD_exomes_NFE_AF','gnomAD_exomes_SAS_AF', 'clinvar_id', 'clinvar_trait', 'clinvar_var_source']
    
    list_columns = ['HUVEC_confidence_value','H1-hESC_confidence_value','GM12878_confidence_value',
                    'integrated_confidence_value', 'clinvar_id', 'clinvar_source']
    dictionary_calcs = {'TP': [], 'FN': [], 'FP': [], 'TN': []}
    #print(type(table_drop['clinvar_clnsig']))
    table_drop = drop_colums(list_columns, table)
    for i in table_drop.columns[14:51]:
        dictionary_calcs['TP'].append(true_positive(table_drop, 'clinvar_clnsig', i))
        dictionary_calcs['FN'].append(false_negative(table_drop, 'clinvar_clnsig', i))
        dictionary_calcs['FP'].append(false_positive(table_drop, 'clinvar_clnsig', i))
        dictionary_calcs['TN'].append(true_negative(table_drop, 'clinvar_clnsig', i))
    #print(dictionary_calcs)
    

    list_TP = get_list_TP(dictionary_calcs)
    list_FN = get_list_FN(dictionary_calcs)
    list_FP = get_list_FP(dictionary_calcs)
    list_TN = get_list_TN(dictionary_calcs)
    programs_name = table_drop.columns[14:51]

    print('Table_DROP: ', table_drop.columns[14:51])
    dictionary_statistics = {'programs': [], 'sensibility': [], 'especificity': [], 'acuracy': [], 'kappa_value': []}
    for idx in range(len(list_TP)):
        dictionary_statistics['sensibility'].append(calc_sensibility(list_TP[idx], list_FN[idx]))
        dictionary_statistics['especificity'].append(calc_especificity(list_TN[idx], list_FP[idx]))
        dictionary_statistics['acuracy'].append(calc_acuracy(list_TP[idx], list_TN[idx], list_FN[idx], list_FP[idx]))
        dictionary_statistics['programs'].append(programs_name[idx])
    #print('Sensibilidade: ', dictionary_statistics['sensibility'])
    #print('Especificidade: ', dictionary_statistics['especificity'])
    #print('Acuracia: ', dictionary_statistics['acuracy'])
    dictionary_statistics = kappa_to_apply(table_drop, 'clinvar_clnsig', dictionary_statistics)
    print(dictionary_statistics['kappa_value'])
    df = pd.DataFrame.from_dict(dictionary_statistics, orient='index').transpose()
    print(df)
        
