#pragma once
// Memasukan library yang digunakan
#include <iostream>
#include <string>

using namespace std;

class Vehicle {
  private :

  string plat_nomor;
  string merk;
  string tahun_produksi;
  string warna;

  public :

  Vehicle(){
    
  }

  Vehicle(string plat_nomor){
    this->plat_nomor = plat_nomor;
    merk = "";
    tahun_produksi = "";
    warna = "";
  }

  Vehicle(string plat_nomor, string merk){
    this->plat_nomor = plat_nomor;
    this->merk = merk;
    tahun_produksi = "";
    warna = "";
  }

  Vehicle(string plat_nomor, string merk, string tahun_produksi){
    this->plat_nomor = plat_nomor;
    this->merk = merk;
    this->tahun_produksi = tahun_produksi;
    warna = "";
  }

  Vehicle(string plat_nomor, string merk, string tahun_produksi, string warna){
    this->plat_nomor = plat_nomor;
    this->merk = merk;
    this->tahun_produksi = tahun_produksi;
    this->warna = warna;
  }

  void set_plat_nomor(string plat_nomor)
  {
    this->plat_nomor = plat_nomor;
  }
  void set_merk(string merk)
  {
    this->merk = merk;
  }
  void set_tahun_produksi(string tahun_produksi)
  {
    this->tahun_produksi = tahun_produksi;
  }
  void set_warna(string warna)
  {
    this->warna = warna;
  }

  string get_plat_nomor()
  {
    return plat_nomor;
  }

  string get_merk(){
    return merk;
  }

  string get_tahun_produksi(){
    return tahun_produksi;
  }

  string get_warna(){
    return warna;
  }

  ~Vehicle(){

  }
}