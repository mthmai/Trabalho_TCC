import pandas as pd
from sklearn.metrics import cohen_kappa_score
from typing import List




def drop_colums(lista_columns: List[str], table: pd.DataFrame) -> pd.DataFrame:
    
    return table.drop(columns= list_columns)

def true_positive(table: pd.DataFrame, column_name: str, idx_int: int) -> int:

    search_TP = (table[(table[column_name] == 1) & (table[idx_int] == 1)])

    return len(search_TP.index)

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
    
    table = pd.read_csv('/home/matheus_mai/Desktop/teste_execute_statistics.csv')
    #kappa_calculation(table)
    list_columns = ['HUVEC_confidence_value','H1-hESC_confidence_value','GM12878_confidence_value','integrated_confidence_value', '1000Gp3_AF','1000Gp3_AFR_AF', '1000Gp3_EUR_AF', '1000Gp3_AMR_AF', '1000Gp3_EAS_AF','1000Gp3_SAS_AF', 'gnomAD_exomes_flag', 'gnomAD_exomes_AF','gnomAD_exomes_AFR_AF', 
                    'gnomAD_exomes_AMR_AF', 'gnomAD_exomes_ASJ_AF','gnomAD_exomes_EAS_AF', 'gnomAD_exomes_FIN_AF', 'gnomAD_exomes_NFE_AF','gnomAD_exomes_SAS_AF', 'clinvar_id', 'clinvar_trait', 'clinvar_var_source']
    
    
    #for i, row in table.iterrows():
        #print(row)
    
    table_drop = drop_colums(list_columns, table)
    for idx in table_drop.columns[14:52]:
        search_TP = (table_drop[(table_drop['clinvar_clnsig'] == 1) & (table_drop[idx] == 1)])
        search_PAT_nao_class = (table_drop[(table_drop['clinvar_clnsig'] == 1) & (table_drop[idx] == 10000)])

        print(len(search_PAT_nao_class.index))
        #print(table_drop[idx])