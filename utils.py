import json
import psycopg2
import os


def get_data(file_path):
    """
    Загрузка и чтение данных из файла JSON.
    """
    with open(file_path) as f:
        data = json.load(f)
        return data


def create_database(database_name, params):
    """Создание базы данных и таблиц для сохранения данных о сообщениях."""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        cur.execute(f"DROP DATABASE IF EXISTS {database_name};")
    except:
        pass
    try:
        cur.execute(f"CREATE DATABASE {database_name};")
    except:
        pass

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS message
            (id serial,
            date_m varchar(30),
            info_m varchar(30),
            application_m varchar(30),
            action_m varchar(150));
            """)

    conn.commit()
    conn.close()


def save_data_to_database(database_name, messages, params):
    """Сохранение данных о собщения о вирусе в базу данных"""
    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for message in messages['message']:
            cur.execute("""
                INSERT INTO message (date_m, info_m, application_m, action_m)
                VALUES (%s, %s, %s, %s)
                """, (message['Date'], message['Info'], message['Application'], message['Action']))

    conn.commit()
    conn.close()
