"""
Nome: Gabriel Mendes
Turma: PIPL0924
Trabalho: Ex 4 - Funções

"""

import math

# Ex1
def ex1():
    print("--"*3, "Exercício 1", "--"*3)
    print("Olá, mundo!")

print(ex1)

# Ex2
def ex2():
    print("--"*3, "Exercício 2", "--"*3)
    num = input("Insira um número: ")
    print(f"O número informado foi {num}.")

print(ex2)

# Ex3
def ex3():
    print("--"*3, "Exercício 3", "--"*3)
    num1 = float(input("Insira um número: "))
    num2 = float(input("Insira um outro número: "))
    soma = num1 + num2
    print(f"A soma de {num1} + {num2} é igual a {soma}.")

print(ex3)

# Ex4
def ex4():
    print("--"*3, "Exercício 4", "--"*3)
    nota1 = float(input("Insira a primeira nota do aluno: "))
    nota2 = float(input("Insira a segunda nota do aluno: "))
    nota3 = float(input("Insira a terceira nota do aluno: "))
    nota4 = float(input("Insira a quarta nota do aluno: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"A média do aluno é {media:.2f}")

print(ex4)

# Ex5
def ex5():
    print("--"*3, "Exercício 5", "--"*3)
    metros = float(input("Insira o valor em metros: "))
    cent = metros * 100
    print(f"{metros} metros equivalem a {cent} centímetros")

print(ex5)

# Ex6
def ex6():
    print("--"*3, "Exercício 6", "--"*3)
    raio = float(input("Insira o raio do círculo: "))
    area = math.pi * (raio ** 2)
    print(f"A área do círculo é {area:.2f} m²")

print(ex6)

# Ex7
def ex7():
    print("--"*3, "Exercício 7", "--"*3)
    lado = float(input("Insira o valor do lado do quadrado: "))
    area = lado ** 2
    dobro = 2 * area
    print(f"A área do quadrado é {area:.2f}.")
    print(f"O dobro da área é {dobro:.2f}.")

print(ex7)

# Ex8
def ex8():
    print("--"*3, "Exercício 8", "--"*3)
    ganho_hora = float(input("Quanto você ganha por hora? "))
    horas_mes = float(input("Quantas horas você trabalha por mês? "))
    salario = ganho_hora * horas_mes
    print(f"O seu salário mensal é €{salario:.2f}")

print(ex8)

# Ex9
def ex9():
    print("--"*3, "Exercício 9", "--"*3)
    fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))
    celsius = 5 * ((fahrenheit - 32) / 9)
    print(f"A temperatura de {fahrenheit}°F é igual a {celsius:.2f}°C")

print(ex9)

# Ex10
def ex10():
    print("--"*3, "Exercício 10", "--"*3)
    celsius = float(input("Insira a temperatura em Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"A temperatura de {celsius}°C é igual a {fahrenheit:.2f}°F.")

print(ex10)

# Ex11
def ex11():
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

print(ex11)

# Ex12
def ex12():
    print("--"*3, "Exercício 1", "--"*3)
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
        
    if num1 > num2:
        print(f"O maior número é {num1}.")
    elif num2 > num1:
        print(f"O maior número é {num2}.")
    else:
        print("Os dois números são iguais.")

print(ex12)

# Ex13
def ex13():
    print("--"*3, "Exercício 2", "--"*3)
    valor = float(input("Insira um valor: "))
        
    if valor > 0:
        print(f"O valor {valor} é positivo.")
    elif valor < 0:
        print(f"O valor {valor} é negativo.")
    else:
        print("O valor é zero.")

print(ex13)

# Ex14
def ex14():
    print("--"*3, "Exercício 3", "--"*3)
    letra = input("Insira a letra F ou M: ").upper()

    if letra == 'F':
        print("Feminino")
    elif letra == 'M':
        print("Masculino")
    else:
        print("Sexo Inválido")

print(ex14)

# Ex15
def ex15():
    print("--"*3, "Exercício 4", "--"*3)
    letra = input("Insira uma letra: ").lower()
        
    if letra in 'aeiou':
        print(f"A letra {letra} é uma vogal.")
    elif letra.isalpha():
        print(f"A letra {letra} é uma consoante.")
    else:
        print("Por favor, digite uma letra válida.")

print(ex15)

# Ex16
def ex16():
    print("--"*3, "Exercício 5", "--"*3)
    nota1 = float(input("Insira a primeira nota: "))
    nota2 = float(input("Insira a segunda nota: "))
    media = (nota1 + nota2) / 2

    if media == 10:
        print("Aprovado com Distinção")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

print(ex16)

# Ex17
def ex17():
    print("--"*3, "Exercício 6", "--"*3)
    a = float(input("Insira o primeiro número: "))
    b = float(input("Insira o segundo número: "))
    c = float(input("Insira o terceiro número: "))

    maior = max(a, b, c)
    print(f"O maior número é {maior}\n")

print(ex17)

# Ex18
def ex18():
    print("--"*3, "Exercício 7", "--"*3)
    a = float(input("Insira o primeiro número: "))
    b = float(input("Insira o segundo número: "))
    c = float(input("Insira o terceiro número: "))

    maior = max(a, b, c)
    menor = min(a, b, c)
    print(f"O maior número é {maior}")
    print(f"O menor número é {menor}\n")

print(ex18)

# Ex19
def ex19():
    print("--"*3, "Exercício 8", "--"*3)
    p1 = float(input("Insira o preço do primeiro produto: "))
    p2 = float(input("Insira o preço do segundo produto: "))
    p3 = float(input("Insira o preço do terceiro produto: "))

    mais_barato = min(p1, p2, p3)

    if mais_barato == p1:
        produto = "Primeiro produto"
    elif mais_barato == p2:
        produto = "Segundo produto"
    else:
        produto = "Terceiro produto"

    print(f"Você deve comprar o {produto}, que custa {mais_barato:.2f}€\n")

print(ex19)

# Ex20
def ex20():
    print("--"*3, "Exercício 9", "--"*3)
    nums = []
    for i in range(3):
        n = float(input(f"Insira o {i+1}º número: "))
        nums.append(n)

    nums.sort(reverse=True)
    print("Números em ordem decrescente:", nums, "\n")

print(ex20)

# Ex21
def ex21():
    print("--"*3, "Exercício 10", "--"*3)
    turno = input("Insira o turno que você estuda (M-matutino / V-vespertino / N-noturno): ").strip().upper()

    if turno == 'M':
        print("Bom Dia!!!!!\n")
    elif turno == 'V':
        print("Boa Tarde!!!\n")
    elif turno == 'N':
        print("Boa Noite!!!!!\n")
    else:
        print("Valor Inválido!!!!!!!\n")

print(ex21)

# Ex22
def ex22():
    print("--"*3, "Exercício 11", "--"*3)
    salario = float(input("Insira o salário do colaborador (€): "))

    if salario <= 280:
        percentual = 20
    elif salario <= 700:
        percentual = 15
    elif salario <= 1500:
        percentual = 10
    else:
        percentual = 5

    aumento = salario * (percentual / 100)
    novo_salario = salario + aumento

    print(f"\nSalário antes do reajuste: {salario:.2f}€")
    print(f"Percentual de aumento aplicado: {percentual}%")
    print(f"Valor do aumento: {aumento:.2f}€")
    print(f"Novo salário após o aumento: {novo_salario:.2f}€")

print(ex22)

# Ex23
def ex23():
    print("--"*3, "Exercício 1", "--"*3)
    while True:
        nota = float(input("Insira uma nota entre 0 e 10: "))
        if 0 <= nota <= 10:
            print(f"Nota válida: {nota}")
            break
        else:
            print("Nota inválida!!!! Tente novamente.\n")


# Ex24
def ex24():
    print("--"*3, "Exercício 2", "--"*3)
    while True:
        usuario = input("Insira o nome de usuário: ")
        senha = input("Insira a senha: ")

        if senha == usuario:
            print("Erro: a senha não pode ser igual ao nome de usuário.\n")
        else:
            print("Usuário e senha cadastrados com sucesso!!!!!\n")
            break


# Ex25
def ex25():
    print("--"*3, "Exercício 3", "--"*3)
    while True:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        salario = float(input("Salário: "))
        sexo = input("Sexo (f/m): ").lower()
        estado_civil = input("Estado Civil (s, c, v, d): ").lower()

        if len(nome) <= 3:
            print("Erro: nome deve ter mais de 3 caracteres\n")
        elif not (0 <= idade <= 150):
            print("Erro: idade deve estar entre 0 e 150\n")
        elif salario <= 0:
            print("Erro: salário deve ser maior que zero\n")
        elif sexo not in ['f', 'm']:
            print("Erro: sexo deve ser 'f' ou 'm'\n")
        elif estado_civil not in ['s', 'c', 'v', 'd']:
            print("Erro: estado civil inválido.\n")
        else:
            print("Informações válidas!!!!!\n")
            break


# Ex26
def ex26():
    print("--"*3, "Exercício 4", "--"*3)
    popA = 80000
    popB = 200000
    taxaA = 0.03
    taxaB = 0.015
    anos = 0

    while popA < popB:
        popA += popA * taxaA
        popB += popB * taxaB
        anos += 1

    print(f"Levará {anos} anos para a população do país A ultrapassar ou igualar a do país B.\n")


# Ex27
def ex27():
    print("--"*3, "Exercício 5", "--"*3)
    while True:
        popA = int(input("Informe a população do país A: "))
        taxaA = float(input("Informe a taxa de crescimento do país A (em %): "))
        popB = int(input("Informe a população do país B: "))
        taxaB = float(input("Informe a taxa de crescimento do país B (em %): "))

        if popA <= 0 or popB <= 0 or taxaA <= 0 or taxaB <= 0:
            print("Todos os valores devem ser maiores que zero\n")
            continue

        taxaA /= 100
        taxaB /= 100
        anos = 0

        while popA < popB:
            popA += popA * taxaA
            popB += popB * taxaB
            anos += 1

        print(f"Serão necessários {anos} anos para A ultrapassar ou igualar B\n")

        repetir = input("Deseja repetir a operação? (s/n): ").lower()
        if repetir != 's':
            break


# Ex28
def ex28():
    print("--"*3, "Exercício 6", "--"*3)
    print("Números de 1 a 20 (um abaixo do outro):")
    for i in range(1, 21):
        print(i)

    print("\nNúmeros de 1 a 20 (um ao lado do outro):")
    for i in range(1, 21):
        print(i, end=" ")
    print("\n")


# Ex29
def ex29():
    print("--"*3, "Exercício 7", "--"*3)
    maior = None
    for i in range(5):
        num = float(input(f"Digite o {i+1}º número: "))
        if maior is None or num > maior:
            maior = num
    print(f"O maior número é: {maior}\n")


# Ex30
def ex30():
    print("--"*3, "Exercício 8", "--"*3)
    soma = 0
    for i in range(5):
        num = float(input(f"Insira o {i+1}º número: "))
        soma += num
    media = soma / 5
    print(f"Soma dos números: {soma}")
    print(f"Média dos números: {media}\n")


# Ex31
def ex31():
    print("--"*3, "Exercício 9", "--"*3)
    print("Números ímpares entre 1 e 50:")
    for i in range(1, 51):
        if i % 2 != 0:
            print(i, end=" ")
    print("\n")


# Ex32
def ex32():
    print("--"*3, "Exercício 10", "--"*3)
    inicio = int(input("Insira o primeiro número: "))
    fim = int(input("Insira o segundo número: "))

    if inicio > fim:
        inicio, fim = fim, inicio  # garante ordem crescente

    print(f"Números entre {inicio} e {fim}:")
    for i in range(inicio + 1, fim):
        print(i, end=" ")
    print("\n")


# Ex33
def ex33():
    print("--"*3, "Exercício 11", "--"*3)
    inicio = int(input("Insira o primeiro número: "))
    fim = int(input("Insira o segundo número: "))

    if inicio > fim:
        inicio, fim = fim, inicio

    soma = 0
    print(f"Números entre {inicio} e {fim}:")
    for i in range(inicio + 1, fim):
        print(i, end=" ")
        soma += i

    print(f"\nSoma dos números no intervalo: {soma}\n")


# Ex34
def ex34():
    print("--"*3, "Exercício 12", "--"*3)
    num = int(input("Insira um número para ver sua tabuada (1 a 10): "))

    if 1 <= num <= 10:
        print(f"\nTabuada de {num}:")
        for i in range(1, 11):
            print(f"{num} X {i} = {num * i}")
    else:
        print("Número inválido! Digite entre 1 e 10.")
