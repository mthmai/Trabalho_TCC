#!/usr/bin/env python3

import logging
import os

#logger = logging.basicConfig(level=logging.DEBUG,  # Nível mínimo de log a ser exibido (DEBUG, INFO, WARNING, ERROR, CRITICAL)
#                    format='%(asctime)s - %(levelname)s - %(message)s')

# Exemplos de uso do logger
#logging.debug('Esta é uma mensagem de debug')
#logging.info('Esta é uma mensagem de informação')
#logging.warning('Esta é uma mensagem de aviso')
#logging.error('Esta é uma mensagem de erro')
#logging.critical('Esta é uma mensagem crítica')


class CustomFormatter(logging.Formatter):
    """Adapted from https://stackoverflow.com/a/56944256/3638629"""

    grey = '\u001b[30;246m'
    green = '\u001b[32;1m'
    blue = '\u001b[34;5;1m'
    white = '\u001b[37;1m'
    blinking = '\u001b[37;5;1m'
    yellow = '\u001b[33;1m'
    red = '\u001b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'
    background_red = '\u001b[41m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.green + self.fmt + self.reset,
            logging.INFO: self.white + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.background_red + self.blinking
            + self.fmt + self.reset
        }
        self.create_logs('./log')

    def create_logs(self, path):
        #logger.info('Creating directory structure for logging')
        if os.path.exists(path):
            ...
        else:
            os.system('mkdir log')

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(
            log_fmt,
            datefmt='%d/%m/%y %H:%M:%S'
        )
        return formatter.format(record)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Definir o nível global do logger

# Configurar o manipulador para saída no console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Nível mínimo para exibir no console
console_handler.setFormatter(CustomFormatter('%(message)s'))  # Usar a formatação personalizada
logger.addHandler(console_handler)

# Configurar o manipulador para saída no arquivo de log
file_handler = logging.FileHandler('log/miss_pred_log.log')
file_handler.setLevel(logging.DEBUG)  # Nível mínimo para escrever no arquivo
file_handler.setFormatter(CustomFormatter('%(asctime)s - %(levelname)s - %(message)s'))  # Usar a formatação personalizada
logger.addHandler(file_handler)
'''
logger = logging.getLogger()
#if log_level:
#    logger.setLevel(logging.DEBUG)
formatter_shell = '[%(asctime)s] %(levelname)s: %(message)s'
formatter_file = logging.Formatter(
    '[%(asctime)s] %(levelname)s: %(message)s (%(lineno)s)'
)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(CustomFormatter(formatter_shell))

fh = logging.FileHandler('log/miss_pred_log.log', 'a')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter_file)
'''