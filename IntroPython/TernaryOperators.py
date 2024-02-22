
# If Else
ketersediaan = "Daging ayam"

if ketersediaan == "Daging sapi":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")

string = ""
if string: print("Ini True")
else: print("Ini False")

nilai = 82
perilaku = "tidak baik"

if nilai>=80 and perilaku != "baik":
    print("Selamat! Anda mendapat nilai A dan Berperilaku Tidak Baik")
    print("Tingkatkan!")
elif nilai>=80 and perilaku == "baik":
    print("Selamat! Anda mendapat nilai A dan Berperilaku Baik")
    print("Pertahankan!")
elif nilai>=70:
    print("Hore! Anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai>=60:
    print("Hmm.. Anda mendapat nilai C")
    print("Ayo semangat!")
else:
    print("Waduh, Anda mendapat nilai D")
    print("Yuk belajar lebih giat lagi!")

# TernaryOperation -> One Liner
print("Selamat! Anda mendapat nilai A dan Berperilaku Tidak Baik") if nilai >= 80 and perilaku != "baik" else print("Selamat! Anda mendapat nilai A dan Berperilaku Baik")

# TernaryTuples
# (blokKodeSalah, blokKodeBenar) [kondisi]

lulus = True
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
print(kelulusan)

