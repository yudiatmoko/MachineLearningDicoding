age = 17
salary = 5000000.0
complex = 1 + 12j
x = True

print(type(age))
print(type(salary))
print(type(complex))
print(type(x))

age = "17"
print(type(age))

# number bersifat immutable
var = 12
print(var)
print(id(var))

var = 13
print(var)
print(id(var))

# multilane string
greeting = """
Halo, Ilham!
Apa kabar?
"""
print(greeting)

# string adalah urutan char, dan bersifat immutable
greetingTwo = "Halo"
print(greetingTwo[1])
# slicing string
print(greetingTwo[1:])
print(greetingTwo[:4])

# formatted string
name = "Jawa Atmoko"
print(f"Halo, nama saya adalah {name}")
print(f"Halo, nama saya adalah %s" % (name))
print("Halo, nama saya adalah {}".format(name))

# tipe data collection

# list -> mutable
list = [1, "Ilham", True]
list[0] = 18
print(type(list))
print(list[0])

# slicing list sequence[start:stop:step]
'''
Start merupakan indeks pertama yang Anda ambil. Stop merupakan indeks terakhir yang ingin Anda ambil. Step merupakan jumlah elemen yang ingin Anda lewati di antara setiap elemen slice. Secara default, nilai step adalah 1.
'''
devices = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(devices[0])
print(devices[2])
print(devices[-1])
print(devices[-3])

# slicing
print(devices[0:7:4])
print(devices[1:])
print(devices[:7])

# Tuple -> imutable, bisa juga dilakukan slicing seperti list
tupleExample = (1, "Dicoding", 1+3j)
print(type(tupleExample))

# Set -> can't indexing and duplicate data
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

# Union and Intersection
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2) # -> penggabungan set, dan menghapus data duplicate
print("Union:", union)

intersection = set1.intersection(set2) # -> menampilkan data duplicate atau yang sama
print("Intersection:", intersection)

# Dictionary -> key : value
dictionaryExample = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(type(dictionaryExample))
print(dictionaryExample["name"]) # diakses melalui key, bukan indexing

# Add data to Dictionary
dictionaryExample ["Job"] = "Android Developer"
print(dictionaryExample)

# Delete data from Dictionary
del dictionaryExample["isMarried"]
print(dictionaryExample)

# Update data Dictionary
dictionaryExample['name'] = "Ilham Yudiatmoko"
print(dictionaryExample)

# Data Type Conversion
# Int -> Float
print(float(2))

# Float -> Int
print(int(2.0))

# From string to other data types or from other data types to string
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

# Collection Conversion
print(set([1,2,3]))
print(tuple({5,6,7}))
# print(list('ILHAM'))
print(dict([[1,2],[3,4]]))
print(dict([(3,26),(4,44)]))