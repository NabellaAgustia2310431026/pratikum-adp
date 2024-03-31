print ("NABELLA AGUSTIA")
print ("2310431026")
print ("shift 2 ")

print("\n Menampilkan Lirik Lagu ")
print("===========================")

teks = input ('ketik lirik lagu: ')
pengganti = input ('masukkan pengganti: ')
for huruf in 'a,i,u,e,o': 
  teks = teks.replace (huruf , pengganti)
  teks= teks.replace (',','\n')
print (f'\n{teks}')
