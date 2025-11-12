"""

Nome: GabrieL Mendes
Turma: PIPL0924
Trabalho: Ex7 - ListComp

"""

#Programa 1
numeros = [10, -3, 25, -7, 0, 8, -1, 14, -20, 5]

copia_numeros = numeros.copy()

positivos = []
negativos = []
quadrados = []
pares = []
impares = []

for num in numeros:
    if num >= 0:
        positivos.append(num)
    else:
        negativos.append(num)

    quadrados.append(num ** 2)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(copia_numeros)
print(positivos)
print(negativos)
print(quadrados)
print(pares)
print(impares)

print("-----------------------")

#Programa 2
frase = input("Digite uma frase: ")

vogais = []
for char in frase:
    if char.lower() in 'aeiou':
        vogais.append(char)

palavras = frase.split()

tamanho_palavra = []
palavra_minuscula = []
palavra_grande = []
primeira_letra = []
palavras_invertida = []
tupla_palavra = []
hashtags = []

for palavra in palavras:
    limpa = palavra.strip('.,!?')

    tamanho_palavra.append(len(limpa))

    palavra_minuscula.append(limpa.lower())

    if len(limpa) >= 5:
        palavra_grande.append(limpa)

    if len(limpa) > 0:
        primeira_letra.append(limpa[0])

    palavras_invertida.append(limpa[::-1])

    tupla_palavra.append((limpa, len(limpa)))

    if palavra.startswith('#'):
        hashtags.append(palavra[1:])

vogais_unicas_ordenadas = sorted(set(char.lower() for char in frase if char.lower() in 'aeiou'))

print(vogais)
print(tamanho_palavra)
print(palavra_minuscula)
print(palavra_grande)
print(primeira_letra)
print(palavras_invertida)
print(tupla_palavra)
print(hashtags)
print(vogais_unicas_ordenadas)
