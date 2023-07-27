import pandas as pd

from apply_statistics import processar_arquivos_cleanup, convert_list_dict_to_dataframe


if __name__ == '__main__':
    
    list_dict = (processar_arquivos_cleanup('/home/ubuntu/Área de Trabalho/Genes_teste'))
    
    data_frame = convert_list_dict_to_dataframe(list_dict)
    print(data_frame)
    data_frame.to_csv('/home/ubuntu/Área de Trabalho/seila_teste.csv', index=False)
  
    