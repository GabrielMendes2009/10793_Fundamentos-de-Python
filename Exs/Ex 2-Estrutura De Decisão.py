"""
Nome: Gabriel Mendes
Turma: PIPL0924
Trabalho: Ex 2 - Estrutura De Decisão

"""

# Ex1
print("--"*3, "Exercício 1", "--"*3)

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
    
if num1 > num2:
    print(f"O maior número é {num1}.")
elif num2 > num1:
    print(f"O maior número é {num2}.")
else:
    print("Os dois números são iguais.")

# Ex2
print("--"*3, "Exercício 2", "--"*3)

valor = float(input("Insira um valor: "))
    
if valor > 0:
    print(f"O valor {valor} é positivo.")
elif valor < 0:
    print(f"O valor {valor} é negativo.")
else:
    print("O valor é zero.")

# Ex3
print("--"*3, "Exercício 3", "--"*3)

letra = input("Insira a letra F ou M: ").upper()

if letra == 'F':
    print("Feminino")
elif letra == 'M':
    print("Masculino")
else:
    print("Sexo Inválido")

# Ex4
print("--"*3, "Exercício 4", "--"*3)

letra = input("Insira uma letra: ")
    
if letra in 'aeiou':
    print(f"A letra {letra} é uma vogal.")
elif letra.isalpha():
    print(f"A letra {letra} é uma consoante.")
else:
    print("Por favor, digite uma letra válida.")

# Ex5
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

# Ex6
print("--"*3, "Exercício 6", "--"*3)
a = float(input("Insira o primeiro número: "))
b = float(input("Insira o segundo número: "))
c = float(input("Insira o terceiro número: "))

maior = max(a, b, c)
print(f"O maior número é {maior}\n")


# Ex7
print("--"*3, "Exercício 7", "--"*3)
a = float(input("Insira o primeiro número: "))
b = float(input("Insira o segundo número: "))
c = float(input("Insira o terceiro número: "))

maior = max(a, b, c)
menor = min(a, b, c)
print(f"O maior número é {maior}")
print(f"O menor número é {menor}\n")


# Ex8
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


# Ex9
print("--"*3, "Exercício 9", "--"*3)
nums = []
for i in range(3):
    n = float(input(f"Insira o {i+1}º número: "))
    nums.append(n)

nums.sort(reverse=True)
print("Números em ordem decrescente", nums, "\n")


# Ex10
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


# Ex11
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

