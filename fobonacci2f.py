print ("Nabella Agustia")
print ("2310431026")
print ("shift :2")

print ("PROGRAM DERET DAN JUMLAH DERET BILANGAN FIBONACCI")
print("===================================================")

while True: 
    data =int(input("masukkan bilangan n untuk fibonacci ke-: "))
    if data <3 or data >199: 
        print("melewati batas interval nilai")
    else:
        if data >100 and data <109:
            print("bilangan n harus selain interval 100 sampai 109")
        else : 
            break 

f1 = 1
f2 = 1
deret = []
for i in range (data): 
    deret.append(f1)
    total = f1 + f2 
    f1 = f2
    f2 = total 
    total_deret=sum(deret)
print("deret fibonacci: ", deret)
print ("Jumlah deret : ", total_deret)

    
    