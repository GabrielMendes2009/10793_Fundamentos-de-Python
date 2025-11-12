lst = [12,31,12,3,12,4,12,41,3,130]


nova_lst = []
for i in lst:
    nova_lst.append(i*2)

print(nova_lst)


print("------ List Comprehension ----- ")


# nova_lst [exp for valor in lst if condição]


nova_lst2 = [i * 2 for i in lst]
print(nova_lst2)


"""

crie uma lista com 10 num inteiros 
recorrendo ao List Comprehension crie uma nova lista que guarde o triplo de cada um dos valores na lista original 

"""


lst3 = [1,2,3,4,5,6,7,8,9,10]
nova_lst3 = [i * 3 for i in lst3]



print("----")


x = "12"

x_int = int(x)



print(x_int)

print(float(x))
print(str(x))
print(bool(x))

print("----")


"""

crie uma lista com 10 str com numeros inteiros ["1", "3",..., "41"]
recorrendo ao List Comprehension crie uma nova lista que guarde os valores na lista original como inteiro 

"""

x = "12"
x_int = int(x)


lst4 = ["1","2","3","4","5","6","7","8","9","10"]


lst4_int = [int(i) for i in lst4]


print("------ List Comprehension --- Condições ----- ")

lst = [12,31,12,3,12,4,12,41,3,130]


par = [x for x in lst if x % 2 == 0]
print(par)

impar = [x for x in lst if x % 2 != 0]
print(impar)


print("----")

print("12".isnumeric())


"""

Cire uma lista com 15 strings, umas numéricas e outas não, crie uma nova lista so com as numéricas guardadas como int 

"""

lst = ["Arvore", "2", "zezo", "6", "46", "Arroz", "luis", "4", "43", "84", "53", "GodOFWar", "32", "42", "Quinze" ]
onlyNums = [int(i) for i in lst if i.isnumeric()]
print(onlyNums)


print("------ List Comprehension --- mtx ----- ")


mtx = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#
# [<exp baseada no elm lista> for <elm lista> in <Lista> ]
#
mtx_dobro = [[x * 2 for x in linha ] for linha in mtx]
print(mtx_dobro)