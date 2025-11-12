"""
Nome: Gabriel Mendes
Turma: PIPL0924
Trabalho: Ex8 - revisões  
"""

def maiorNumero(lista):
    # Aqui inicio o maior número com o primeiro elemento da lista
    maior = lista[0]
    # Anda por toda a lista para encontrar o maior número
    for num in lista:
        if num > maior:
            maior = num
    return maior

def menorNumero(lista):
    # Aqui inicio o menor número com o primeiro elemento da lista
    menor = lista[0]
    # Percorre toda a lista para encontrar o menor número
    for num in lista:
        if num < menor:
            menor = num
    return menor

def main():
    numeros = []

    # Aqui peço ao usuário quantos números ele deseja inserir com um loop while
    while True:
        try:
            quantidade = int(input("Quantos números deseja inserir? "))
            if quantidade <= 0:
                print("Insira um número positivo!!!!")
                continue
            break
        except ValueError:
            print("Valor inválido. Insira um número inteiro!!!!")

    # Aqui peço ao usário que insira o valor dos números desejados e inseridos anteriormente
    for i in range(quantidade):
        while True:
            try:
                numero = float(input(f"Insira o {i + 1}º número: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Valor inválido. Insira um número válido!!!!")

    # Aqui estou chamando as funções para encontrar o maior e o menor número
    maior = maiorNumero(numeros)
    menor = menorNumero(numeros)

    # Aqui estou imprimindo o maior e o menor número inserido pelo usuário anteriormente
    print(f"O maior número inserido é: {maior}")
    print(f"O menor número inserido é: {menor}")

# Aqui estou chamando a função main para rodar o programa
if __name__ == "__main__":
    main()
