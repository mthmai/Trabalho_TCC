import pandas as pd
from peewee import JOIN, DoesNotExist

from typing import List

from create_db import Classificacao, Alteracao, Gene, db
from alg_statistics import CalculateStaats
from make_log import logger
from settings import columns_table_to_search

class SearchDataBase:
    def __init__(self, dataframe):
        self.dataframe = self._validated_data_frame(dataframe)
    
    @property
    def gene_name(self):
        return self.dataframe['gene_name'].unique()[0]

    def _validated_data_frame(self, dataframe: pd.DataFrame):
        
        for column in columns_table_to_search:
            try:
                dataframe[column]
            except KeyError:
                raise (f'Dataframe não está correto, está faltando a coluna {column}')

        return dataframe
    
    def search_data(self):
        if db.connect() == False:
            db.connect()

        dataframes = list()
        gene_name = self.dataframe['gene_name'].unique()

        if len(gene_name) > 1:
            raise (f'O dataframe apresenta mais de um nome de gene. Verifique a informação e prossiga.')
        
        hgvsc_annovar = self.dataframe['HGVSc_ANNOVAR'].unique()
        hgvsp_annovar = self.dataframe['HGVSp_ANNOVAR'].unique()
        hgvsp_vep = self.dataframe['HGVSp_VEP'].unique()

        for idx in range (len(hgvsc_annovar)):
            try:
                classificacoes = (
                    Classificacao.select().join(Alteracao).join(Gene).where((Gene.gene_name == self.gene_name) 
                                                            & (Alteracao.HGVSc_ANNOVAR == hgvsc_annovar[idx])
                                                        )
                ).get()
                dict_return = (
                    Classificacao.select().join(Alteracao).join(Gene).where((Gene.gene_name == self.gene_name) 
                                                            & (Alteracao.HGVSc_ANNOVAR == hgvsc_annovar[idx])
                                                        )
                )
                df = pd.DataFrame(list(dict_return.dicts()))

            except DoesNotExist:
                try:
                    classificacoes = (
                        Classificacao.select().join(Alteracao).join(Gene).where((Gene.gene_name == self.gene_name) 
                                                                & (Alteracao.HGVSp_ANNOVAR == hgvsp_annovar[idx])
                                                            )
                    ).get()
                    dict_return = (
                        Classificacao.select().join(Alteracao).join(Gene).where((Gene.gene_name == self.gene_name) 
                                                                & (Alteracao.HGVSp_ANNOVAR == hgvsp_annovar[idx])
                                                            )
                    )
                    df = pd.DataFrame(list(dict_return.dicts()))

                except DoesNotExist:
                    try:
                        classificacoes = (
                            Classificacao.select().join(Alteracao).join(Gene).where((Gene.gene_name == self.gene_name) 
                                                                    & (Alteracao.HGVSp_VEP == hgvsp_vep[idx])
                                                                )
                        ).get()
                        dict_return = (
                            Classificacao.select().join(Alteracao).join(Gene).where((Gene.gene_name == self.gene_name) 
                                                                    & (Alteracao.HGVSp_VEP == hgvsp_vep[idx])
                                                                )
                        )
                        df = pd.DataFrame(list(dict_return.dicts()))
                    except DoesNotExist:
                        logger.info(f'As mutações: {hgvsc_annovar[idx]}, {hgvsp_annovar[idx]} e {hgvsp_vep[idx]} não estão presentes para o gene {gene_name}')
                        df = pd.DataFrame()
            dataframes.append(df)
            db.close()
        return dataframes
    
    def return_dataframe(self, list_dataframes: List[pd.DataFrame]):
        return pd.concat(list_dataframes, ignore_index=True)
    

if __name__ == '__main__':
    teste = str(input(print('Coloque o caminho do arquivo que deseja utilizar: \n')))
    teste_2 = int(input(print('Deseja utilizar o clinvar como padrão: \n 1-Sim;\n 2-Não;')))
    df_inicial = pd.read_csv(teste)
    list_dataframes = SearchDataBase(df_inicial).search_data()
    result_df = SearchDataBase(df_inicial).return_dataframe(list_dataframes)
    nome_gene = SearchDataBase(df_inicial).gene_name

    if teste_2 == 1:

        #print(df_final)
        dictionary_statistics = {'gene_name': [], 'programs': [], 'sensibility': [], 'especificity': [], 'acuracy': [], 'kappa_value': []}
        for name_column in result_df.columns[2::]:
            dictionary_statistics['gene_name'].append(nome_gene)
            dictionary_statistics['programs'].append(name_column)
            dictionary_statistics['sensibility'].append(CalculateStaats(result_df).calc_sensibility('clinvar_clnsig', name_column))
            dictionary_statistics['especificity'].append(CalculateStaats(result_df).calc_especificity('clinvar_clnsig', name_column))
            dictionary_statistics['acuracy'].append(CalculateStaats(result_df).calc_acuracy('clinvar_clnsig', name_column))
            dictionary_statistics['sensibility'].append(CalculateStaats(result_df).calc_sensibility('clinvar_clnsig', name_column))
            dictionary_statistics['kappa_value'].append(CalculateStaats(result_df).calc_kappa('clinvar_clnsig', name_column))

        print(dictionary_statistics)
    
    elif teste_2 == 2:
        result_df = result_df.drop(columns=['clinvar_clnsig'])
        try:
            df_inicial['padrão']
        except KeyError:
            print('A coluna padrão não foi encontrada na tabela que foi passada. Verifique isso e tente novamente.')
        
        result_df['padrão'] = df_inicial['padrão'].copy()
        #print(df_final)
        dictionary_statistics = {'gene_name': [], 'programs': [], 'sensibility': [], 'especificity': [], 'acuracy': [], 'kappa_value': []}
        for name_column in result_df.columns[2::]:
            dictionary_statistics['gene_name'].append(nome_gene)
            dictionary_statistics['programs'].append(name_column)
            dictionary_statistics['sensibility'].append(CalculateStaats(result_df).calc_sensibility('padrão', name_column))
            dictionary_statistics['especificity'].append(CalculateStaats(result_df).calc_especificity('padrão', name_column))
            dictionary_statistics['acuracy'].append(CalculateStaats(result_df).calc_acuracy('padrão', name_column))
            dictionary_statistics['sensibility'].append(CalculateStaats(result_df).calc_sensibility('padrão', name_column))
            dictionary_statistics['kappa_value'].append(CalculateStaats(result_df).calc_kappa('padrão', name_column))

        print(dictionary_statistics)

    else:
        print(f'O numero {teste_2} não é válido. Rode novamente e tente de novo.')


'''    
if __name__ == '__main__':
    db.connect()
    nome_gene = 'ABCA4'
    hgvsc_annovar = 'c.3163C>T'
    hgvsp_annovar = ''
    hgvsp_vep = 'p.Arg1055Ter'
    list_hgvs = ['c.3163C>T', 'c.3140G>T', 'c.3089A>G', 'c.3062T>C', 'c.2762G>A', 'c.2608A>C', 'c.2495G>C', 'c.2465G>A', 'c.2453T>C']
    dataframes = list()
    # Consulta para buscar todas as Classificacoes associadas ao gene 'OR4F5'

    for classi in list_hgvs:
        classificacoes = (
        Classificacao.select().join(Alteracao).join(Gene).where((Gene.gene_name == nome_gene) 
                                                            & (Alteracao.HGVSc_ANNOVAR == classi)
                                                        )
        )

        df = pd.DataFrame(list(classificacoes.dicts()))
        dataframes.append(df)

    result_df = pd.concat(dataframes, ignore_index=True)
    print(result_df)

    dictionary_statistics = {'gene_name': [], 'programs': [], 'sensibility': [], 'especificity': [], 'acuracy': [], 'kappa_value': []}
    for name_column in result_df.columns[2::]:
        print('Aqui é o nome da coluna: ', name_column)
        dictionary_statistics['gene_name'].append(nome_gene)
        dictionary_statistics['programs'].append(name_column)
        dictionary_statistics['sensibility'].append(CalculateStaats(result_df).calc_sensibility('clinvar_clnsig', name_column))
        dictionary_statistics['especificity'].append(CalculateStaats(result_df).calc_especificity('clinvar_clnsig', name_column))
        dictionary_statistics['acuracy'].append(CalculateStaats(result_df).calc_acuracy('clinvar_clnsig', name_column))
        dictionary_statistics['sensibility'].append(CalculateStaats(result_df).calc_sensibility('clinvar_clnsig', name_column))
        dictionary_statistics['kappa_value'].append(CalculateStaats(result_df).calc_kappa('clinvar_clnsig', name_column))

    print(dictionary_statistics)
    db.close()
'''