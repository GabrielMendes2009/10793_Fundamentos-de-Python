"""

tipos de dados
var
op com var
    +
    -
    / -> float
    *
    % -> Modulo (Mod)  <- (resto)
    // -> div inteira -> int
condições
    if-elif-else
    match-case

range -> seq de num int

loop
    for
    while
collections
    list
        list slicing -> [1:15:4]
        List comprehension
    dict
    set
    tuple

func (def)
    param
    return

try - except

"""

print(10/2) # 5.0
print(10//5)

print(10 + 2)

print(10 + 2.0)


mySet = {1,2,3,4,5,6}
print(type(mySet))
print(mySet)
print(mySet.add(10))
print(mySet.add(10))
print(mySet)

myTuple = (1,2,3)
print(type(myTuple))
print(myTuple)
print(myTuple[0])

print("--- for x in myTuple: ---")
for x in myTuple:
    print(x)

print("--- for x in mySet: ---")
for x in mySet:
    print(x)


print("--- funções: ---")
def nome():
    print("Ola")

nome()

# Crie uma função que some dois números recebidos como param

def soma():
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))
    res = num1 + num2
    print(res)

def soma2(num1, num2):
    res = num1 + num2
    return res


res_soma = soma2(2,4)
print(".... codigo e mais codigo....")

print(res_soma)

res_soma2 = soma2(res_soma,4)

print(res_soma2)




"""

Crie um programa que peça ao utilizador quantos números quer inserir, 
    em seguida paça ao utilizador essa quantidade de números e adicione-os a uma lista

Crie um conjunto de funções para achar o maior e o menor (sem usar o max nem min), 
    estes valores so devem ser calculados quando terminar de inserir os números 
     
moste o resultado (qual o maior e menor valor)

deve garantir que caso o utilizador insira um valor não numérico programa não da erro   
"""