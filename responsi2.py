# import waktu
import datetime
sekarang = datetime.datetime.now()


#  admin
# berikut adalah ID dan password untuk masuk sebagai admin penjual yang sudah tersimpan di database
import sqlite3
with sqlite3.connect("konter.db") as db:
    cursor = db.cursor()

# pembuatan table admin dan table pembelian
cursor.execute(""" CREATE TABLE IF NOT EXISTS admin(id integer PRIMARY KEY, password text NOT NULL); """)
cursor.execute(""" CREATE TABLE IF NOT EXISTS pembelian(nama text, nomor integer, pembelian_pulsa integer, harga_pulsa integer, uang_pembayaran integer, uang_kembalian integer, waktu_pembelian text); """)

# pengisian tabel admin
cursor.execute(""" INSERT or ignore INTO admin(id, password) VALUES(2003, "taman langit")""")
cursor.execute(""" INSERT or ignore INTO admin(id, password) VALUES(2004, "bintang di surga")""")
cursor.execute(""" INSERT or ignore INTO admin(id, password) VALUES(2007, "hari yang cerah")""")
cursor.execute(""" INSERT or ignore INTO admin(id, password) VALUES(2012, "seperti seharusnya")""")
cursor.execute(""" INSERT or ignore INTO admin(id, password) VALUES(2019, "keterkaitan keterikatan")""")

db.commit()

# pulsa basic, sebelum diedit oleh admin. Hal ini dibutuhkan ketika pengujian program langsung memilih menu no.2 yaitu pembelian, agar pembelian tidak kosong dan tetap bisa dilakukan
hargaPulsa = [7000, 27000, 52000, +2000]
nominalPulsa = (5000, 25000, 50000)

# function Admin
def pengecekanAdmin():
    # login admin
    login = "y"
    while login == "y":
        print("\n\n=====================================")
        print("Selamat Datang di Konter")
        cekIdAdmin = int(input("Silahkan masukan id admin anda : "))
        cekPasswordAdmin = input("Silahkan masukan password admin anda : ")
        print("=====================================")

        # Select database admin, kolom id
        selectId = "SELECT id FROM admin"
        cursor.execute(selectId)
        resultsId = cursor.fetchall()
        
        # Select database admin, kolom password
        selectPassword = "SELECT password FROM admin"
        cursor.execute(selectPassword)
        resultsPassword = cursor.fetchall()

        # validasi login admin
        if (cekIdAdmin == resultsId[0][0] and cekPasswordAdmin == resultsPassword[0][0] or cekIdAdmin == resultsId[1][0] and cekPasswordAdmin == resultsPassword[1][0] or cekIdAdmin == resultsId[2][0] and cekPasswordAdmin == resultsPassword[2][0] or cekIdAdmin == resultsId[3][0] and cekPasswordAdmin == resultsPassword[3][0]) or cekIdAdmin == resultsId[4][0] and cekPasswordAdmin[4][0]:
            # login berhasil
            print("\n=====================================")
            print("login berhasil")
            print("=====================================\n")


            # membuat harga pulsa
            print("=====================================")
            print("Silahkan masukan harga pulsa")
            harga1 = int(input("masukan harga pulsa 5000 : Rp "))
            harga2 = int(input("masukan harga pulsa 25000 : Rp "))
            harga3 = int(input("masukan harga pulsa 50000 : Rp "))
            harga4 = int(input("masukan keuntungan pulsa untuk isi nominal sendiri : Rp "))
            hargaPulsa[0] = harga1
            hargaPulsa[1] = harga2
            hargaPulsa[2] = harga3
            hargaPulsa[3] = +harga4
            print("=====================================")
            looping = "y"
            while looping == "y":
                # menu admin
                print("\n\n=====================================")
                print("Silahkan memilih menu")
                print("1. melihat banyak pembeli")
                print("2. data transaksi ")
                print("3. edit harga pulsa")
                print("4. perhitungan pulsa (berdasar database)")
                print("5. Perhitungan harian, mingguan, tahunan")
                print("0. Keluar")
                pilihMenu = int(input("pilih sesuai angka : "))
                print("=====================================")

                # jika memilih menu1
                if(pilihMenu == 1):
                    # Select tabel pembelian, kolom nama
                    selectPembeli = "Select nama from pembelian"
                    cursor.execute(selectPembeli)
                    resultsPembeli = cursor.fetchall()

                    # menghitung banyak pembeli yang ada di database
                    print("\n=====================================")
                    print("Banyak Pembeli (berdasarkan database) adalah : ", len(resultsPembeli))

                    # menampilkan pembeli yang ada pada database
                    print("Nama Pembeli : ")
                    for you in range(len(resultsPembeli)):
                        print(resultsPembeli[you][0])
                    looping == "y"
                    print("=====================================")

                # jika memilih menu2
                elif(pilihMenu == 2):
                    # Select semua dara yang ada pada database di tabel pembelian
                    print("\n=====================================")
                    print("data transaksi")
                    cursor.execute("SELECT * FROM pembelian")
                    for x in cursor.fetchall():
                        print(x)
                    looping == "y"
                    print("=====================================")


                # Jika memilih menu3
                elif(pilihMenu == 3):
                    # menu pada pilihan nomor 3, yaitu untuk mengedit harga pulsa yang ada
                    print("\n\n=====================================")
                    print("Mengubah harga pulsa")
                    print("pilihan nominal isi pulsa")
                    print("1. pulsa 5000, harga Rp", hargaPulsa[0])
                    print("2. pulsa 25000, harga Rp", hargaPulsa[1])
                    print("3. pulsa 50000, harga Rp", hargaPulsa[2])

                    # nominal sendiri adalah si pembeli mengisi nominal pulsa yang di inginkan. jadi si admin tidak menentukan harganya, tetapi menentukan keuntungan dari nominal yang diisikan oleh pembeli tersebut
                    print("4. isi nominal sendiri, harga = nominal pulsa + Rp", hargaPulsa[3])
                    pilihNominal = int(input("pilih nomor untuk mengubah harga pulsa : "))
                    print("=====================================")

                    # memilih pulsa yang akan diubah harganya
                    # jika ingin mengganti harga pulsa nomor1
                    if (pilihNominal == 1):
                        print("\n=====================================")
                        hargaPulsaBaru = int(input("Silahkan masukan harga pulsa yang baru : Rp "))
                        print("berhasil diubah")
                        print("Pulsa 5000, harga Rp", hargaPulsaBaru)
                        hargaPulsa[0] = hargaPulsaBaru
                        print("=====================================")

                    # jika ingin mengganti harga pulsa nomor2
                    elif (pilihNominal == 2):
                        print("\n\n=====================================")
                        hargaPulsaBaru = int(input("Silahkan masukan harga pulsa yang baru : Rp "))
                        print("berhasil diubah")
                        print("Pulsa 25000, harga Rp ", hargaPulsaBaru)
                        hargaPulsa[1] = hargaPulsaBaru
                        print("=====================================")
                    
                    # jika ingin mengganti harga pulsa nomor3
                    elif (pilihNominal == 3):
                        print("\n\n=====================================")
                        hargaPulsaBaru = int(input("Silahkan masukan harga pulsa yang baru : Rp "))
                        print("berhasil diubah")
                        print("Pulsa 50000, harga Rp", hargaPulsaBaru)
                        hargaPulsa[2] = hargaPulsaBaru
                        print("=====================================")

                    # jika ingin mengganti harga pulsa nomor4
                    elif (pilihNominal == 4):
                        print("\n\n=====================================")
                        untung = int(input("masukan keuntungan pulsa yang baru : Rp "))
                        print("berhasil diubah")
                        hargaPulsaBaru = + untung
                        print("Harga pulsa yang di isi nominal sendiri adalah nominal pulsa ditambah keuntungan dari pulsa yaitu Rp", untung)
                        hargaPulsa[3] = hargaPulsaBaru
                        print("=====================================")

                    looping == "y"
                # jika memilih menu no.0
                elif (pilihMenu == 0):
                    looping = "t"
                    return looping
                # jika memilih menu no.4
                elif (pilihMenu == 4):
                    print("=====================================")
                    saldo = int(input("masukan total saldo pulsa : "))
                    modal = int(input("masukan modal pembelian saldo : Rp "))

                    # select kolom pembelian_pulsa pada tabel pembelian dalam database
                    selectPembelianPulsa = "Select pembelian_pulsa from pembelian"
                    cursor.execute(selectPembelianPulsa)
                    resultsPembelianPulsa = cursor.fetchall()
                    total = 0

                    # untuk menjumlah semua pemasukan yang masuk ke dalam database
                    for you in range(len(resultsPembelianPulsa)):
                        total = total + resultsPembelianPulsa[you][0]
                    print("=====================================")
                    print("Total Pendapatan Konter (sesuai data yang ada pada database) : Rp", total)
                    print("=====================================")

                    if (total >= modal):
                        print("=====================================")
                        untung = total - modal
                        print("Keuntungan anda sebesar : Rp", untung)
                        print("=====================================")
                    elif (total < modal):
                        print("=====================================")
                        rugi = total - modal
                        print("Kerugian anda sebesar : Rp", rugi)
                        print("=====================================")


                # jika memilih menu no.5
                elif (pilihMenu == 5):
                    print("\n=====================================")
                    print("Perhitungan sehari")
                    int(input("input banyaknya orang yang membeli dalam sehari :"))
                    pemasukanSehari = int(input("input pemasukan dalam sehari : Rp "))
                    modalSehari = int(input("input modal perhari : Rp "))
                    if (modalSehari <= pemasukanSehari):
                        print("anda untung sebesar Rp", pemasukanSehari - modalSehari)
                    elif(modalSehari > pemasukanSehari):
                        print("anda rugi sebesar Rp", pemasukanSehari - modalSehari)
                    print("=====================================")

                    print("\n=====================================")
                    print("Perhitungan seminggu")
                    int(input("input banyaknya orang yang membeli dalam sehari : "))
                    pemasukanSeminggu = int(input("input pemasukan dalam seminggu : Rp "))
                    modalSeminggu = int(input("input modal perminggu : Rp "))
                    if (modalSeminggu <= pemasukanSeminggu):
                        print("anda untung sebesar Rp", pemasukanSeminggu - modalSeminggu)
                    elif(modalSeminggu > pemasukanSeminggu):
                        print("anda rugi sebesar Rp", pemasukanSeminggu - modalSeminggu)
                    print("=====================================")

                    print("\n=====================================")
                    print("Perhitungan sebulan")
                    int(input("input banyaknya orang yang membeli dalam sebulan : "))
                    pemasukanSebulan = int(input("input pemasukan dalam sebulan : Rp "))
                    modalSebulan = int(input("input modal perminggu : Rp "))
                    if (modalSebulan <= pemasukanSebulan):
                        print("anda untung sebesar Rp", pemasukanSebulan - modalSebulan)
                    elif(modalSebulan > pemasukanSebulan):
                        print("anda rugi sebesar Rp", pemasukanSebulan - modalSebulan)
                    print("=====================================")
            login = "t"
        else:
            print("=====================================")
            print("Id admin atau password yang anda masukan salah")
            print("Silahkan mengulangi !!!")
            login = "y"
            print("=====================================")


# function pembelian
def pembelian():
    print("\n\n=====================================")
    print("Selamat Datang di konter")
    nama = input("masukan nama anda : ")
    nomor = int(input("masukan nomor telepon anda : "))
    print("=====================================")
    print("\n\nSilahkan memilih nominal isi pulsa anda")
    print("1. 5000, harga Rp",hargaPulsa[0])
    print("2. 25000, harga Rp", hargaPulsa[1])
    print("3. 50000, harga Rp", hargaPulsa[2])
    print("4. isi nominal sendiri")
    pilihPulsa = int(input("pilih sesuai angka : "))
    print("=====================================")
    if (pilihPulsa == 1):
        print("=====================================")
        print("anda membeli pulsa", nominalPulsa[0], ", harga Rp", hargaPulsa[0])
        data = (nama, nomor, nominalPulsa[0], hargaPulsa[0])
        print("=====================================")
        return data

    elif (pilihPulsa == 2):
        print("=====================================")
        print("anda membeli pulsa", nominalPulsa[1], ", harga Rp", hargaPulsa[1])
        data = (nama, nomor, nominalPulsa[1], hargaPulsa[1])
        print("=====================================")
        return data


    elif (pilihPulsa == 3):
        print("=====================================")
        print("anda membeli pulsa", nominalPulsa[2], ", harga Rp", hargaPulsa[2])
        data = (nama, nomor, nominalPulsa[2], hargaPulsa[2])
        print("=====================================")
        return data
        
    elif (pilihPulsa == 4):
        print("=====================================")
        isiNominal = int(input("input nominal pulsa yang ingin anda isi : "))
        hargaIsiNominal = hargaPulsa[3] + isiNominal
        print("anda membeli pulsa", isiNominal, ", harga Rp", hargaIsiNominal)
        data = (nama, nomor, isiNominal, hargaIsiNominal)
        print("=====================================")
        return data
        
    return data

# function struk
def struk(x):
    ulang = "y"
    while ulang == "y":
        bayar = int(input("\nmasukan uang pembayaran anda : Rp "))
        if (bayar >= x[3]):
            kembalian = bayar - x[3]  
            ulang = "t"
        elif (bayar < x[3]):
            print("uang anda kurang")
            ulang = "y"

    print("\n\n=====================================")
    print("======STRUK PEMBAYARAN=======")
    print("=====================================")
    print("Nama pembeli :", x[0])
    print("Nomor Kartu :", x[1])
    print("Pembelian : Pulsa", x[2], ",harga Rp",x[3])
    print("Uang Pembayaran : Rp", bayar)
    print("Uang Kembalian : Rp", kembalian)
    print("=====================================")
    print("    ",sekarang)
    print("=====================================")

# mengisi database tabel pembelian dengan informasi yang telah dilakukan pada function pembelian() dan yang sudah tercetak pada struk
    cursor.execute(""" INSERT INTO pembelian(nama, nomor, pembelian_pulsa, harga_pulsa, uang_pembayaran, uang_kembalian, waktu_pembelian) VALUES(?,?,?,?,?,?,?)""", (x[0], x[1], x[2], x[3], bayar, kembalian, sekarang))
    db.commit()


def main():
    ulang = "t"
    while ulang == "t":
        print("\n\n=====================================")
        print("Halo Selamat Datang")
        print("Silahkan pilih menu berikut ini")
        print("1. Admin Konter")
        print("2. Pembeli")
        pilihLogin = int(input("masukan angka pilihan anda : "))
        print("=====================================")
        if (pilihLogin == 1):
            returnPengecekanAdmin = pengecekanAdmin()
            ulang = returnPengecekanAdmin
        if (pilihLogin == 2):
            returnPembelian = pembelian()
            struk(returnPembelian)
            ulang = input("Apakah ingin membeli lagi ? <y/t>")
            if ulang == "y":
                ulang = "t"
            elif ulang == "t":
                ulang = "y"
            
            

main()