matriks = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

print(matriks)
print(matriks[0][1])

# Library numpy
import numpy
import sys

matriksNumpy = numpy.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])
print(matriksNumpy)

print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(matriks)*len(matriks))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", matriksNumpy.size*matriksNumpy.itemsize)