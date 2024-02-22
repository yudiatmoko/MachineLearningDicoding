
# length -> menghiutng banyaknya elemen

# List
listExample = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(listExample)
print(len(listExample))

# Set
setExample = set([1, 3, 3, 5, 5, 5, 7, 7, 9])
print(setExample)
print(len(setExample))

# String
stringExample = "Ilham Yudiatmoko"
print(stringExample)
print(len(stringExample))

# min and max -> mengetahui nilai min dan maks dari list
listExample = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(listExample)
print(min(listExample))
print(max(listExample))

# count -> mengetahui berapa kali suatu objek muncul di list
evenExample = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(evenExample.count(6))

substring = "e"
print(stringExample.count(substring))

# in and not in -> mengetahui apakah ada objek di dalam list (boolean)
substring = "y" # case sensitive
print(substring in stringExample)
print(substring not in stringExample)

# set nilai untuk multiple variable
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

# sort tidak mengurutkan list yang memiliki elemen campuran
# ASCII -> uppercase priority
# ascending sorting
vehicleExample = ['motor', 'mobil', 'helikopter', 'Pesawat']
vehicleExample.sort(key=str.lower)
print(vehicleExample)

# descending sorting
vehicleExample.sort(reverse = True)
print(vehicleExample)


