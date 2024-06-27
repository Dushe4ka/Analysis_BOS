import os
import time
from analysis import analysis
from config import config
from utils import create_database

"""
Исходные данные
"""
PATH = os.path.join('debug.log')
PATH_JSON = os.path.join('log_analysics.json')
pattern = str(input("Введите ключевое слово для поиска: "))
params = config()


def detect_file_changes(file_path, PATH_JSON, interval=1):
    """
    Функция проверки на изменение файла
    """
    last_read = 0
    last_modified = 0
    create_database('bosik', params)
    while True:
        current_modified = os.path.getmtime(file_path)
        if current_modified != last_modified:
            last_read = analysis(file_path, PATH_JSON, pattern, last_read, params)
            print("File has changed!")
            last_modified = current_modified
        time.sleep(interval)


detect_file_changes(PATH, PATH_JSON)
