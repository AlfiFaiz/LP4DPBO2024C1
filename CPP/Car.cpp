#pragma once
// Memasukan library yang digunakan
#include <iostream>
#include <string>
#include "Vehicle.cpp"

using namespace std;

class Car : public Vehicle
{
    private:
        int jumlah_pintu;
        int jumlah_kursi;
    public:
    Car(){
        
    }

    Car(int jumlah_pintu, string plat_nomor, string merk, string tahun_produksi, string warna) : Vehicle(string plat_nomor, string merk, string tahun_produksi, string warna){
        this->jumlah_pintu = jumlah_pintu;
        jumlah_kursi ="";
    }
    Car(int jumlah_pintu,int jumlah_kursi, string plat_nomor, string merk, string tahun_produksi, string warna) : Vehicle(string plat_nomor, string merk, string tahun_produksi, string warna){
        this->jumlah_pintu = jumlah_pintu;
        this->jumlah_kursi = jumlah_kursi;
    }

    void set_jumlah_pintu(int jumlah_pintu){
        this->jumlah_pintu = jumlah_pintu;
    }

    void set_jumlah_kursi(int jumlah_kursi){
        this->jumlah_kursi = jumlah_kursi;
    }

    string get_jumlah_pintu(){
        return jumlah_pintu;
    }
    int get_jumlah_kursi(){
        return jumlah_kursi;
    }
}