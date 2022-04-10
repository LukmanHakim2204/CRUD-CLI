import psycopg2
#Connect Database
conn = psycopg2.connect(
         host="localhost",
         database="kampuskuumc",
         user="lukman",
         password="1234")

#Menyimpan Data Baru
def insert_data(conn):
   nim = input("Masukkan NIM Mahasiswa: ")
   nama = input("Masukkan Nama Mahasiswa: ")
   idfakultas = int(input("Masukkan ID Fakultas Mahasiswa: "))
   idprodi = int(input("Masukkan ID Prodi: "))
   val = (nim,nama,idfakultas,idprodi)
   sql = "INSERT INTO mahasiswaumc (nim, nama, idfakultas, idprodi) VALUES ( %s, %s, %s, %s)"
   cur = conn.cursor()
   cur.execute(sql, val)
   conn.commit()
   print("==================================")
   print("{} Data Berhasil Disimpan".format(cur.rowcount))

#Menampilkan Data
def show_data(conn):
   cur = conn.cursor()
   sql = "SELECT * FROM mahasiswaumc"
   cur.execute(sql)
   result = cur.fetchall()

   if cur.rowcount < 0:
      print("==================================")
      print("DATA ANDA TIDAK ADA ATAU BELUM TERISI")
   else:
      print("==================================")
      print("-{} DATA BERHASIL DITEMUKAN".format(cur.rowcount))
      for data in result:
         print(data)

#Update Data
def update_data(conn):
   cur = conn.cursor()
   show_data(conn)
   nimhs = input("Silahkan Pilih Nim Mahasiswa Yang Akan Di Ubah: ")
   nim = input("Masukkan NIM Mahasiswa yang Baru: ")
   nama = input("Masukkan Nama Mahasiswa Yang Baru: ")
   idfakultas = int(input("Masukkan Id Fakultas yang Baru: "))
   idprodi = int(input("Masukkan Id Prodi Yang Baru: "))
   sql = "UPDATE mahasiswaumc SET nim=%s, nama=%s, idfakultas=%s, idprodi=%s WHERE nim=%s"
   val = (nim, nama, idfakultas, idprodi, nimhs)
   cur.execute(sql, val)
   conn.commit()
   print("==================================")
   print("{} Data Berhasil Diupdate".format(cur.rowcount))

#Menghapus Data
def delete_data(conn):
   cur = conn.cursor()
   show_data(conn)
   idmhs = input("Pilih ID Mahasiswa Yang Akan Dihapus: ")
   sql = "SELECT * FROM mahasiswaumc WHERE idmhs='"+idmhs+"'"
   cur.execute(sql)
   con = cur.rowcount
   if (con == 1):
      inp = input("Apakah Anda Ingin Menghapus Data Tersebut? (y/t): ")
      if (inp.upper()=="Y"):
         sql = "DELETE FROM mahasiswaumc WHERE idmhs='"+idmhs+"'"
         cur.execute(sql)
         conn.commit()
         print("="*20)
         print("\b{} DATA BERHASIL DIHAPUS".format(cur.rowcount))
      else:
         print("DATA TIDAK BERHASIL DIHAPUS")
   else:
      print("TIDAK ADA NIM YANG DIMAKSUD")

#Mencari Data
def search_data(conn):
   cur = conn.cursor()
   keyword = input("Masukkan NIM ATAU NAMA DATA YANG DICARI: ")
   sql = "SELECT * FROM mahasiswaumc WHERE nim LIKE %s OR nama LIKE %s OR nama LIKE %s OR nama LIKE %s"
   val = ("%{}%".format(keyword), "%{}%".format(keyword.lower()),"%{}%".format(keyword.upper()),"%{}%".format(keyword.title()))
   cur.execute(sql, val)
   result = cur.fetchall()

   if cur.rowcount <= 0:
      print("==================================")
      print("TIDAK ADA DATA YANG DIMAKSUD")
   else:
      print("==================================")
      print("{} DATA YANG DIMAKSUD BERHASIL DITEMUKAN".format(cur.rowcount))
      for data in result:
         print(data)

#Menampilkan Menu
def show_menu(conn):
   print("---------------------------------------------")
   print("|    TUGAS 1 PEMBUATAN CRUD BERBASIS CLI    |")
   print("---------------------------------------------")
   print("|1. Tambah Data                             |")
   print("|2. Menampilkan Data                        |")
   print("|3. Memperbarui Data                        |")  
   print("|4. Menghapus Data                          |")
   print("|5. Mencari Data                            |")
   print("|0. Keluar                                  |")
   print("---------------------------------------------")
   menu = input("Silahkan Pilih Menu : ")

   if menu == "1":
      insert_data(conn)
   elif menu == "2":
      show_data(conn)
   elif menu == "3":
      update_data(conn)
   elif menu == "4":
      delete_data(conn)
   elif menu == "5":
      search_data(conn)
   elif menu == "0":
      exit()
   else:
      print("Menu Yang Anda Masukkan Tidak Tersedia")

#Looping
if __name__ == "__main__":
   while(True):
      show_menu(conn)