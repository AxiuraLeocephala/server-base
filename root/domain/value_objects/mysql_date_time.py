from datetime import datetime

class MySQLDateTime:
    FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, value: str):
        self.value = datetime.strptime(value, self.FORMAT)

class MySQLDate(MySQLDateTime):
    FORMAT = "%Y-%m-%d"