import logging
from typing import Dict, Union, Tuple

import mysql.connector as mysql_connector
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.cursor import MySQLCursor
from mysql.connector.errors import PoolError

from root.application.interfaces import DBInterface

class MySQL(DBInterface):
    __instance: "MySQL" = None
    __is_exist: bool = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db_config: Dict):
        if self.__is_exist:
            return
        self.__is_exist = True
        self.__cnx_pool = mysql_connector.pooling.MySQLConnectionPool(**db_config)

    def __get_connection(self) -> Tuple[PooledMySQLConnection, MySQLCursor]:
        # TODO: сделать круговую очередь или алгоритм планирования, 
        # чтобы не возникала ошибка PoolError
        try:
            cnx = self.__cnx_pool.get_connection()
            cursor = cnx.cursor()
            return cnx, cursor
        except PoolError as pool_error:
            raise pool_error

    async def execute(self, sql: str, params = None) -> None:
        cnx, cursor = self.__get_connection()
        try:
            cursor.execute(operation=sql, params=params)
            cnx.commit()
        except mysql_connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()

    async def query(self, sql: str, params = None) -> Union[Tuple, Dict, None]:
        cnx, cursor = self.__get_connection()
        try:
            cursor.execute(operation=sql, params=params)
        except mysql_connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()