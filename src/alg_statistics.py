import math

import pandas as pd

from table_cleanup import CleanUpTable
from sklearn.metrics import cohen_kappa_score
from typing import List, Dict
from settings import list_columns


class CalculateStaats(CleanUpTable):
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe
    
    def _true_positive(self, column_name: str, idx_int) -> int:
        search_TP = (self.dataframe[(self.dataframe[column_name] == 1) & (self.dataframe[idx_int] == 1)])

        return len(search_TP.index)
    
    def _false_negative(self, column_name: str, idx_int) -> int:
        search_FN = (self.dataframe[(self.dataframe[column_name] == 1) & (self.dataframe[idx_int] == 0)])

        return len(search_FN.index)
    
    def _pat_no_class(self, column_name: str, idx_int: int) -> int:
        search_pat_no_class = (self.dataframe[(self.dataframe[column_name] == 1) & (self.dataframe[idx_int] == 10000)])

        return len(search_pat_no_class.index)
    
    def _false_positive(self, column_name: str, idx_int: int) -> int:
        search_FP = (self.dataframe[(self.dataframe[column_name] == 0) & (self.dataframe[idx_int] == 1)])

        return len(search_FP.index)
    
    def _true_negative(self, column_name: str, idx_int: int) -> int:
        search_TN = (self.dataframe[(self.dataframe[column_name] == 0) & (self.dataframe[idx_int] == 0)])

        return len(search_TN.index)
    
    def _ben_no_class(self, column_name: str, idx_int: int) -> int:
        search_ben_no_class = (self.dataframe[(self.dataframe[column_name] == 0) & (self.dataframe[idx_int] == 10000)])

        return len(search_ben_no_class.index)
    
    # sensibilidade
    # TP/(TP+FN)
    def calc_sensibility(self, column_name: str, idx_int: int) -> float:
        value_tp = self._true_positive(column_name, idx_int)
        value_fn = self._false_negative(column_name, idx_int)
        try:
            return value_tp / (value_tp + value_fn)
        except ZeroDivisionError:
            return None

    # especificidade
    # TN/(TN+FP)
    def calc_especificity(self, column_name: str, idx_int: int) -> float:
        value_tn = self._true_negative(column_name, idx_int)
        value_fp = self._false_positive(column_name, idx_int)
        try:
            return value_tn / (value_tn + value_fp)
        except ZeroDivisionError:
            return None

    # acurácia
    # (TP+TN)/(TP+TN+FN+FP)
    def calc_acuracy(self, column_name: str, idx_int: int) -> float:
        value_tp = self._true_positive(column_name, idx_int)
        value_tn = self._true_negative(column_name, idx_int)
        value_fp = self._false_positive(column_name, idx_int)
        value_fn = self._false_negative(column_name, idx_int)
        try:
            return (value_tp + value_tn) / (value_tp + value_tn + value_fn + value_fp)
        except ZeroDivisionError:
            return None
        
    def calc_kappa(self, standard_column: str, program_column: str) -> float:
        #col_1 = program_column.tolist()
        #col_2 = standard_column.tolist()
        col_1, col_2 = self._drop_values_to_kappa_score(standard_column, program_column)
        col_1_nan = list(filter(lambda x: not math.isnan(x), col_1))
        col_2_nan = list(filter(lambda x: not math.isnan(x), col_2))

        print(standard_column, program_column)
        print(col_1_nan, col_2_nan)
        
        return cohen_kappa_score(col_1_nan, col_2_nan)


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

'''
if __name__ == '__main__':
    

    table = pd.read_csv('/home/matheus_mai/Desktop/table_teste_TCC.csv')
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
'''
if __name__ == '__main__':
    import pandas as pd
    dataframe = pd.read_csv('/home/matheus_mai/Desktop/table_teste_TCC.csv')
    dataframe_clean = CalculateStaats(dataframe)._drop_columns(list_columns)
    dictionary_statistics = {'programs': [], 'sensibility': [], 'especificity': [], 'acuracy': [], 'kappa_value': []}
    for name_column in dataframe_clean.columns[14:51]:
        dictionary_statistics['programs'].append(name_column)
        dictionary_statistics['sensibility'].append(CalculateStaats(dataframe_clean).calc_sensibility('clinvar_clnsig', name_column))
        dictionary_statistics['especificity'].append(CalculateStaats(dataframe_clean).calc_especificity('clinvar_clnsig', name_column))
        dictionary_statistics['acuracy'].append(CalculateStaats(dataframe_clean).calc_acuracy('clinvar_clnsig', name_column))
        dictionary_statistics['sensibility'].append(CalculateStaats(dataframe_clean).calc_sensibility('clinvar_clnsig', name_column))
        dictionary_statistics['kappa_value'].append(CalculateStaats(dataframe_clean).calc_kappa('clinvar_clnsig', name_column))