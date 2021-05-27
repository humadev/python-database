
from models.table import Table


class Mahasiswa(Table) :

    def __init__(self):
        table = 'Mahasiswa'
        key = 'id'
        super().__init__(table, key)

    def insert(self, nim, nama):
        connection = self.connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Mahasiswa SET nim='%s', nama='%s'" % (nim, nama))
        connection.commit()

        data = cursor
        connection.close()

    def update(self, id, nim, nama):
        connection = self.connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE Mahasiswa SET nim='%s', nama='%s' WHERE id=%s" % (nim, nama, id))
        connection.commit()

        data = cursor
        connection.close()
