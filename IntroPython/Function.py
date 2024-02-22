# Documentation String
def mencari_luas_persegi_panjang(panjang, lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """

    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang


persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)


# Argument

# Keyword Argument
def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang


persegi_panjang_pertama = mencari_luas_persegi_panjang(panjang=5, lebar=10)

print(persegi_panjang_pertama)


# Positional Argument
def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang


persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)

print(persegi_panjang_pertama)


# Parameter

# Positional or Keyword
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan


print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))


# Positional Only
def penjumlahan(a, b, /):
    return a + b


print(penjumlahan(8, 50))


# print(penjumlahan(a=3, b=5)) // keyword tidak bisa

# Keyword Only
def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan


print(greeting(pesan="Selamat sore!", nama="Dicoding"))


# print(greeting("Selamat sore!","Dicoding")) // positional tidak bisa

# Variadic Positional
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total


print(hitung_total(1, 2, 3, 4, 5))


# Variadic Keyword

def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info


print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

# Lambda Expression
rectangularAreaFormula = lambda length, width: length * width
print(rectangularAreaFormula(5, 2))

# Scope Variable

# Global Variable
a = 10  # global


def add(b):
    result = a + b
    return result


bilanganPertama = add(20)
print(bilanganPertama)


# Local Variable
def add(a, b):
    lokal_var = 5
    result = a + b - lokal_var
    return result


bilanganPertama = add(10, 20)
print(bilanganPertama)


# Practice
def minimal(a, b):
    if a <= b:
        return a
    else:
        return b


test = minimal(3, 2)
print(test)
