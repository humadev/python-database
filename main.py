from mahasiswa import addMahasiswa, getMahasiswa

def display() :
    programRun = True
    while programRun == True :
        print("1. tampilkan data mahasiswa")
        print("2. tambah data mahasiswa")
        print("3. edit data mahasiswa")
        print("4. hapus data mahasiswa")
        print("ketik exit untuk menghentikan program")
        pilihan = input()

        if pilihan == '1' :
            getMahasiswa()
        if pilihan == '2' :
            addMahasiswa()
        elif pilihan == 'exit' :
            programRun = False


display()
