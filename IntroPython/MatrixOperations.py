
# Multiplying matrix element by constants
# 2 x [5 0]
#     [1 -2]

varMatrix = [
    [5, 0],
    [1, -2]
]
defMatrix = [
    [0 for i in range(2)]
    for j in range(2)
]

for i in range(len(varMatrix)):
    for j in range(len(varMatrix[0])):
        defMatrix[i][j] = varMatrix[i][j] * 2

print(defMatrix)

# with library NumPy
import numpy as np

varMat = np.array(
    [
        [5, 0],
        [1, -2]
    ]
)

result = varMat * 2
resultTranspose = varMat.transpose()
resultDeterminant = np.linalg.det(varMat)
resultInverse = np.linalg.inv(varMat)

print(result)
print(resultTranspose)
print(resultInverse)
print(resultDeterminant)
