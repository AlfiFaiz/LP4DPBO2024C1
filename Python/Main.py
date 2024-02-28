# Import kelas-kelas yang dibutuhkan
from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle
from Garage import Garage
from ParkingLot import ParkingLot



car1 = Car("B123CD", "Toyota", 2020, "Hitam", 8, 4)
car2 = Car("B456EF", "Honda", 2021, "Putih", 4, 4)
car3 = Car("B789GH", "Mitsubisi", 2024, "Merah", 2, 2)

motorcycle1 = Motorcycle("D123EF", "Honda", 2021, "Merah", "Sport", 30)
motorcycle2 = Motorcycle("D456GH", "Yamaha", 2022, "Kuning", "Matic", 30)
motorcycle3 = Motorcycle("D789IJ", "Suzuki", 2023, "Hijau", "Bebek", 30)


print(f"\nGarasi")
garage = Garage("Garasi A", 100)
garage2 = Garage("Garasi B", 200)

# Menambahkan kendaraan ke garasi pertama
garage.tambah_kendaraan(car1)
garage.tambah_kendaraan(motorcycle1)
garage.tambah_kendaraan(motorcycle2)
garage.tambah_kendaraan(motorcycle3)

# Menampilkan daftar kendaraan di garasi pertama
garage.tampilkan_daftar_kendaraan()

# Menambahkan kendaraan ke garasi kedua
garage2.tambah_kendaraan(car2)
garage2.tambah_kendaraan(car3)

# Menampilkan daftar kendaraan di garasi kedua
garage2.tampilkan_daftar_kendaraan()


print(f"\nParking Lot")
parking_lot = ParkingLot(10)

# Menambahkan kendaraan ke tempat parkir
parking_lot.tambah_kendaraan(car1)
parking_lot.tambah_kendaraan(car2)
parking_lot.tambah_kendaraan(car3)
parking_lot.tambah_kendaraan(motorcycle1)

# Menampilkan informasi tempat parkir
parking_lot.tampilkan_info()
