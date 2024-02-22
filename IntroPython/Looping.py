# For
varList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in varList:
    print(i)

# range(start, stop, step)
for i in range(15):
    print(i)

for i in range(1, 15, 3):
    print(i)

# While -> berhenti ketika memenuhi suatu kondisi
varCounter = 3
while varCounter <= 5:
    print(varCounter)
    varCounter += 1

# Nested Loop
for i in range(1, 5):
    for j in range(1, 3):
        print(i, j)

# Looping Control
for i in range(10):
    print("Perulangan Luar:", i)
    for j in range(10):
        print("Perulangan Dalam:", j)
        if j == i:
            break

for huruf in "Dico Ding":
    if huruf == " ":
        break
    print(f"Huruf saat ini: {huruf}")

# Continue -> skip
for huruf in 'Dico ding':
    if huruf == 'd':
        continue
    print('Huruf saat ini: {}'.format(huruf))

# Else di dalam for
varNumber = [1, 2, 3, 4, 5, 6, 7]
inputNumber = int(input("Masukkan nomor: "))

for i in varNumber:
    if i == inputNumber:
        print(f"Angka ditemukan: {i}")
        break
else:
    print(f"Angka {inputNumber} tidak ditemukan")

# Else setelah while
count = 0
while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")
    # tidak dieksekusi, karena while bernilai True, dan berhenti karena break

# Pass -> skip / tidak melakukan apapun

# List Comprehension
angka = [1, 2, 3, 4]
pangkat = [i ** 2 for i in angka]
print(pangkat)


evenNumber = [i for i in range(0, 501, 2)]
print(evenNumber)
