# pip install psycopg2
import psycopg2  # это адаптер базы данных PostgreSQL для Python
from sqlite3 import Error
import sqlite3
from abc import ABC, abstractmethod


class DataClient(ABC):
    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def create_mebel_table(self, conn):
        pass

    @abstractmethod
    def get_items(self, conn, price_from=0, price_to=10000):
        pass

    @abstractmethod
    def insert(self, conn, link, price, description):
        pass

    def run_test(self):
        conn = self.get_connection()
        self.create_mebel_table(conn)
        items = self.get_items(conn, price_from=10, price_to=30)
        for item in items:
            print(item)
        conn.close()


class PostgresClient(DataClient):
    USER = 'postgres'
    PASSWORD = 'postgres'
    HOST = 'localhost'
    PORT = '5432'

    def get_connection(self):
        try:
            connection = psycopg2.connect(
                user=self.USER,
                password=self.PASSWORD,
                host=self.HOST,
                port=self.PORT
            )
            return connection
        except Error:
            print(Error)

    def create_mebel_table(self, conn):
        cursor_object = conn.cursor()
        cursor_object.execute(
            """
                CREATE TABLE IF NOT EXISTS app1_mebel
                (
                    id serial PRIMARY KEY,
                    link text,
                    price integer,
                    description text
                )
    
            """
        )
        conn.commit()

    def get_items(self, conn, price_from=0, price_to=10000):
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM app1_mebel WHERE price >= {price_from} and price <= {price_to}')
        return cursor.fetchall()  # fetchall() возвращает результаты запроса в виде списка кортежей, в котором каждый
    # кортеж содержит одну строку данных из результатов запроса

    def insert(self, conn, link, price, description):
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO app1_mebel (link, price, description) VALUES ('{link}', '{price}', '{description}')")
        conn.commit()


class Sqlite3Client(DataClient):
    DB_Name = 'kufar.db'

    def get_connection(self):
        try:
            conn = sqlite3.connect(self.DB_Name)
            return conn
        except Error:
            print(Error)

    def create_mebel_table(self, conn):
        cursor_object = conn.cursor()
        cursor_object.execute(
            """
                CREATE TABLE IF NOT EXISTS app1_mebel
                (
                    id integer PRIMARY KEY autoincrement,
                    link text,
                    price integer,
                    description text
                )

            """
        )
        conn.commit()

    def get_items(self, conn, price_from=0, price_to=10000):
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM app1_mebel WHERE price >= {price_from} and price <= {price_to}')
        return cursor.fetchall()  # fetchall() возвращает результаты запроса в виде списка кортежей, в котором каждый
        # кортеж содержит одну строку данных из результатов запроса

    def insert(self, conn, link, price, description):
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO app1_mebel (link, price, description) VALUES ('{link}', '{price}', '{description}')")
        conn.commit()


data_client = PostgresClient()
#data_client = Sqlite3Client()
data_client.run_test()

