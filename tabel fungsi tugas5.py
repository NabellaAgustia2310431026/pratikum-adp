print ("--------------------")
print ("Nabella Agustia")
print ("  2310431026   ")
print ("   shift 2     ")
print("---------------------")
print ("   TABEL FUNGSI     ")
print("---------------------")
print( "f(x) = 3x^2 + 7x- 2, jika x >= 0")
print("      = 2x^2 - 5x - 4, jika x < 0")
print(" g(x) = f(x)^ 2 - sqrt f(x)")
print(" h(x) = f(x) * g(x)")


import math
n = 0  # Inisialisasi jumlah data
data = [0] * 50
pilihan = 'Y'

while pilihan == 'Y' or pilihan == 'y':
    n = int(input("\n Input banyak data n: "))
    
    # Memasukkan nilai x ke dalam list
    for i in range(n):
        data[i] = float(input("Input nilai x ke-{}: ".format(i + 1)))

    print("----------------------------------------------------------")
    print("   no   |    x    |    f(x)    |    g(x)    |    h(x)    |")
    print("----------------------------------------------------------")

    for i in range(n):
        x = data[i]
        if x >= 0:
            fx = 3 * x * x + 7 * x - 2
        elif x < 0:
            fx = 2 * x * x - 5 * x - 4

        gx = fx * fx  - math.sqrt(fx)
        hx = fx * gx

        print("    {}   |    {:.2f}    |    {:.2f}    |    {:.2f}    |    {:.2f}   |".format(i + 1, x, fx, gx, hx))

    print("-----------------------------------------------------------")
    # Meminta input untuk menambah data baru atau tidak
    pilihan = input("Input nilai X lagi? (Y/N): ")

print("Program selesai.")
