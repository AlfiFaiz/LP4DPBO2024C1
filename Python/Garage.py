# Import class Vehicle dan turunannya
from Vehicle import Vehicle
from Motorcycle import Motorcycle
from Car import Car

class Garage:
    def __init__(self, nama_garasi, luas_garasi):
        # Inisialisasi atribut-atribut garasi
        self.__nama_garasi = nama_garasi
        self.__luas_garasi = luas_garasi
        self.__daftar_kendaraan = []

    def tambah_kendaraan(self, kendaraan):
        # Menambahkan kendaraan ke dalam daftar kendaraan di garasi
        self.__daftar_kendaraan.append(kendaraan)

    def tampilkan_daftar_kendaraan(self):
        # Menampilkan informasi garasi dan daftar kendaraan yang ada
        print(f"============== {self.__nama_garasi} ==============")
        print(f"LUAS Garasi : {self.__luas_garasi}\n")
        for i, kendaraan in enumerate(self.__daftar_kendaraan, start=1):
            print(f"        === KENDARAAN {i} ===")
            if isinstance(kendaraan, Motorcycle): 
                # Menampilkan informasi motor
                print(f"              Motor")
                print(f" - Plat Nomor        : {kendaraan.get_plat_nomor()}")
                print(f" - Merk              : {kendaraan.get_merk()}")
                print(f" - Tahun Produksi    : {kendaraan.get_tahun_produksi()}")
                print(f" - Warna             : {kendaraan.get_warna()}")
                print(f" - Jenis             : {kendaraan.get_jenis_motor()}")
                print(f" - Kapasitas Tangki  : {kendaraan.get_kapasitas_tangki()}")
            elif isinstance(kendaraan, Car):
                # Menampilkan informasi mobil
                print(f"              Mobil")
                print(f" - Plat Nomor        : {kendaraan.get_plat_nomor()}")
                print(f" - Merk              : {kendaraan.get_merk()}")
                print(f" - Tahun Produksi    : {kendaraan.get_tahun_produksi()}")
                print(f" - Warna             : {kendaraan.get_warna()}")
                print(f" - Jumlah Kursi      : {kendaraan.get_jumlah_kursi()}")
                print(f" - Jumlah Pintu      : {kendaraan.get_jumlah_pintu()}")
            print("        ===================\n")
        print("======================================")

    def get_nama_garasi(self):
        # Getter untuk mendapatkan nama garasi
        return self.__nama_garasi

    def get_luas_garasi(self):
        # Getter untuk mendapatkan luas garasi
        return self.__luas_garasi
