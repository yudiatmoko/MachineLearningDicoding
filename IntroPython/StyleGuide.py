
# Package
# huruf kecil dan singkat dan hindari garis bawah. Contoh: math

# File / Module
# huruf kecil dan singkat, atau dengan tambahan _. Contoh: math_operations.py

# Class
# huruf besar setiap kosakata, tetapi kebanyakan nama kelas hanya satu kata. Contoh: Vehicle

# Variable Type
# huruf besar setiap kosakata, Contoh: T, AnyStr, Num

# Function, Variable, and Parameter
# huruf kecil dan garis bawah. Variable: first_name, last_name, full_name | Function: addSpeed | Parameter: length: int = 2

# Constant
# LOWERCASE. Contoh : PI, TOTAL

# Contoh
class MyClass:
    def __init__(self):
        self._private_var = 42   # Variabel non publik dengan awalan satu garis bawah
        self._secret_list = [1, 2, 3]  # Variabel non publik lainnya

    def _private_method(self):
        print("Ini adalah method non publik")

    def public_method(self):
        print("Ini adalah method publik")
        self._private_method()  # Method publik dapat memanggil method non publik
