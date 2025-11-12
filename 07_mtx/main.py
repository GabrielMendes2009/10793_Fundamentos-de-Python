"""

o que e uma matriz

lst = [1,2,3]


mtx = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

"""

mtx = [[1,2,3],[4,5,6],[7,8,9]]

print(mtx)
print("-------")
print(mtx[0])
print(mtx[1])
print(mtx[2])

print("-------")

linha1 = mtx[0]
val1_linha1 = linha1[0]

print(val1_linha1)


print("-------")

linha1 = mtx[0][0] # mtx[linha][col]

print(val1_linha1)

print("-------")

# linha1 = mtx[0, 0] # com list nao funciona

# print(val1_linha1)

print("-------")


for linha in mtx:
    print(linha)

print("-------")

for linha in mtx:
    for coluna in linha:
        print(coluna, end=' ')
    print()

print("-------")

mtx2 = [[[10,11,12],[13,14,15],[16,17,18]],[4,5,6],[7,8,9]]

print(mtx2)
print("-------")
for linha in mtx2:
    for coluna in linha:
        print(coluna, end=' ')
    print()


print(mtx2[0])
print(mtx2[0][0])
print(mtx2[0][0][0])