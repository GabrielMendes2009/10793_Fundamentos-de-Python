"""
Hoje S2

Funcs

Arrays e listas

"""

def ola_mundo():
    print("Olá mundo!")

ola_mundo()
ola_mundo()


def ola_mundo1(nome):
    print(f"Olá mundo!, {nome}")

ola_mundo1("Gonçalo")
ola_mundo1("João")

def ola_mundo2(nome, idade:int):
    print(f"Olá mundo, {nome.upper()}, {idade}")

ola_mundo2(nome = "Carlos", idade = 20)

def ola_mundo3(nome:str, idade:int):

    print(f"Olá Mundo, {nome}, {idade}")

ola_mundo3(nome = "Carlos", idade = 20)

ola_mundo3(nome = 41, idade=20)

v=10
print(v)
v="Gonçalo"
print(v)
v=True

def ola_mundo4(nome:str, idade:int):
    return f"Olá mundo, {nome}, {idade}"

msg1 = ola_mundo4(nome="Carlos", idade=20)
msg2 = ola_mundo4(nome="Joao", idade=20)

print("--"*10)
print(msg1)
print("--"*10)
print(msg2)

def ola_mundo5(nome:str, idade:int):
    return f"Ola Mundo, {nome}, {idade}"

msg3 = ola_mundo5(nome="Joao", idade=20)




# Faça um programa que leia três números e mostre o maior deles.
# var
# opr com var
# condições

"""

v1
v2
v3


"""

print("---"*5)
def ola_mundo6(nome:str, idade:int):
    return f"Ola Mundo, {nome}, {idade}"

msg4 = ola_mundo6(nome="Joao", idade=20)
print(msg4)

msg5 = ola_mundo6(idade=20, nome="Joao")
print(msg5)

print("---"*5)
def ola_mundo7(nome:str, idade:int = 18):
    return f"Ola Mundo, {nome}, {idade}"

msg6 = ola_mundo7(nome="Joao")
print(msg6)

msg7 = ola_mundo7(nome="Joao", idade=25)
print(msg7)

print("---"*5)

x=2
def demo():
    x=10
demo()

print(x)

print("---"*5)

def soma(a,b):
    return a+b

print(soma(a=1, b=2))

print(soma(soma(a=1, b=2, ), soma(a=1, b=2)))