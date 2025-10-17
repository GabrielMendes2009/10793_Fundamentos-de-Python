"""
Nome: Gabriel Mendes
Turma: PIPL0924
Trabalho: Ex 3 - Estrutura De Repetição

"""

# Ex1
print("--"*3, "Exercício 1", "--"*3)

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print(f"Nota válida: {nota}")
        break
    else:
        print("Valor inválido! Tente novamente.\n")


# Ex2
print("--"*3, "Exercício 2", "--"*3)

while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if senha == usuario:
        print("Erro: a senha não pode ser igual ao nome de usuário.\n")
    else:
        print("Usuário e senha cadastrados com sucesso!\n")
        break


# Ex3
print("--"*3, "Exercício 3", "--"*3)

while True:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    salario = float(input("Salário: "))
    sexo = input("Sexo (f/m): ").lower()
    estado_civil = input("Estado Civil (s, c, v, d): ").lower()

    if len(nome) <= 3:
        print("Erro: nome deve ter mais de 3 caracteres.\n")
    elif not (0 <= idade <= 150):
        print("Erro: idade deve estar entre 0 e 150.\n")
    elif salario <= 0:
        print("Erro: salário deve ser maior que zero.\n")
    elif sexo not in ['f', 'm']:
        print("Erro: sexo deve ser 'f' ou 'm'.\n")
    elif estado_civil not in ['s', 'c', 'v', 'd']:
        print("Erro: estado civil inválido.\n")
    else:
        print("Informações válidas!\n")
        break


# Ex4
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


# Ex5
print("--"*3, "Exercício 5", "--"*3)

while True:
    popA = int(input("Informe a população do país A: "))
    taxaA = float(input("Informe a taxa de crescimento do país A (em %): "))
    popB = int(input("Informe a população do país B: "))
    taxaB = float(input("Informe a taxa de crescimento do país B (em %): "))

    if popA <= 0 or popB <= 0 or taxaA <= 0 or taxaB <= 0:
        print("Todos os valores devem ser maiores que zero.\n")
        continue

    taxaA /= 100
    taxaB /= 100
    anos = 0

    while popA < popB:
        popA += popA * taxaA
        popB += popB * taxaB
        anos += 1

    print(f"Serão necessários {anos} anos para A ultrapassar ou igualar B.\n")

    repetir = input("Deseja repetir a operação? (s/n): ").lower()
    if repetir != 's':
        break


# Ex6
print("--"*3, "Exercício 6", "--"*3)

print("Números de 1 a 20 (um abaixo do outro):")
for i in range(1, 21):
    print(i)

print("\nNúmeros de 1 a 20 (um ao lado do outro):")
for i in range(1, 21):
    print(i, end=" ")
print("\n")


# Ex7
print("--"*3, "Exercício 7", "--"*3)

maior = None
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    if maior is None or num > maior:
        maior = num

print(f"O maior número é: {maior}\n")


# Ex8
print("--"*3, "Exercício 8", "--"*3)

soma = 0
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    soma += num

media = soma / 5
print(f"Soma dos números: {soma}")
print(f"Média dos números: {media}\n")


# Ex9
print("--"*3, "Exercício 9", "--"*3)

print("Números ímpares entre 1 e 50:")
for i in range(1, 51):
    if i % 2 != 0:
        print(i, end=" ")
print("\n")


# Ex10
print("--"*3, "Exercício 10", "--"*3)

inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

if inicio > fim:
    inicio, fim = fim, inicio  # garante ordem crescente

print(f"Números entre {inicio} e {fim}:")
for i in range(inicio + 1, fim):
    print(i, end=" ")
print("\n")


# Ex11
print("--"*3, "Exercício 11", "--"*3)

inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

if inicio > fim:
    inicio, fim = fim, inicio

soma = 0
print(f"Números entre {inicio} e {fim}:")
for i in range(inicio + 1, fim):
    print(i, end=" ")
    soma += i

print(f"\nSoma dos números no intervalo: {soma}\n")


# Ex12
print("--"*3, "Exercício 12", "--"*3)

num = int(input("Digite um número para ver sua tabuada (1 a 10): "))

if 1 <= num <= 10:
    print(f"\nTabuada de {num}:")
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
else:
    print("Número inválido! Digite entre 1 e 10.")

