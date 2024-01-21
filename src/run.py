import pandas as pd

from datetime import datetime
from apply_statistics import ApplyStaatsInFiles
from make_log import logger


if __name__ == '__main__':
    
    start = datetime.now()
    absolute_path = '/home/matheus_mai/Desktop/teste_runn/dbNSFP4.2a/Genes'
    data_frame = ApplyStaatsInFiles().convert_list_dict_to_dataframe(absolute_path)

    data_frame.to_csv(f'{absolute_path}/table_generate_teste.csv', index=False)
  
    elapsed = str(datetime.now() - start).split('.')[0]

    logger.info(f'Finished. Time elapsed: {elapsed}')