print ("\nProgram_Nilai_Mahasiswa")
print("***************************")
#menentukan matriks n*m
n = int (input("\nMasukkan jumlah mahasiswa: "))
m = int (input("Masukkan jumlah mata kuliah: "))

#inisialisasi array nama mahasiswa dan nama mata kuliah 
nama_mahasiswa = []
nama_mata_kuliah= []

#menginput nama mahasiswa
print("\nMasukkan nama mahasiswa: ")
for i in range (n):
    nama= input(f"Masukkan Nama mahasiwa ke-{i+1}: ")
    nama_mahasiswa.append(nama)

#mengiput mata kuliah mahasiswa
print("\nMasukkan nama mata kuliah: ")
for j in range (m): 
    mata_kuliah= input(f"Masukkan mata kuliah ke-{j+1}: ")
    nama_mata_kuliah.append(mata_kuliah)

#inisialisasikan nilai ujian  
nilai_ujian= []

#menginput nilai nilai ujian masing-masing mahasiswa dari setiap mata kuliah 
print("\nMasukkan nilai ujian setiap mahasiswa dan setiap mata kuliah: ")
for i in range (n):
    nilai_mahasiswa =[]
    print(f"Nilai untuk mahasiswa {nama_mahasiswa[i]}: ")
    for j in range (m):
        nilai= int(input(f"Nilai dari matkul {nama_mata_kuliah[j]} : "))
        nilai_mahasiswa.append(nilai)
    nilai_ujian.append(nilai_mahasiswa)
       

#menampilkan array dari nama mahasiswa dan mata kuliah
print("\n----------------------------------------------")
print("List Nama mahasiswa:", nama_mahasiswa)
print("List nama mata kuliah: ", nama_mata_kuliah)
print("List nilai mahasiswa: ")
for nilai_mahasiswa in nilai_ujian: 
    print(nilai_mahasiswa)
print("----------------------------------------------")

#1. Menampilkan data nilai ujian dalam bentuk tabel
print("\n===================================")
print("         Data Nilai Ujian ")
print("===================================")
print("\nNama Mahasiswa\t|", end= " ")
for j in range (m):
    print (f" Mata kuliah {j+1} |", end=" ")
print()
for i in range (n): 
    print("{:<19}".format(nama_mahasiswa[i]), end=" ")
    for j in range (m):
        print("{:<19}".format(nilai_ujian[i][j]), end=" ")
    print()

#2. Menghitung nilai rata-rata nilai ujian dari setiap mahasiswa
rata_rata_mahasiswa= [ ]
print("\nRata-rata Nilai Ujian Setiap Mahasiswa: ")
for i in range(n): 
    total= sum(nilai_ujian[i])
    rata_rata = total/m
    rata_rata_mahasiswa.append(rata_rata)
# Menampilkan nama dan rata-rata setiap mahasiswa
print("\n------------------------------")
print("| Nama Mahasiswa | Rata-rata |")
for i in range(n):
    print(f" {nama_mahasiswa[i]}\t              {rata_rata_mahasiswa[i]}")
print("------------------------------")

#3. Menentukan nilai tertinggi dan terendah dari setiap mata kuliah
nilai_tertinggi_mata_kuliah = []
nilai_terendah_mata_kuliah = []

for j in range(m):
    # Mendapatkan nilai semua mahasiswa untuk mata kuliah j
    nilai_mata_kuliah_j = [nilai_ujian[i][j] for i in range(n)]

    # Inisialisasi nilai tertinggi dan terendah untuk mata kuliah j
    nilai_tertinggi = nilai_mata_kuliah_j[0]
    nilai_terendah = nilai_mata_kuliah_j[0]

    # Inisialisasi list untuk menyimpan nama mahasiswa dengan nilai tertinggi dan terendah
    nama_mahasiswa_tertinggi = [1]
    nama_mahasiswa_terendah = [1]

    # Loop untuk mencari nilai tertinggi dan terendah beserta nama mahasiswa
    for i in range(1, n):
        if nilai_mata_kuliah_j[i] > nilai_tertinggi:
            nilai_tertinggi = nilai_mata_kuliah_j[i]
            nama_mahasiswa_tertinggi = [i+1]
        elif nilai_mata_kuliah_j[i] == nilai_tertinggi:
            nama_mahasiswa_tertinggi.append(i+1)

        if nilai_mata_kuliah_j[i] < nilai_terendah:
            nilai_terendah = nilai_mata_kuliah_j[i]
            nama_mahasiswa_terendah = [i+1]
        elif nilai_mata_kuliah_j[i] == nilai_terendah:
            nama_mahasiswa_terendah.append(i+1)

    # Menambahkan nilai tertinggi dan terendah ke dalam list
    nilai_tertinggi_mata_kuliah.append((nilai_tertinggi, nama_mahasiswa_tertinggi))
    nilai_terendah_mata_kuliah.append((nilai_terendah, nama_mahasiswa_terendah))

# Menampilkan nilai tertinggi dan terendah dari setiap mata kuliah
for j in range(m):
    print(f"\nMata kuliah {j+1}: ")
    print(f"Nilai Tertinggi: {nilai_tertinggi_mata_kuliah[j][0]} - Mahasiswa: {nilai_tertinggi_mata_kuliah[j][1]}")
    print(f"Nilai Terendah: {nilai_terendah_mata_kuliah[j][0]} - Mahasiswa: {nilai_terendah_mata_kuliah[j][1]}")
