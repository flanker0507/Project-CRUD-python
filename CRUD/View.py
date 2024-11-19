from . import Operasi

def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data Buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("tahun harus angka, silahkan masukkan angka lagi (yyy)")
        except:
            print("tahun harus angka, silahkan masukkan angka lagi (yyy)")


    Operasi.create(tahun,judul,penulis)
    print("\nBerikut adalah data baru anda")
    read_console()

def read_console():
    data_file = Operasi.read()

    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    #Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("\n"+"-"*100)

    #Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:5}",end="")

    #Footer
    print("\n"+"="*100+"\n")

def update_console():
    read_console()
    while(True):
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("nomor tidak valid, silahkan masukkan lagi")

    data_break = data_buku.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while(True):
        # data yang ingin di update
        print("\n"+"="*100)
        print("Silahkan Pilih data apa yang mau di Update ")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # memilih mode untuk update
        user_option = input("Pili Data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3":
                while (True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("tahun harus angka, silahkan masukkan angka lagi (yyy)")
                    except:
                        print("tahun harus angka, silahkan masukkan angka lagi (yyy)")

            case _: print("index  tidak cocok")

        print("Data Baru Anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        is_done = input("Apakah Sudah Selesai Update (y/n)")
        if is_done.lower() == "y":
            break

    Operasi.update(no_buku,pk,date_add,penulis,judul,tahun)





