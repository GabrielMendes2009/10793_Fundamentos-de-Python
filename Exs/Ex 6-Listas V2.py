"""

Nome: Gabriel Mendes
Turma: PIPL0924
Trabalho: Ex 6 - Listas V2

"""

#ex1
def ex1():
    perg = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
    
    respostas = []
    for pergunta in perg:
        resposta = input(pergunta + " (s/n): ").strip().lower()
        respostas.append(resposta)
    
    sim = respostas.count("s")
    nao = respostas.count("n")

    if sim == 2 and nao == 3:
        print("\nSuspeito\n")
    elif 3 <= sim <= 4:
        print("\nCúmplice\n")
    elif sim == 5 and nao == 0:
        print("\nAssassino\n")
    elif nao == 5 and sim == 0:
        print("\nInocente\n")
    else:
        print("\nDados inserido corretamente!!!\n")
ex1()

#ex2
def ex2():
    notas = []
    while True:
        valor = float(input("Insira uma nota (-1 para sair): "))
        if valor == -1:
            break
        notas.append(valor)
    
    if len(notas) == 0:
        print("Nenhuma nota informada")
        return

    print("\nQuantidade de Notas escritas:", len(notas))
    print("Notas informadas:", notas)
    
    print("\nNotas na ordem inversa: ")
    for n in reversed(notas):
        print(n)
    
    soma = sum(notas)
    media = soma/len(notas)
    
    print(f"\nSoma das notas: {soma}")
    print(f"Média das notas: {media:.2f}")
    
    acima_media = sum(1 for n in notas if n > media)
    abaixo_sete = sum(1 for n in notas if n < 7)
    
    print(f"Quantidade de notas acima da média: {acima_media}")
    print(f"Quantidade de notas abaixo de 7: {abaixo_sete}\n")
ex2()

#ex3
def ex3():
    salarios = [0] * 9
    
    while True:
        vendas = input("Insira o valor das vendas do vendedor (ou 's' para encerrar): ")
        if vendas.lower() == "s":
            break
        
        vendas = float(vendas)
        salario = 200 + 0.09 * vendas
        
        indice = int(salario // 100) - 2
        if indice >= 8:
            indice = 8
        elif indice < 0:
            indice = 0
        salarios[indice] += 1

    print("\nDistribuição dos salários:")
    intervalos = [
        "$200 - $299",
        "$300 - $399",
        "$400 - $499",
        "$500 - $599",
        "$600 - $699",
        "$700 - $799",
        "$800 - $899",
        "$900 - $999",
        "$1000 em diante"
    ]
    for i in range(len(intervalos)):
        print(f"{intervalos[i]}: {salarios[i]} vendedores")

ex3()

#ex4
def ex4():
    while True:
        nome = input("Nome do atleta (ou ENTER para sair): ").strip()
        if nome == "":
            break
        
        saltos = []
        for i in range(1, 6):
            distancia = float(input(f"Insira a distância do {i}º salto: "))
            saltos.append(distancia)
        
        media = sum(saltos)/len(saltos)
        
        print(f"\nAtleta: {nome}\n")
        print(f"Primeiro Salto: {saltos[0]} m")
        print(f"Segundo Salto: {saltos[1]} m")
        print(f"Terceiro Salto: {saltos[2]} m")
        print(f"Quarto Salto: {saltos[3]} m")
        print(f"Quinto Salto: {saltos[4]} m")

        print("\nResultado Final")
        print(f"Atleta: {nome}")
        print("Saltos: " + " - ".join([str(s) for s in saltos]))
        print(f"Média dos saltos: {media:.2f} m\n")
ex4()

