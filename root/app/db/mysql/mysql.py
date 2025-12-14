import logging
from typing import Tuple, Dict, Union

import mysql.connector as mysql_connector
from mysql.connector import pooling, cursor, errors

from setting import DATABASE_CONFIG_MYSQL 

class MySQL:
    __is_exist: bool = False
    __instance: "MySQL" = None
    __config: Dict = DATABASE_CONFIG_MYSQL

    def __new__(cls, *args, **kwargs):
        if not cls.__is_exist:
            cls.__instance = super().__init__(args, kwargs)
        return cls.__instance
    
    def __init__(self):
        if  self.__is_exist:
            return
        else:
            self.__is_exist = True

        self.__pool = pooling.MySQLConnectionPool(**self.__config)

    def __get_connection_from_pool(self) -> Tuple[pooling.PooledMySQLConnection, cursor.MySQLCursor]:
        try:
            cnx = self.__pool.get_connection()
            cursor = cnx.cursor()
            return cnx, cursor 
        except errors.PoolError as mysql_error:
            logging.error("CODE:MySQL. Error receiving a connection from the pool", mysql_error)
            raise mysql_error
    
    def query(self, sql: str, params: Union[Dict, Tuple] = None) -> Union[Dict, Tuple, None]:
        cnx, cursor = self.__get_connection_from_pool()

        try:
            cursor.execute(sql, params)
            return cursor.fetchall()
        except mysql_connector.Error as mysql_error:
            logging.error("CODE: MySQL. Query execution error: ", mysql_error)
            raise
        finally:
            cursor.close()
            cnx.close()

    def execute(self, sql: str, params: Union[Dict, Tuple] = None) -> None:
        cnx, cursor = self.__get_connection_from_pool()

        try:
            cursor.execute(sql, params)
            cnx.commit()
        except mysql_connector.Error as mysql_error:
            logging.error("CODE: MySQL. Query(execute) execution error: ", mysql_error)
            raise
        finally:
            cursor.close()
            cnx.close()