"""
Nome: Gabriel Mendes
Turma: PIPL0924
Trabalho: Ex 4 - Estrutura Sequencial

"""

import math

# Ex1
def ola_mundo():
    print("Olá, mundo!")

print(ola_mundo)

# Ex2
def mostrar_numero():
    num = input("Insira um número: ")
    print(f"O número informado foi {num}.")

print(mostrar_numero)

# Ex3
def somar_numeros():
    num1 = float(input("Insira um número: "))
    num2 = float(input("Insira um outro número: "))
    soma = num1 + num2
    print(f"A soma de {num1} + {num2} é igual a {soma}.")

print(somar_numeros)

# Ex4
def ex4_media_notas():
    print("--"*3, "Exercício 4", "--"*3)
    nota1 = float(input("Insira a primeira nota do aluno: "))
    nota2 = float(input("Insira a segunda nota do aluno: "))
    nota3 = float(input("Insira a terceira nota do aluno: "))
    nota4 = float(input("Insira a quarta nota do aluno: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"A média do aluno é {media:.2f}")


# Ex5
def ex5_metros_para_centimetros():
    print("--"*3, "Exercício 5", "--"*3)
    metros = float(input("Insira o valor em metros: "))
    cent = metros * 100
    print(f"{metros} metros equivalem a {cent} centímetros")


# Ex6
def ex6_area_circulo():
    print("--"*3, "Exercício 6", "--"*3)
    raio = float(input("Insira o raio do círculo: "))
    area = math.pi * (raio ** 2)
    print(f"A área do círculo é {area:.2f} m²")


# Ex7
def ex7_area_quadrado():
    print("--"*3, "Exercício 7", "--"*3)
    lado = float(input("Insira o valor do lado do quadrado: "))
    area = lado ** 2
    dobro = 2 * area
    print(f"A área do quadrado é {area:.2f}.")
    print(f"O dobro da área é {dobro:.2f}.")


# Ex8
def ex8_salario_mensal():
    print("--"*3, "Exercício 8", "--"*3)
    ganho_hora = float(input("Quanto você ganha por hora? "))
    horas_mes = float(input("Quantas horas você trabalha por mês? "))
    salario = ganho_hora * horas_mes
    print(f"O seu salário mensal é €{salario:.2f}")


# Ex9
def ex9_fahrenheit_para_celsius():
    print("--"*3, "Exercício 9", "--"*3)
    fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))
    celsius = 5 * ((fahrenheit - 32) / 9)
    print(f"A temperatura de {fahrenheit}°F é igual a {celsius:.2f}°C")


# Ex10
def ex10_celsius_para_fahrenheit():
    print("--"*3, "Exercício 10", "--"*3)
    celsius = float(input("Insira a temperatura em Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"A temperatura de {celsius}°C é igual a {fahrenheit:.2f}°F.")


# Ex11
def ex11_operacoes_numeros():
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