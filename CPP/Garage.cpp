#pragma once
// Memasukan library yang digunakan
#include <iostream>
#include <string>
#include "Vehicle.cpp"
// #include "Car.cpp"
#include "Motorcycle.cpp"


using namespace std;


class Garage : public Motorcycle
{
private:
    string nama;
    int luas_garasi;

public:
    Garage()
    {


    }
  // Constructor : Overloading
    Garage(string nama, string jenis_motor,int kapasitas_tangki, string plat_nomor, string merk, string tahun_produksi, string warna) : Motorcycle( jenis_motor, kapasitas_tangki,  plat_nomor,  merk,  tahun_produksi,  warna)
    {  
        this->nama = nama;
        luas_garasi = 0;
    }


    // Constructor : Overloading
    Garage(string nama, int luas_garasi, string jenis_motor,int kapasitas_tangki, string plat_nomor, string merk, string tahun_produksi, string warna) : Motorcycle( jenis_motor, kapasitas_tangki,  plat_nomor,  merk,  tahun_produksi,  warna)
    { 
       
        this->nama = nama;
        this->luas_garasi = fakultas;
    }




    // Method setter untuk set setiap nilai atribut pada kelas Garage
    void setNama(string Nama)
    {
        this->nama = Nama;
    }


    void setluas_garasi(string luas_garasi)
    {
        this->luas_garasi = luas_garasi;
    }




    // Method getter untuk mendapatkan nilai setiap atribut pada kelas Garage
    string get_nama()
    {
        return nama;
    }


    string getluas_garasi()
    {
        return luas_garasi;
    }



    // Destructor
    ~Garage()
    {


    }
};


