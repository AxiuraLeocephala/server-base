from typing import Dict, List, Union, Tuple

import mysql.connector as mysql_connector
from mysql.connector import errorcode
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.cursor import MySQLCursor

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

        try:
            self.__cnx_pool = mysql_connector.pooling.MySQLConnectionPool(**db_config)
        except mysql_connector.Error as connection_error:
            if connection_error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise "Something is wrong with your user name or password"
            elif connection_error.errno == errorcode.ER_BAD_DB_ERROR:
                raise "Database does not exist"
            else:
                raise connection_error

    def __get_connection(self) -> Tuple[PooledMySQLConnection, MySQLCursor]:
        # TODO: сделать круговую очередь или алгоритм планирования,
        # чтобы не возникала ошибка PoolError
        try:
            cnx = self.__cnx_pool.get_connection()
            cursor = cnx.cursor(dictionary=True)
            return cnx, cursor
        except mysql_connector.errors.PoolError as pool_error:
            raise pool_error

    async def execute(self, sql: str, params: Union[Tuple, Dict] = None) -> Union[int, None]:
        cnx, cursor = self.__get_connection()
        try:
            cursor.execute(operation=sql, params=params)
            cnx.commit()
            return cursor.lastrowid
        except mysql_connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()

    async def query(self, sql: str, params: Union[Tuple, Dict] = None) -> Union[Tuple, List, None]:
        cnx, cursor = self.__get_connection()
        try:
            cursor.execute(operation=sql, params=params)
            return cursor.fetchall()
        except mysql_connector.Error as mysql_error:
            raise mysql_error
        finally:
            cursor.close()
            cnx.close()