print("Nabella Agustia")
print("2310431026")
print("shift 2")

print("DAFTAR TUJUAN BUS PT.ANS DARI PADANG")
print("====================================")
print ('''
1. Medan    : Rp.250.000
2. Jambi    : Rp.250.000
3. Lampung  : Rp.350.000
4. Jakarta  : Rp.400.000
5. Bandung  : Rp.500.000
6. Depok    : Rp.500.000
            ''')
pilihan = int(input("Pilih tujuan (pilihan dengan angka): "))
#operasi percabangan untuk menentukan tujuan kota
if pilihan == 1:
        harga = 250000
        tujuan = "Medan"
elif pilihan == 2: 
        harga = 250000
        tujuan = " Jambi"
elif pilihan == 3:
        harga = 350000
        tujuan = "Lampung"
elif pilihan == 4:
        harga = 400000
        tujuan = " Jakarta"
elif pilihan == 5:
        harga = 500000
        tujuan = " Bandung "
elif pilihan == 6:
        harga = 500000
        tujuan = "Depok"

print("DAFTAR JENIS KELAS")
print("======================")
print('''
1. Ekonomi class : Rp. 10.000
2. Bisnis class : Rp. 20.000
3. First class : Rp. 30.000
      ''')
kelas = int(input("Pilih jenis kelas(pilihan berupa angka): "))
#operasi percabangan untuk menentukan jenis kelas 
if kelas == 1:
    harga += 10000
    jenis_kelas = "Ekonomi class"
elif kelas == 2:
       harga += 20000
       jenis_kelas =  "Bisnis class"
elif kelas == 3:
       harga += 30000
       jenis_kelas = "first class"


jumlah_tiket= int (input("Masukkan jumlah tiket(berupa angka): "))
total = harga * jumlah_tiket 

#operasi percabangan untuk menghitung besar diskon
if (jumlah_tiket >= 3) & (jumlah_tiket <= 5):
       diskon = 5
elif jumlah_tiket > 5:
       diskon = 10
else :
      diskon = 0

#operasi menghitung harga diskon
harga_diskon = total * (diskon/100)

#operasi menghitung harga setelah diskon 
harga_total = total - harga_diskon 

print ( f"""
Tujuan = {tujuan}
Jenis kelas = {jenis_kelas}
Harga tiket = {harga}
Jumlah tiket = { jumlah_tiket}
Total = {total}
Diskon = {diskon}%
Diskon yang didapat = {harga_diskon}
Harga setelah diskon = {harga_total}
""")

       
    
