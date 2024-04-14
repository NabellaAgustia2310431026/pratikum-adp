#include <iostream>
#include <cmath>

using namespace std;

int main()
{   cout<<"-----------------"<<endl;
    cout<<"Nabella Agustia"<<endl;
    cout<<"  2310431026   "<<endl;
    cout<<"   shift 2     "<<endl;
    cout<<"----------------"<<endl;
    cout<<"  TABEL FUNGSI  "<<endl;
    cout<<"----------------"<<endl;
    cout<<" f(x) = 3x^2 + 7x- 2, jika x >= 0"<<endl;
    cout<<"      = 2x^2 - 5x - 4, jika x < 0"<<endl;
    cout<<" g(x) = f(x)^ 2 - sqrt f(x)"<<endl;
    cout<<" h(x) = f(x) * g(x)"<<endl;

    int n = 0; // Inisialisasi jumlah data
    char pilihan;
    do
    {
        cout << "\n input banyak data n: ";
        cin >> n;
        int data [n];

        // Memasukkan nilai x ke dalam array
        for (int i = 0; i < n; i++)
        {
            cout << "input nilai x ke-" << i + 1 << ": ";
            cin >> data[i];
        }

        cout << "----------------------------------------------------------" << endl;
        cout << "   no   |    x    |    f(x)    |    g(x)    |    h(x)    |" << endl;
        cout << "----------------------------------------------------------" << endl;

        for (int i = 0; i < n; ++i)
        {
            float x = data[i];
            float fx;
                if (x >= 0)
            {
                fx = 3 * x * x + 7 * x - 2;
            }
                else if (x < 0)
            {
                fx = 2 * x * x - 5 * x - 4;
            }

            float gx = fx * fx  - sqrt(fx);
            float hx = fx * gx;


            cout << "    " << i + 1 << "   |   "<< "  " << x << "    |    " << fx << "    |    " << gx << "    |    " << hx << "   |   " << endl;
        }

        cout << "-----------------------------------------------------------" << endl;
        // Meminta input untuk menambah data baru atau tidak
        cout << "Input nilai X lagi? (Y/N): ";
        cin >> pilihan;
    } while (pilihan == 'Y' || pilihan == 'y');

    return 0;
}
