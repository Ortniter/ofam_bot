import pymysql


class MySQLAdapter:
    def __init__(self, db_name):
        self.connection = pymysql.connect(host='ortniter.mysql.pythonanywhere-services.com',
                                          user='ortniter',
                                          password='PikachuIsHere',
                                          db=db_name)

    def select_all(self, table):
        query = f"select * from {table}"
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def select_from(self, table, columns, where):
        """
        Incapsulates SELECT query to SQLite
        :table: table name
        :columns: string with columns to get
        :where: dict of columns and data
        """
        where = ' AND '.join([f"{i[0]}=\'{i[1]}\'" for i in where.items()])
        query = f"SELECT {columns} " \
                f"FROM {table} " \
                f"WHERE {where};"
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def insert_into(self, table, values):
        query = f"INSERT INTO {table} " \
                f"VALUES {values}"
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        return True

    def upsert_into(self, values, table):
        """
        This method INSERT values into a table or updates if values already exist
        :param values: data you want to insert
        :param table: table name
        :return: True
        """
        query = f'REPLACE INTO {table} VALUES {values};'
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        return True

    def create_table(self, table, cols):
        """
        This method creates a new table with columns if it doesn't exist
        :param table: table name
        :param cols: columns you want to create
        :return: True
        """
        cols_str = ', '.join(cols)
        query = f'CREATE TABLE {table} ({cols_str})'
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
        finally:
            return True
