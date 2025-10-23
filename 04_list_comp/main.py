"""
var
tipos de dados
op com var
in/out

condições 
    if
    match-case

range

loops
    for
    while

func

listas
    criar
    add fim
    add inicio meio
    remover ultimo
    remover inicio meio
    aceder a um elem
    list slicing [1:10]

    list comp


"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


nova_lista = []


for i in lst:
    if i % 2 == 0:
        nova_lista.append(1)


print(nova_lista)

nova_lista2 = list(lst)
print(nova_lista2)


"""

nova_lista = [exp for item in lista]


"""
lst = [1,2,3,4,5,6,7,8,9,10]

nova_lista3 = [item for item in lst]

print(nova_lista3)

"""

nova_lista = [exp for item in lista]


"""

nova_lista4 = [item * 2 for item in lst if item % 2 == 0]

print(nova_lista)
print(nova_lista4)

def dobro(x):
    return x * 2

nova_lista5 = [dobro(num) for num in lst if num % 2 == 0]



lst.extend()




cidades = ["Lisboa", "Porto", "Coimbra", "Braga", "Faro"
           "Aveiro", "Évora", "Funchal", "Viseu", "Leiria"]

for cidade in cidades:
    print(cidade)


t = ("nome", "Turma", "Nota")
a, b, c = t

print(c)

nova_var = 1,4,1

print(type(nova_var))

