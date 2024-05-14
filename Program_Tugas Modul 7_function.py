print ("\n****** KONVERSI SUHU ******")
print ("===========================")

def input_suhu():
    batas = {'c': (0,100), 'k': (273,373), 'f': (32,212), 'r': (0,80)}  
    
    while True:
        satuan = input("\nMasukkan satuan (C/F/K/R): ").lower()
        if satuan in batas:
            batas_minimal, batas_maksimal = batas[satuan]
            suhu = float(input(f"Masukkan suhu dalam derajat {satuan.upper()} (minimal {batas_minimal}, maksimal {batas_maksimal}): "))
            if batas_minimal <= suhu <= batas_maksimal:
                return suhu, satuan.upper()
            else:
                print(f"Suhu yang Anda masukkan diluar batas yaitu ({batas_minimal} sampai {batas_maksimal})")
        else:
            print("Satuan yang Anda masukkan salah")


        
def konversi_suhu(suhu,satuan):
    if satuan == 'C':
        reamur = 4/5* suhu
        ferenheit = (9/5 * suhu) + 32
        kelvin = suhu + 273.15
        return reamur, ferenheit, kelvin 
    elif satuan == 'F':
        celcius = (suhu - 32) * 5/9
        reamur = (4/9) * (suhu-32)
        kelvin = 5/9 * (suhu - 32)  + 273.15
        return celcius, reamur, kelvin
    elif satuan == 'R':
        celcius = suhu * 5/4
        ferenheit = (suhu * 9/4) + 32
        kelvin = (5/4 * suhu) + 273.15
        return celcius, ferenheit, kelvin
    elif satuan == 'K':
        celcius = suhu - 273.15
        reamur = (4/5) * ( suhu - 273.15)
        ferenheit = (9/5) * (suhu-273.15) + 32
        return celcius, reamur, ferenheit
   
def tampilkan_hasil():
    suhu, satuan = input_suhu()
    hasil = konversi_suhu(suhu, satuan)
    
    if satuan.upper() == 'C':
        print(f"\nSuhu dalam satuan {suhu} derajat celcius:")
        print("=======================================")
        print("|  Satuan Suhu   |  Derajat Suhu  |")
        print("=======================================")
        print(f"|     Reamur      |      {hasil[0]:10.2f}   |")
        print(f"|   Fahrenheit    |      {hasil[1]:10.2f}   |")
        print(f"|     Kelvin      |      {hasil[2]:10.2f}   |")
        print("=======================================")
    elif satuan.upper() == 'F':
        print(f"\nSuhu dalam satuan {suhu} derajat fahrenheit:")
        print("=======================================")
        print("|  Satuan Suhu   |  Derajat Suhu  |")
        print("=======================================")
        print(f"|     Reamur      |      {hasil[1]:10.2f}   |")
        print(f"|     Kelvin      |      {hasil[2]:10.2f}   |")
        print(f"|     Celcius     |      {hasil[0]:10.2f}   |")
        print("=======================================")
    elif satuan.upper() == 'K':
        print(f"\nSuhu dalam satuan {suhu} derajat kelvin:")
        print("=======================================")
        print("|  Satuan Suhu   |  Derajat Suhu  |")
        print("=======================================")
        print(f"|     Reamur      |      {hasil[1]:10.2f}   |")
        print(f"|   Fahrenheit    |      {hasil[2]:10.2f}   |")
        print(f"|     Celcius     |      {hasil[0]:10.2f}   |")
        print("=======================================")
    elif satuan.upper() == 'R':
        print(f"\nSuhu dalam satuan {suhu} derajat reamur:")
        print("=======================================")
        print("|  Satuan Suhu   |  Derajat Suhu  |")
        print("=======================================")
        print(f"|     Celcius     |      {hasil[0]:10.2f}   |")
        print(f"|   Fahrenheit    |      {hasil[1]:10.2f}   |")
        print(f"|     Kelvin      |      {hasil[2]:10.2f}   |")
        print("=======================================")
    

tampilkan_hasil()
