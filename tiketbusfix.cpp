#include <iostream>
using namespace std;
int main(){
    int harga_tiket, jumlah_tiket,diskon,harga_diskon,harga, total_harga, kelas, pilihan;
    string nama_pembeli, tujuan, jenis_kelas;

    cout<<"Nabella Agustia"<<endl;
    cout<<"2310431026"<<endl;
    cout<<"shift : 2"<<endl;

     cout<<"\n BUS PT.ANS Lintas Sumatera dari Padang"<<endl;
     cout<<"======================================"<<endl;

     cout<<"     \n Daftar Tujuan  Bus PT.ANS       "<<endl;
     cout<<"======================================"<<endl;
     cout<<" Tujuan     | Harga tiket|"<<endl;
     cout<<" 1. Medan   : Rp. 250.000 "<<endl;
     cout<<" 2. Jambi   : Rp. 250.000 "<<endl;
     cout<<" 3. Lampung : Rp. 350.000 "<<endl;
     cout<<" 4. Jakarta : Rp. 450.000 "<<endl;
     cout<<" 5. Bandung : Rp. 500.000 "<<endl;
     cout<<" 6. Depok   : Rp. 500.000 "<<endl;
     cout<<"======================================="<<endl;

     cout<<"masukkan pilihan: ";
     cin>>pilihan;

        if (pilihan == 1){
                harga_tiket = 250000;
                tujuan = "medan";
        }
        else if (pilihan== 2){
                harga_tiket = 250000;
                tujuan = "Jambi";
        }
        else if (pilihan== 3){
                harga_tiket = 350000;
                tujuan = "Lampung";
        }
        else if (pilihan == 4){
                harga_tiket = 450000;
                tujuan = "Jakarta";
        }
        else if (pilihan == 5){
                harga_tiket = 500000;
                tujuan = "Bandung";
        }
        else if (pilihan == 6 ){
                harga_tiket = 500000;
                tujuan = "Depok";
        }

     cout<<"        \n JENIS KELAS                  "<<endl;
     cout<<" ====================================="<<endl;
     cout<<" Kelas          |  Harga Tambahan |"<<endl;
     cout<<" Ekonomi Class  | Rp. 10.000      |"<<endl;
     cout<<" Bisnis Class   | Rp. 20.000      |"<<endl;
     cout<<" First Class    | Rp. 30.000      |"<<endl;
     cout<<"======================================="<<endl;

      cout<<"jenis kelas: ";
      cin>>kelas;

      if (kelas == 1 ) {
        harga_tiket += 10000;
        jenis_kelas = "ekonomi class";
      }
      else if ( kelas == 2) {
        harga_tiket += 20000;
        jenis_kelas = "bisnis class";
      }
    else if ( kelas == 3){
        harga_tiket += 30000;
        jenis_kelas = "first class";
     }
        cout<<"masukkan jumlah tiket: ";
        cin>>jumlah_tiket;
        harga = harga_tiket * jumlah_tiket;

        if ( jumlah_tiket>=3 && jumlah_tiket <=5){
            diskon = 5;
        }
        else if (jumlah_tiket >5){
            diskon = 10;
        }
        else if (jumlah_tiket <= 2){
            diskon = 0;
        }

        harga_diskon = harga * 0.01 * diskon;
        total_harga = harga - harga_diskon;

        cout<<"\n Tujuan : "<<tujuan<<endl;
        cout<<"Jenis kelas: "<<jenis_kelas<<endl;
        cout<<"harga tiket: Rp. "<<harga_tiket<<endl;
        cout<<"Jumlah Tiket: Rp. "<<jumlah_tiket<<endl;
        cout<<"harga total: Rp. "<<harga<<endl;
        cout<<"Diskon: "<<diskon<<endl;
        cout<<"Diskon yang didapat: "<<harga_diskon<<endl;
        cout<<"Harga setelah diskon: "<<total_harga<<endl;

}

