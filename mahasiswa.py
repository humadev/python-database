from database import connection


def getMahasiswa() :
    cursor = connection.cursor()

    cursor.execute("select*from Mahasiswa")

    for data in cursor :
        print(data)

    mahasiswaRun = True

    while mahasiswaRun == True :
        print("ketik nim untuk melihat studi")
        print("ketik back untuk kembali ke menu utama")
        pilihan = input()

        if pilihan == 'back' :
            mahasiswaRun = False
        else :
            getStudi(pilihan)


def getStudi(nim) :
    studi = connection.cursor()

    studi.execute("select*from Studi where mahasiswaId in (select id from Mahasiswa where nim=%s)" % (nim))

    for data in studi:
        print(data)


def addMahasiswa() :
    nim = input("masukan nim: ")
    nama = input("masukkan nama: ")

    studi = connection.cursor()

    studi.execute(
        "INSERT INTO Mahasiswa SET nim='%s', nama='%s'" % (nim, nama))

    connection.commit()

    print("data mahasiswa tersimpan")
    addMahasiswaRun = True

    while addMahasiswaRun == True:
        print("tambah data lagi? (y/n)")
        pilihan = input()

        if pilihan == 'y':
            addMahasiswa()
        else:
            addMahasiswaRun = False


