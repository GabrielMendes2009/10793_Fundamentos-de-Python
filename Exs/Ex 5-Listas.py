"""

Nome: Gabriel Mendes
Turma: PIPL0924
Trabalho: Ex 5 - Listas

"""

# Ex1
print("--"*3, "Exercício 1", "--"*3)
def ex1(n):
    for i in range(1, n + 1):
        linha = [i] * i
        print(*linha)

print(ex1())

# Ex2
print("--"*3, "Exercício 2", "--"*3)
def ex2(n):
    for i in range(1, n + 1):
        linha = list(range(1, i + 1))
        print(*linha)
    
print(ex2())

# Ex3
print("--"*3, "Exercício 3", "--"*3)
def ex3():
    nums = []
    for i in range(5):
        nums.append(int(input(f"Insira o {i+1}º número inteiro: ")))
    print("Números digitados:", nums)

print(ex3())

# Ex4
print("--"*3, "Exercício 4", "--"*3)
def ex4():
    nums = []
    for i in range(10):
        nums.append(float(input(f"Insira o {i+1}º número real: ")))
    print("Números na ordem inversa:", nums[::-1])

print(ex4())

# Ex5
print("--"*3, "Exercício 5", "--"*3)
def ex5():
    notas = []
    for i in range(4):
        notas.append(float(input(f"Insira a {i+1}ª nota: ")))
    media = sum(notas) / len(notas)
    print("Notas:", notas)
    print("Média:", media)

print(ex5())

# Ex6
print("--"*3, "Exercício 6", "--"*3)
def ex6():
    vetor = []
    consoantes = []
    for i in range(10):
        letra = input(f"Insira o {i+1}º caractere: ").lower().strip()
        vetor.append(letra)
        if letra.isalpha() and letra not in "aeiou":
            consoantes.append(letra)
    print("Consoantes lidas:", consoantes)
    print("Quantidade de consoantes:", len(consoantes))

print(ex6())

# Ex7
print("--"*3, "Exercício 7", "--"*3)
def ex7():
    numero = []
    par = []
    impar = []
    for i in range(20):
        num = int(input(f"Insira o {i+1}º número inteiro: "))
        numero.append(num)
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    print("Todos:", numero)
    print("Pares:", par)
    print("Ímpares:", impar)

print(ex7())

# Ex8
print("--"*3, "Exercício 8", "--"*3)
def ex8():
    medias = []
    for i in range(10):
        notas = []
        print(f"\nAluno {i+1}:")
        for j in range(4):
            notas.append(float(input(f"Insira a {j+1}ª nota: ")))
        media = sum(notas) / 4
        medias.append(media)
    print("\nMédias dos alunos:", medias)
    print("Alunos com média >= 7:", sum(m >= 7 for m in medias))

print(ex8())

# Ex9
print("--"*3, "Exercício 9", "--"*3)
def ex9():
    vetor = []
    for i in range(5):
        vetor.append(int(input(f"Insira o {i+1}º número: ")))
    soma = sum(vetor)
    mult = 1
    for v in vetor:
        mult *= v
    print("Números:", vetor)
    print("Soma:", soma)
    print("Multiplicação:", mult)

print(ex9())

# Ex10
print("--"*3, "Exercício 10", "--"*3)
def ex10():
    idades = []
    alturas = []
    for i in range(5):
        idades.append(int(input(f"Insira a idade da {i+1}ª pessoa: ")))
        alturas.append(float(input(f"Insira a altura da {i+1}ª pessoa: ")))
    print("\nOrdem inversa:")
    for i in range(4, -1, -1):
        print(f"Idade: {idades[i]} | Altura: {alturas[i]:.2f}")

print(ex10())

# Ex11
print("--"*3, "Exercício 11", "--"*3)
def ex11():
    A = []
    for i in range(10):
        A.append(int(input(f"Insira o {i+1}º número: ")))
    soma = sum(x**2 for x in A)
    print("Soma dos quadrados:", soma)

print(ex11())

# Ex12
print("--"*3, "Exercício 12", "--"*3)
def ex12():
    A, B = [], []
    for i in range(10):
        A.append(int(input(f"A[{i+1}]: ")))
    for i in range(10):
        B.append(int(input(f"B[{i+1}]: ")))
    C = []
    for i in range(10):
        C.append(A[i])
        C.append(B[i])
    print("Vetor intercalado:", C)

print(ex12())

# Ex13
print("--"*3, "Exercício 13", "--"*3)
def ex13():
    A, B, C = [], [], []
    for i in range(10):
        A.append(int(input(f"A[{i+1}]: ")))
    for i in range(10):
        B.append(int(input(f"B[{i+1}]: ")))
    for i in range(10):
        C.append(int(input(f"C[{i+1}]: ")))
    D = []
    for i in range(10):
        D.extend([A[i], B[i], C[i]])
    print("Vetor intercalado:", D)

print(ex13())

# Ex14
print("--"*3, "Exercício 14", "--"*3)
def ex14():
    idade = []
    altura = []
    for i in range(30):
        print(f"\nAluno {i+1}:")
        idade.append(int(input("Idade: ")))
        altura.append(float(input("Altura: ")))
    media_altura = sum(altura) / len(altura)
    count = sum(1 for i in range(30) if idade[i] > 13 and altura[i] < media_altura)
    print(f"\nMédia de altura: {media_altura:.2f}")
    print("Alunos > 13 anos com altura < média:", count)

print(ex14())

# Ex15
print("--"*3, "Exercício 15", "--"*3)
def ex15():
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    temperatura = []
    for i in range(12):
        temperatura.append(float(input(f"Temperatura média de {meses[i]}: ")))
    media_anual = sum(temperatura) / 12
    print(f"\nMédia anual: {media_anual:.2f}")
    print("Meses com temperatura acima da média:")
    for i in range(12):
        if temperatura[i] > media_anual:
            print(f"{meses[i]}: {temperatura[i]:.2f}")

print(ex15())
