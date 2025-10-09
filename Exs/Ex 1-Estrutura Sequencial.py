"""
Nome: Gabriel Mendes
Turma: PIPL0924
Trabalho: Ex 1 - Estrutura Sequencial

"""

import math

# Ex1
print("--"*3, "Exercício 1", "--"*3)

print ("Olá mundo!!")

# Ex2
print("--"*3, "Exercício 2", "--"*3)

num = int(input("Insira um número: "))

print(f"O número informado foi {num}")

# Ex3
print("--"*3, "Exercício 3", "--"*3)

num1 = int(input ("Insira um número: "))
num2 = int(input ("Insira um outro número: "))

print(num1 + num2)

# Ex4
print("--"*3, "Exercício 4", "--"*3)

nota = float(input("Insira a primeira nota do aluno: "))
nota1 = float(input("Insira a segunda do aluno: "))
nota2 = float(input("Insira a terceira do aluno: "))
nota3 = float(input("Insira a quarta do aluno: "))

print((nota+nota1+nota2+nota3)/4)

# Ex5
print("--"*3, "Exercício 5", "--"*3)

metros = float(input("Insira o valor em metros: "))
cent = metros * 100
print(f"{metros} metros equivalem a {cent} centímetros")

# Ex6
print("--"*3, "Exercício 6", "--"*3)

raio = float(input("Insira o raio do círculo: "))
area = math.pi * (raio ** 2)
print(f"A área do círculo é {area:.2f} m2")

# Ex7
print("--"*3, "Exercício 7", "--"*3)

lado = float(input("Insira o valor do lado do quadrado: "))
area = lado ** 2
dobro_da_area = 2 * area
print(f"A área do quadrado é {area:.2f}. \nO dobro da área é {dobro_da_area:.2f}")

# Ex8
print("--"*3, "Exercício 8", "--"*3)

ganho_por_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalha por mês? "))
salario = ganho_por_hora * horas_trabalhadas
print(f"O seu salário mensal é €{salario:.2f}")

# Ex9
print("--"*3, "Exercício 9", "--"*3)

fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)
print(f"A temperatura de {fahrenheit}°F é igual a {celsius:.2f}°C")

# Ex10
print("--"*3, "Exercício 10", "--"*3)

celsius = float(input("Insira a temperatura em Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"A temperatura de {celsius}°C é igual a {fahrenheit:.2f}°F.")

# Ex11
print("--"*3, "Exercício 11", "--"*3)

int1 = int(input("Insira o primeiro número inteiro: "))
int2 = int(input("Insira o segundo número inteiro: "))
real = float(input("Insira um número real: "))

prod = (2 * int1) * (int2 / 2)
soma = (3 * int1) + real
cubo = real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é {prod:.2f}.")
print(f"A soma do triplo do primeiro com o terceiro é {soma:.2f}.")
print(f"O terceiro elevado ao cubo é {cubo:.2f}.")
