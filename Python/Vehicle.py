#Saya Muhammad Alfi faiz NIM 2207045 mengerjakan
#soal Latihan 2 dalam mata kuliah Desain Pemograman Berorientasi Objek
#untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

class Vehicle:
    def __init__(self, plat_nomor, merk, tahun_produksi, warna):
        # Inisialisasi atribut-atribut kendaraan
        self.__plat_nomor = plat_nomor
        self.__merk = merk
        self.__tahun_produksi = tahun_produksi
        self.__warna = warna

    # Getter methods
    def get_plat_nomor(self):
        # Mendapatkan plat nomor kendaraan
        return self.__plat_nomor

    def get_merk(self):
        # Mendapatkan merk kendaraan
        return self.__merk

    def get_tahun_produksi(self):
        # Mendapatkan tahun produksi kendaraan
        return self.__tahun_produksi

    def get_warna(self):
        # Mendapatkan warna kendaraan
        return self.__warna

    # Setter methods
    def set_plat_nomor(self, plat_nomor):
        # Mengatur plat nomor kendaraan
        self.__plat_nomor = plat_nomor

    def set_merk(self, merk):
        # Mengatur merk kendaraan
        self.__merk = merk

    def set_tahun_produksi(self, tahun_produksi):
        # Mengatur tahun produksi kendaraan
        self.__tahun_produksi = tahun_produksi

    def set_warna(self, warna):
        # Mengatur warna kendaraan
        self.__warna = warna
