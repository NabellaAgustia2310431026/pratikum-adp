#include <iostream>
using namespace std;
int main () {

    float nilai_agama = 4;
    float nilai_pengantar_matematika = 4;
    float nilai_fisika = 3;
    float nilai_kimia= 4;
    float nilai_kalkulus_1= 3.50;
    float nilai_analisis_data= 4;
    float nilai_bahasa_inggris_matematika= 4;
    float nilai_bahasa_indonesia= 3.75;
    int sks;
    float ip, ipk;
        cout<< "NABELLA AGUSTIA"<<endl;
        cout<<" 2310431026"<<endl;

        cout<< "Nilai-nilai di Semester 1"<<endl;
        cout<< " ........................"<<endl;
        cout<< " 1. Agama                       = "<<nilai_agama<<endl;
        cout<< "    SKS                         = 2"<<endl;
        cout<< " 2. Pengantar Matematika        = "<<nilai_pengantar_matematika<<endl;
        cout<< "    SKS                         = 3"<<endl;
        cout<< " 3. Fisika                      = "<<nilai_fisika<<endl;
        cout<< "    SKS                         = 2"<<endl;
        cout<< " 4. Kimia                       = "<<nilai_kimia<<endl;
        cout<< "    SKS                         = 2"<<endl;
        cout<< " 5. Kalkulus 1                  = "<<nilai_kalkulus_1<<endl;
        cout<< "    SKS                         = 3"<<endl;
        cout<< " 6. Analisis Data               = "<<nilai_analisis_data<<endl;
        cout<< "    SKS                         = 3"<<endl;
        cout<< " 7. Bahasa Inggris Matematika   = "<<nilai_bahasa_inggris_matematika<<endl;
        cout<< "    SKS                         = 2"<<endl;
        cout<< " 8. Bahasa Indonesia            = "<<nilai_bahasa_indonesia<<endl;
        cout<< "    SKS                         = 2"<<endl;

        ip = (nilai_agama+nilai_pengantar_matematika+nilai_fisika+nilai_kimia+nilai_kalkulus_1+nilai_analisis_data+nilai_bahasa_inggris_matematika+nilai_bahasa_indonesia)/8;
        ipk= ip/1;
        
        cout<<" IP Sementara= "<<ip<<endl;
        cout<<" IPK= "<<ipk<<endl;

}