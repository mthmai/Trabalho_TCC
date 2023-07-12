import pandas as pd
from sklearn.metrics import cohen_kappa_score
from typing import List


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


if __name__ == '__main__':
    
    table = pd.read_csv('/home/matheus_mai/Trabalho_TCC/dbNSFP4.2a/Genes/chr_1/ABCA4_cleanup.csv')
    kappa_calculation(table)
    
