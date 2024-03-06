#pragma once
// Memasukan library yang digunakan
#include <iostream>
#include <string>
#include "Vehicle.cpp"

using namespace std;

class Motorcycle : public Vehicle
{
    private:
        string jenis_motor;
        int kapasitas_tangki;
    public:
    Motorcycle(){
        
    }

    Motorcycle(string jenis_motor, string plat_nomor, string merk, string tahun_produksi, string warna) : Vehicle(string plat_nomor, string merk, string tahun_produksi, string warna){
        this->jenis_motor = jenis_motor;
        kapasitas_tangki ="";
    }
    Motorcycle(string jenis_motor,int kapasitas_tangki, string plat_nomor, string merk, string tahun_produksi, string warna) : Vehicle(string plat_nomor, string merk, string tahun_produksi, string warna){
        this->jenis_motor = jenis_motor;
        this->kapasitas_tangki = kapasitas_tangki;
    }

    void set_jenis_motor(string jenis_motor){
        this->jenis_motor = jenis_motor;
    }

    void set_kapasitas_tangki(int kapasitas_tangki){
        this->kapasitas_tangki = kapasitas_tangki;
    }

    string get_jenis_motor(){
        return jenis_motor;
    }
    int get_kapasitas_tangki(){
        return kapasitas_tangki;
    }
}