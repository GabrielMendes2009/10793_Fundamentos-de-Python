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
