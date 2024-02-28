# Import class Vehicle yang menjadi parent class
from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, plat_nomor, merk, tahun_produksi, warna, jenis_motor, kapasitas_tangki):
        # Memanggil konstruktor dari parent class (Vehicle)
        super().__init__(plat_nomor, merk, tahun_produksi, warna)
        
        # Menambahkan atribut khusus untuk class Motorcycle
        self.__jenis_motor = jenis_motor
        self.__kapasitas_tangki = kapasitas_tangki

    # Getter methods untuk mendapatkan nilai atribut
    def get_jenis_motor(self):
        return self.__jenis_motor

    def get_kapasitas_tangki(self):
        return self.__kapasitas_tangki

    # Setter methods untuk mengubah nilai atribut
    def set_jenis_motor(self, jenis_motor):
        self.__jenis_motor = jenis_motor

    def set_kapasitas_tangki(self, kapasitas_tangki):
        self.__kapasitas_tangki = kapasitas_tangki
