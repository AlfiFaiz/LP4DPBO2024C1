#Saya Muhammad Alfi faiz NIM 2207045 mengerjakan
#soal Latihan 2 dalam mata kuliah Desain Pemograman Berorientasi Objek
#untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

# Import class Vehicle dan turunannya
from Vehicle import Vehicle
from Motorcycle import Motorcycle  # Import Motorcycle class
from Car import Car  # Import Car class

class ParkingLot:
    def __init__(self, kapasitas):
        # Inisialisasi atribut-atribut tempat parkir
        self.__kapasitas = kapasitas
        self.__daftar_kendaraan = []

    def tambah_kendaraan(self, kendaraan):
        # Menambahkan kendaraan ke dalam daftar kendaraan di tempat parkir
        if len(self.__daftar_kendaraan) < self.__kapasitas:
            self.__daftar_kendaraan.append(kendaraan)
        else:
            print("Parkir penuh. Tidak dapat menambahkan kendaraan.")

    def tampilkan_info(self):
        # Menampilkan informasi tentang kapasitas dan kendaraan di tempat parkir
        print(f"Kapasitas Parkir: {self.__kapasitas}")
        print(f"Jumlah Kendaraan Saat Ini: {len(self.__daftar_kendaraan)}")
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
