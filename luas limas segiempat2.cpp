#include <iostream>
using namespace std;
int main()
{
    float a,t;
    float luas, luas_permukaan, volume;
    	cout<<"Nabella Agustia: "<<endl; 
    	cout<<"2310431026"<<endl; 
    	
        cout<<"Menghitung Volume dan Luas permukaan limas segiempat"<<endl;
        cout<<"---------------"<<endl; 

    	cout << " masukkan sisi alas : ";
    	cin >> a ;
    	cout << "masukkan tinggi limas: ";
    	cin >> t ;

        luas=a*a;
        luas_permukaan = luas + (0.5*a*t)*4;
        volume = 1.0/3*luas*t;

        cout<<"luas permukaan limas: "<<luas_permukaan<<endl;

        cout<<"volume limas: "<<volume<<endl;

}
