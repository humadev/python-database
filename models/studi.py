
from models.table import Table


class Studi(Table):

    def __init__(self):
        table = 'Studi'
        key = 'id'
        super().__init__(table, key)

    def getByMahasiswa(self, idMahasiswa):
        connection = self.connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT*FROM Studi WHERE mahasiswaId = %s" % (idMahasiswa))
        
        data = cursor.fetchall()
        connection.close()
        return data;

    def insert(self, idMahasiswa, nama, nilaiAngka, angkaMutu, hurufMutu):
        connection = self.connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Studi SET mahasiswaId=%s, nama='%s', nilaiAngka='%s', angkaMutu='%s', hurufMutu='%s'" % (idMahasiswa, nama, nilaiAngka, angkaMutu, hurufMutu))
        connection.commit()

        data = cursor
        connection.close()

    def update(self, id, idMahasiswa, nama, nilaiAngka, angkaMutu, hurufMutu):
        connection = self.connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE Mahasiswa SET mahasiswaId=%s, nama='%s', nilaiAngka='%s', angkaMutu='%s', hurufMutu='%s' WHERE id=$s" % (idMahasiswa, nama, nilaiAngka, angkaMutu, hurufMutu, id))
        connection.commit()

        data = cursor
        connection.close()
