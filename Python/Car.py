# Import class Vehicle yang menjadi parent class
from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, plat_nomor, merk, tahun_produksi, warna, jumlah_kursi, jumlah_pintu):
        # Memanggil konstruktor dari parent class (Vehicle)
        super().__init__(plat_nomor, merk, tahun_produksi, warna)
        
        # Menambahkan atribut khusus untuk class Car
        self.__jumlah_kursi = jumlah_kursi
        self.__jumlah_pintu = jumlah_pintu

    # Getter methods untuk mendapatkan nilai atribut
    def get_jumlah_kursi(self):
        return self.__jumlah_kursi

    def get_jumlah_pintu(self):
        return self.__jumlah_pintu

    # Setter methods untuk mengubah nilai atribut
    def set_jumlah_kursi(self, jumlah_kursi):
        self.__jumlah_kursi = jumlah_kursi

    def set_jumlah_pintu(self, jumlah_pintu):
        self.__jumlah_pintu = jumlah_pintu
