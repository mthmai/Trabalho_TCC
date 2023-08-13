import os

import pandas as pd


def verificar_qnt_mutacao(data_frame: pd.DataFrame, gene_name) -> pd.DataFrame:

    count_values = data_frame['clinvar_clnsig'].value_counts()
    dict_count_values = count_values.to_dict()
    label_dict = {1.0: 'patogenica', 0.0: 'benign'}

    finish_values =  {label_dict[key]: value for key, value in dict_count_values.items() if key in label_dict}

    finish_values['genename']= gene_name

    return finish_values

def percorrer_arquivos_aplicar_funcao(caminho_base) -> pd.DataFrame:

    dfs = []    
    for cromossomo in os.listdir(caminho_base):
        cromossomo_path = os.path.join(caminho_base, cromossomo)

        # Verificar se é um diretório
        if os.path.isdir(cromossomo_path):
            # Percorrer as tabelas no diretório do cromossomo
            for tabela in os.listdir(cromossomo_path):
                indx =+ 1
                # Verificar se a tabela contém '_cleanup.csv'
                if tabela.endswith('_cleanup.csv'):
                    file_path = os.path.join(cromossomo_path, tabela)
                    tabela = pd.read_csv(file_path)
                    print(cromossomo_path)
                    genename = file_path.replace((cromossomo_path + '/'), '')

                    data_dict = verificar_qnt_mutacao(tabela, genename.replace(('_cleanup.csv'), ''))
                    temp_df = pd.DataFrame(data_dict, index=[indx])
                    dfs.append(temp_df) 
    final_df = pd.concat(dfs, ignore_index= True)
    return final_df

                    



if __name__ == '__main__':

    tabela = pd.read_csv('/home/matheus_mai/Trabalho_TCC/dbNSFP4.2a/Genes/chr_1/ABCA4_cleanup.csv')
    data_frame = percorrer_arquivos_aplicar_funcao('/home/matheus_mai/Trabalho_TCC/dbNSFP4.2a/Genes')
    data_frame.to_csv('/home/matheus_mai/Desktop/qnt_variantes_dbNSFP.csv')
    
    #verificar_qnt_mutacao(tabela)
