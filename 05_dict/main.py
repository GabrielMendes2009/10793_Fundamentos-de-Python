
# "nome" e 'nome'


# print(" o 'Joao' tem 20 anos")

# print('o "Joao" tem 20 anos')


# print('o \'Joao\' tem 20 anos')
# print("o \"Joao\" tem 20 anos")
"""

dict :
    criar
    add
    ler
    remover


CRUD ?
"""

aluno = {'nome': "Joao", "idade": 19}

print(aluno)
print(aluno["nome"])

aluno["turma"] = "PIPL0924"


print(aluno)
print(aluno["turma"])


aluno.pop("turma")

print(aluno)



print(aluno.get("turma"))

"""
em q situações usar aluno.get("turma")?
em q situações usar aluno["turma"]?

"""

print(aluno)
aluno.popitem()
print(aluno)



aluno = {'nome': "Joao", "idade": 19, "turma": "PIPL0924", "sexo": "M", "Aprovado": False}

print(aluno.items())
print(aluno.keys().__contains__("turma"))
print(aluno.values())


print("----------")
for elm in aluno:
    print(elm)

print("-----Equivalente -----")
for elm in aluno.keys():
    print(elm)

# {key: value, chave:Valor}
print("----------")

# como mostrar todos os valores
for elm in aluno.values():
    print(elm)


# como mostrar todos os par chave:valor
for elm in aluno.items():
    print(elm)



aluno = {'nome': "Joao", "Aprovado": False, "nome": "Maria", "nome": "Rita"}
print(aluno)