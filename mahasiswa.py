from models.studi import Studi
from models.mahasiswa import Mahasiswa

tableMahasiswa = Mahasiswa()
tableStudi = Studi()

def getMahasiswa() :
    for data in tableMahasiswa.getAll() :
        print(data)

    mahasiswaRun = True

    while mahasiswaRun == True :
        print("ketik 'id mahasiswa' untuk melihat studi mahasiswa")
        print("ketik back untuk kembali ke menu utama")
        pilihan = input()

        if pilihan == 'back' :
            mahasiswaRun = False
        else :
            getStudi(pilihan)


def getStudi(idMahasiswa) :
    studi = tableStudi.getByMahasiswa(idMahasiswa)

    print("Studi Mahasiswa :")
    for data in studi:
        print(data)


def addMahasiswa() :
    nim = input("masukan nim: ")
    nama = input("masukkan nama: ")

    tableMahasiswa.insert(nim, nama)

    print("data mahasiswa tersimpan")
    addMahasiswaRun = True

    while addMahasiswaRun == True:
        print("tambah data lagi? (y/n)")
        pilihan = input()

        if pilihan == 'y':
            addMahasiswa()
        else:
            addMahasiswaRun = False


def editMahasiswa():
    for data in tableMahasiswa.getAll():
        print(data)

    id = input("masukan id mahasiswa: ")
    nim = input("masukan nim: ")
    nama = input("masukkan nama: ")

    tableMahasiswa.update(id, nim, nama)

    print("data mahasiswa diperbaharui")
    addMahasiswaRun = True

    while addMahasiswaRun == True:
        print("edit data lagi? (y/n)")
        pilihan = input()

        if pilihan == 'y':
            editMahasiswa()
            addMahasiswaRun = False
        else:
            addMahasiswaRun = False


def deleteMahasiswa():
    for data in tableMahasiswa.getAll():
        print(data)

    id = input("masukan id mahasiswa yang ingin dihapus: ")
    
    tableMahasiswa.delete(id)

    print("data mahasiswa dihapus")
    addMahasiswaRun = True

    while addMahasiswaRun == True:
        print("hapus data lagi? (y/n)")
        pilihan = input()

        if pilihan == 'y':
            deleteMahasiswa()
            addMahasiswaRun = False
        else:
            addMahasiswaRun = False
