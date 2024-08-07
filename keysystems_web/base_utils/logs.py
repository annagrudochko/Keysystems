from keysystems_web.settings import TIME_ZONE

from datetime import datetime

import logging
import os
import traceback
import re


# запись ошибок
def log_error(message, wt: bool = True):
    # now = datetime.now(TIME_ZONE)
    now = datetime.now()
    log_folder = now.strftime ('%m-%Y')
    log_path = os.path.join('logs', log_folder)

    if not os.path.exists(log_path):
        os.makedirs(log_path)

    log_file_path = os.path.join(log_path, f'{now.day}.log')
    logging.basicConfig (level=logging.WARNING, filename=log_file_path, encoding='utf-8')
    # logger = logging.getLogger(f'error_logger_{now}')

    if wt:
        ex_traceback = traceback.format_exc()
        tb = ''
        msg = ''
        start_row = '    File "/app'
        tb_split = ex_traceback.split('\n')
        for row in tb_split:
            if row.startswith(start_row) and not re.search ('venv', row):
                tb += f'{row}\n'

            if not row.startswith(' '):
                msg += f'{row}\n'

        logging.warning(f'{now}\n{tb}\n\n{msg}\n---------------------------------\n')
        return msg
    else:
        logging.warning(f'{now}\n{message}\n\n---------------------------------\n')