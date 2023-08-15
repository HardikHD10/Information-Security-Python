import math
from sympy import *

plaintext = input("Enter plaintext: ").upper()
key = input("Enter key: ").upper()

if len(plaintext) < len(key):
    plaintext += (len(key) - len(plaintext)) * "X"
else:
    plaintext = plaintext[:len(key)]

matrix_lengthKey = (math.sqrt(len(key)))
matrix_lengthPlaintext = (math.sqrt(len(plaintext)))

tableKey = [[0 for j in range(0, int(matrix_lengthKey))]
            for i in range(0, int(matrix_lengthKey))]

j = 0
i = 0

for k in key:
    if j >= matrix_lengthKey:
        j = 0
        i += 1
    tableKey[i][j] = ord(k) % 65
    j += 1

tablePlaintext = [[0 for j in range(0, int(matrix_lengthPlaintext))]
                  for i in range(0, int(matrix_lengthPlaintext))]

j = 0
i = 0

for k in plaintext:
    if j >= matrix_lengthPlaintext:
        j = 0
        i += 1
    tablePlaintext[i][j] = ord(k) % 65
    j += 1

result = [[0 for j in range(0, int(matrix_lengthPlaintext))]
          for i in range(0, int(matrix_lengthKey))]

for j in range(len(tablePlaintext)):
    for i in range(len(tableKey)):
        sum = 0
        for k in range(len(tableKey[i])):
            sum += (tableKey[i][k] * tablePlaintext[j][k])
            result[j][i] = sum % 26
encryptedText = ""

for i in range(len(result)):
    for j in range(len(result[0])):
        encryptedText += (chr(result[i][j] + 65))

print()
print(f"Encryption: {encryptedText}")
tempMatrix = [[0 for i in range(0, len(tableKey))] for j in range(0, len(tablePlaintext))]

for i in range(len(tableKey)):
    for j in range(len(tableKey[0])):
        tempMatrix[j][i] = tableKey[i][j]

A = Matrix(tempMatrix)
tempMatrix = A.adjugate().T.tolist()
determinant = A.det() % 26
multInverse = 0
for i in range(1, 27):
    if (determinant * i) % 26 == 1:
        multInverse = i
        break
else:
    print("No Possible Multiplcative Inverse")
    exit()

for i in range(len(tempMatrix)):
    for j in range(len(tempMatrix[0])):
        tempMatrix[i][j] = multInverse * tempMatrix[i][j] % 26

j = 0
i = 0
for k in encryptedText:
    if j >= matrix_lengthKey:
        j = 0
        i += 1
    tablePlaintext[i][j] = ord(k) % 65
    j += 1

for j in range(len(tablePlaintext)):
    for i in range(len(tempMatrix)):
        sum = 0
        for k in range(len(tempMatrix[i])):
            sum += (tempMatrix[i][k] * tablePlaintext[j][k])
            result[j][i] = sum % 26

decryptedText = ""
for i in range(len(result)):
    for j in range(len(result[0])):
        decryptedText += (chr(result[i][j] + 65))
print(f"Decryption: {decryptedText}")