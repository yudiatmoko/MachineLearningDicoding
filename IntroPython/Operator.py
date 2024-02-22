
# Operator Aritmatika
# + - * / // % **
x = 11
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)
print(x ** y)

# Operator Relasional
# == != > < >= <=
x = 5
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = "Dicoding"
y = "Indonesia"

print(f"\n{x == y}")
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Operator Logika
# AND, OR, NOT

# AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# NOT
print(not True)
print(not False)


# Operator Assignment
# += -= *= /= %=

# +=
x = 11
x += 5
print(x)

# -=
x = 11
x -= 5
print(x)

# *=
x = 11
x *= 5
print(x)

# /=
x = 11
x /= 5
print(x)

#%=
x = 11
x%= 5
print(x)


"""
TODO:
Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
  dan simpan dalam variabel bernama "total_harga".

Tips:
- Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
"""
# Jangan ubah kode ini
dico = 750000
discon = dico * 10/100
total_harga = dico - discon
print(total_harga)
