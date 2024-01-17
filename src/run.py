import pandas as pd

from apply_statistics import ApplyStaatsInFiles


if __name__ == '__main__':
    
    absolute_path = '/home/matheus_mai/Trabalho_TCC/teste_refactoring/Genes_teste_cleanup'
    data_frame = ApplyStaatsInFiles().convert_list_dict_to_dataframe(absolute_path)
    #list_dict = (processar_arquivos_cleanup('/home/matheus_mai/Trabalho_TCC/dbNSFP4.2a/Genes'))
    
    #data_frame = convert_list_dict_to_dataframe(list_dict)
    #print(data_frame)
    data_frame.to_csv(f'{absolute_path}/table_generate_teste.csv', index=False)
  
    