import sqlite3


class SQLiteAdapter:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name, check_same_thread=False)

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

    def upsert_into(self, conflict_col, table, values, updating_cols):
        '''
        This method INSERT values into a table or updates if values already exist
        :param conflict_col: takes column where you want to check a conflict
        :param table: table name
        :param values: data you want to insert
        :param updating_cols: columns you want to update in case if data already exist
        :return: True
        '''
        updating_cals = ', '.join([f'{i}=excluded.{i}' for i in updating_cols])
        query = f'INSERT INTO {table} ' \
                f'VALUES {values}' \
                f'ON CONFLICT ({conflict_col}) DO UPDATE SET ' \
                f'{updating_cals}'
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


