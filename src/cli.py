#!/usr/bin/env python3

import argparse
import csv
import logging
import sys
import pandas as pd
import textwrap

from datetime import datetime

from alg_statistics import CalculateStaats
from create_db import db, Gene, Alteracao, Classificacao
from make_log import logger
from search_database import SearchDataBase
#logging.basicConfig(level=logging.DEBUG,  # Nível mínimo de log a ser exibido (DEBUG, INFO, WARNING, ERROR, CRITICAL)
#                    format='%(asctime)s - %(levelname)s - %(message)s')

class CliMethods:
    NAME= 'MissPred'
    CLI_VERSION = 'v1.2 '
    DESCRIPTION = 'Programa de avaliação de preditores de variantes genéticas'
    asterisc = '*'
    space = ' '

    def __init__(self):
        self.__run()

    def __run(self):
        self.parser = argparse.ArgumentParser(
            prog = ' '.join(sys.argv),
            formatter_class = argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent(
                """\
                \33[1m{0}
                *{1}{4} {2}{1}*
                {0}
                *{3}{5}{3}*
                {0}
                \33[0m
                """.format(self.asterisc * 68, self.space * 26, self.CLI_VERSION, self.space * 4, self.NAME, self.DESCRIPTION,)
            ),
            epilog = 'Hospital de Clinicas Porto Alegre - RS - Brasil',
            usage = '%(prog)s [options]',
            conflict_handler = 'resolve',
        )

        self.parser.version = self.CLI_VERSION

        self.parser.add_argument('-v', '--version', action = 'version')
        subparsers = self.parser.add_subparsers(help = 'MissPred comandos implementados', dest = 'command')
        
        self.populate_db = subparsers.add_parser(
            'populate',
            help = 'Popular dados na database',
            conflict_handler= 'resolve',
        )

        self.populate_db.add_argument(
            '-f',
            '--file',
            help = 'Tabela que deseja popular na database. Ex: ',
            required = True,
            type= str,
        )

        self.staats_db = subparsers.add_parser(
            'staatsdb',
            help = 'Aplicar calculo de estatísticas para determinadas sequências',
            conflict_handler = 'resolve',
        )

        self.staats_db.add_argument(
            '-f',
            '--file',
            help = 'Tabela contendo as mutações para determinado gene que deseja avaliar. Ex: ',
            required = True,
            type= str,
        )

        self.staats_db.add_argument(
            '-sd',
            '--standard',
            help = 'Qual padrão deseja utilizar. 1- Clinvar; 2- Passar um padrão;',
            type = int,
        )

        self.staats_db.add_argument(
            '-fr',
            '--fileresult',
            help = 'Caminho para a criação da tabela resultante do algoritmo. Ex: ',
            required = True,
            type= str,
        )

        args = self.parser.parse_args()

        if args.command == 'populate':
            self.__populate_database(args)

        elif args.command == 'staatsdb':
            self.__staats_db_apply(args)

        else:
            logger.warning('Função acionada não existe')

    def __populate_database(self, args):
        start = datetime.now()
        db.connect()
        db.create_tables([Gene, Alteracao, Classificacao])
        with open(args.file, 'r') as file:
            reader = csv.DictReader(file)
    
            for row in reader:
                # Crie ou obtenha o Gene associado
                gene, created = Gene.get_or_create(chr=row['chr'], gene_name=row['genename'])

                # Crie a Alteracao associada
                alteracao = Alteracao.create(gene_name=gene, **row)

                # Crie a Classificacao associada
                classificacao = Classificacao.create(alteracao=alteracao, **row)

        # Feche a conexão com o banco de dados
        db.close()
        logger.info('Database populada com sucesso!')
        elapsed = str(datetime.now() - start).split('.')[0]

        logger.info(f'Finished. Time elapsed: {elapsed}')


    def __staats_db_apply(self, args):
        start = datetime.now()

        if args.standard == 1:
            df_inicial = pd.read_csv(args.file)
            list_dataframes = SearchDataBase(df_inicial).search_data()
            result_df = SearchDataBase(df_inicial).return_dataframe(list_dataframes)
            nome_gene = SearchDataBase(df_inicial).gene_name
            dictionary_statistics = {'gene_name': [], 'programs': [], 'sensibility': [], 'especificity': [], 'acuracy': [], 'kappa_value': []}
            for name_column in result_df.columns[2::]:
                dictionary_statistics['gene_name'].append(nome_gene)
                dictionary_statistics['programs'].append(name_column)
                dictionary_statistics['sensibility'].append(CalculateStaats(result_df).calc_sensibility('clinvar_clnsig', name_column))
                dictionary_statistics['especificity'].append(CalculateStaats(result_df).calc_especificity('clinvar_clnsig', name_column))
                dictionary_statistics['acuracy'].append(CalculateStaats(result_df).calc_acuracy('clinvar_clnsig', name_column))
                dictionary_statistics['kappa_value'].append(CalculateStaats(result_df).calc_kappa('clinvar_clnsig', name_column))
            
            #for key in dictionary_statistics:

                #logger.info(f'Aqui é o tamanho da lista {key}: {len(dictionary_statistics[key])}')
            dataframe_return = pd.DataFrame(dictionary_statistics)

            dataframe_return.to_csv(args.fileresult)

        elif args.standard == 2:
            df_inicial = pd.read_csv(args.file)
            list_dataframes = SearchDataBase(df_inicial).search_data()
            result_df = SearchDataBase(df_inicial).return_dataframe(list_dataframes)
            nome_gene = SearchDataBase(df_inicial).gene_name
            if len(result_df) > 1:
                result_df = result_df.drop(columns=['clinvar_clnsig'])
                try:
                    df_inicial['padrão']
                except KeyError:
                    logger.warning('A coluna padrão não foi encontrada na tabela que foi passada. Verifique isso e tente novamente.')
                
                result_df['padrão'] = df_inicial['padrão'].copy()
                #print(df_final)
                dictionary_statistics = {'gene_name': [], 'programs': [], 'sensibility': [], 'especificity': [], 'acuracy': [], 'kappa_value': []}
                for name_column in result_df.columns[2::]:
                    dictionary_statistics['gene_name'].append(nome_gene)
                    dictionary_statistics['programs'].append(name_column)
                    dictionary_statistics['sensibility'].append(CalculateStaats(result_df).calc_sensibility('padrão', name_column))
                    dictionary_statistics['especificity'].append(CalculateStaats(result_df).calc_especificity('padrão', name_column))
                    dictionary_statistics['acuracy'].append(CalculateStaats(result_df).calc_acuracy('padrão', name_column))
                    dictionary_statistics['kappa_value'].append(CalculateStaats(result_df).calc_kappa('padrão', name_column))
                dataframe_return = pd.DataFrame(dictionary_statistics)

                dataframe_return.to_csv(args.fileresult)
            else:
                logger.warning(f'Não foi encontrado nenhuma mutação na database. Cheque se a tabela do gene {nome_gene} foi populado')

        else:
            logger.warning(f'O numero {args.standard} não é válido. Rode novamente e tente de novo.')

        elapsed = str(datetime.now() - start).split('.')[0]

        logger.info(f'Finished. Time elapsed: {elapsed}')

cli = CliMethods()