#include <bits/stdc++.h>
// #include "Car.cpp"
#include "Motorcycle.cpp"
#include "Garage.cpp"
#include "Vehicle.cpp"

using namespace std;


// Fungsi main() yang digunakan sebagai program utama
int main() {
    ios::sync_with_stdio(0);
    cin.tie();


    // Instansiasi objek Laptop
    Motorcycle motor("Sport", 30,"D123EF", "Honda", 2021, "Merah");



    // Instansiasi objek Mahasiswa
    Garage garasi("210216", 20, motor);
   
    // Menampilkan informasi Mahasiswa
    cout << "Informasi Mahasiswa:" << endl;
    // cout << "NIM       : " << garasi.getNim() << endl;
    cout << "Nama      : " << garasi.get_nama() << endl;
    cout << "Fakultas  : " << garasi.getluas_garasi() << endl;
   
    // // Menampilkan informasi Dosen Wali milik mahasiswa
    // cout << "Informasi Dosen Wali dari " << mhs.getNama() << " : " << endl;
    // cout << "NIP       : " << mhs.getWaliDosen().getNip() << endl;
    // cout << "Nama      : " << mhs.getWaliDosen().getNama() << endl;
    // cout << "Keahlian  : " << mhs.getWaliDosen().getKeahlian() << endl;




    return 0; // Menyatakan keluaran dari fungsi main() adalah true
}
