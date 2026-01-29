from root.db.mysql import MySQL

db_config = {
    "host": "127.0.0.1",
    "port": 3306,
    "database": "hackaton_2.0",
    "user": "root",
    "password": "root"
}

mysql = MySQL(db_config)