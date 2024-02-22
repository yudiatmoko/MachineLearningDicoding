# zFill -> menambahkan 0 di depan kata untuk memastikan panjang karakter
teks = 'Code'
tambah_number = teks.zfill(7)
print(tambah_number)

# rJust -> menambahkan karakter di depan kata
teks = 'Dicoding'
tambahKarakter = teks.rjust(10,"_")
print(tambahKarakter)

# lJust -> menambahkan karakter di belakang kata
teks = 'Dicoding'
tambahKarakter = teks.ljust(10,"_")
print(tambahKarakter)

# center -> menjadikan rata tengah dengan karater diantara kata
teks = 'Dicoding'
tambahKarakter = teks.center(12,"_")
print(tambahKarakter)