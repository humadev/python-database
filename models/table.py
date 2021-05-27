
from models.database import Connection


class Table(Connection):

    def __init__(self, table, key):
        self.table = table
        self.key = key

    def get(self, id):
        connection = self.connection()
        cursor = connection.cursor()
        cursor.execute("select*from %s WHERE %s=%s" % (self.table, self.key, id))

        data = cursor.fetchone()
        connection.close()
        return data

    def getAll(self):
        connection = self.connection()
        cursor = connection.cursor()
        cursor.execute("select*from %s" % (self.table))
        
        data = cursor.fetchall()
        connection.close()
        return data

    def delete(self, id):
        connection = self.connection()
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM %s WHERE %s=%s" % (self.table, self.key, id))
        connection.commit()

        data = cursor
        connection.close()
