# Class
class Mobil:
    # Atribut
    warna = "Merah"


# Object
mobilRush = Mobil()
print(mobilRush.warna)
mobilRush.warna = "Biru"
print(mobilRush.warna)


# Class Constructor
class Motor:
    # Atribut Instance
    def __init__(self):
        self.warna = "Hijau"


motorVega = Motor()
motorBeat = Motor()

print(motorBeat.warna)

motorVega.warna = "Merah"
print(motorVega.warna)


#

class Mobil:
    def __init__(self, warna, merk, kecepatan):
        self.warna = warna
        self.merk = merk
        self.kecepatan = kecepatan


mobilFortuner = Mobil("Putih", "Toyota", 220)
print(mobilFortuner.warna)
print(mobilFortuner.merk)
print(mobilFortuner.kecepatan)


# Decorator
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")

    return wrapper


# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello, world!")


# Memanggil fungsi yang sudah didekorasi
say_hello()


# Method

# Object Method
class Mobil:
    def __init__(self, warna, merk, kecepatan):
        self.warna = warna
        self.merk = merk
        self.kecepatan = kecepatan

    def tambahKecepatan(self):
        self.kecepatan += 10


mobilFortuner = Mobil("Putih", "Toyota", 220)
print(mobilFortuner.warna)
print(mobilFortuner.merk)
print(f"Sebelum tambah kecepatan: {mobilFortuner.kecepatan}")
mobilFortuner.tambahKecepatan()
print(f"Setelah tambah kecepatan: {mobilFortuner.kecepatan}")


# Static Method
class Vehicle:
    def __init__(self, merk):
        self.merk = merk

    @staticmethod
    def introVehicle():
        print("Ini adalah static method dari kelas Vehicle")


Vehicle.introVehicle()
car = Vehicle("Dihatsu")
print(car.merk)
car.introVehicle()


# Class Method
class Vehicle2:
    def __init__(self, merk):
        self.merk = merk

    @classmethod
    def introVehicle2(cls):
        print("Ini adalah static method dari kelas Vehicle2")


Vehicle2.introVehicle2()
car = Vehicle2("Honda")
print(car.merk)
car.introVehicle2()