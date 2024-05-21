def data_buku():
	data= {}
	try:
		with open("data_buku8.txt", 'r') as f:
			for baris in f:
				nilai=baris.strip().split('|')
				if len(nilai) == 4:
					judul, penulis, penerbit, tahun = nilai
					data[judul.strip()] ={
					'judul' : judul.strip(),
					'penulis' : penulis.strip(),
					'penerbit' : penerbit.strip(),
					'tahun terbit' : tahun.strip()
					}
	except FileNotFoundError:
		pass
	return data

def simpan_data(data):
	with open("data_buku8.txt", 'w') as f:
		for judul, value in data.items():
			f.write(f"{judul :<20} | {value['penulis']:<20} | {value['penerbit']:<20} | {value['tahun terbit']:<10} | \n")

def tambah_buku(data):
	judul = input("masukkan judul buku: ")
	penulis = input("masukkan nama penulis: ")
	penerbit = input("masukkan nama penerbit: ")
	tahun = input("masukkan tahun terbit: ")
	data[judul] = {
	'penulis' : penulis,
	'penerbit' : penerbit,
	'tahun terbit' : tahun
	}
	simpan_data(data)
	print("data buku berhasil di tambah")
      
def hapus_buku(data):
    judul = input("masukkan judul buku yang ingin di hapus: ")
    if judul in data:
        del data[judul]
        simpan_data(data)
        print("data buku berhasil di hapus")
    else:
        print("judul buku yg diinput tidak ada dalam data")

def tampil_buku(data):
    if not data:
        print("Tidak ada data buku yang tersimpan.")
    else:
        print("\n***** Data Buku *****")
        for judul, value in data.items():
            print(f"Judul: {judul}")
            print(f"Penulis: {value['penulis']}")
            print(f"Penerbit: {value['penerbit']}")
            print(f"Tahun Terbit: {value['tahun terbit']}")
            print("-------------------")
    
def pilih_menu(): 	
    print("\n****** Menu *******")
    print("1. Menambah Data Buku")
    print("2. Menghapus Data Buku")
    print("3. Menampilkan Data Buku")
    print("4. Keluar dari program")

def main():
    data = data_buku()
    while True:
        pilih_menu()
        pilih = input("Pilih menu (1/2/3/4): ")
        if pilih == '1':
            tambah_buku(data)
        elif pilih == '2':
            hapus_buku(data)
        elif pilih == '3':
            tampil_buku(data)
        elif pilih == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
