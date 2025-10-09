"""
tipo de dados?

bool
int
str
float
    double
char

---------------------------------

if - elif- else

match - case ? <- py 3.10

---------------------------------

int + int -> int
int - int -> int
int * int -> int
int / int -> float

// -> div int

% -> Mod (resto)

str * int -> reptir a str


"""


print(10//3)
print(10 // 3.0)

nome: str = "valor"
print(nome)

nome = 12

print(nome)


print(" nome " * 5)

print (" nome " + " str 2 ") 

nome = "Gonçalo"
ano = 2025
print ("Olá " + nome + " no ano de " + str(ano))
print ("Olá", nome, "no ano de", ano)

print(f"Ola {nome} no ano de {ano}")

nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Adulto")
elif idade >= 12:
    print("Teenager")
else:
    print("Menor")

## faça uma app que recebe um num e diga o mes correspondente
# 1- jan
# 2- Fev
# ......
# 12- Dez
# outro valor - Mês inválido

mes = str(input("Indique um mês (ex: 1 -  Janeiro): "))

#com if

"""
if mes == "1":
    print("Janeiro")
elif mes == "2":
    print("Fevereiro")
elif mes == "3":
    print("Março")
elif mes == "4":
    print("Abril")
elif mes == "5":
    print("Maio")
elif mes == "6":
    print("Junho")
elif mes == "7":
    print("Julho")
elif mes == "8":
    print("Agosto")
elif mes == "9":
    print("Setembro")
elif mes == "10":
    print("Outubro")
elif mes == "11":
    print("Novembro")
elif mes == "12":
    print("Dezembro")
else:
    print("Resposta incorreta!!")

"""

#com match case

match mes:
    case "1":
        print("Janeiro")
    case "2":
        print("Fevereiro")
    case "3":
        print("Março")
    case "4":
        print("Abril")
    case "5":
        print("Maio")
    case "6":
        print("Junho")
    case "7":
        print("Julho")
    case "8":
        print("Agosto")
    case "9":
        print("Setembro")
    case "10":
        print("Outubro")
    case "11":
        print("Novembro")
    case "12":
        print ("Dezembro")
    case _:
        print("Mês inválido")

## faça uma app que recebe um num e diga o dia da semana correspondente
# 1- dom
# 2- seg
#.......
#6- sábado
# outro valor - dia inválido

dia = str(input ("Indique um dia da semana: "))

match dia:
    case "1" | "Domingo":
        print("Domingo")
    case "2" | "Segunda-Feira":
        print("Segunda-Feira")
    case "3" | "Terça-Feira":
        print("Terça-Feira")
    case "4" | "Quarta-Feira":
        print("Quarta-Feira")
    case "5" | "Quinta-Feira":
        print("Quinta-Feira")
    case "6" | "Sexta-Feira":
        print("Sexta-Feira")
    case "7" | "Sábado":
        print("Sábado")
    case _:
        print("Dia inválido!!")

print("--"*3, "loops", "--"*3)

num = 10
while num >= 0:
    print(num)
    num -= 1

"""

faça um programa que peça ao ultilizador número até inserir um valor negativo

conte os valores inseridos
calcule a media do valores inseridos

"""

numero = 0
soma = 0
contador = 0

while numero >= 0:
    numero = float(input("Insira um número (negativo para sair): "))
    
    if numero >= 0:
        soma = soma + numero
        contador = contador + 1
    else:
        if contador > 0:
            media = soma / contador
            print("Quantidade de números:", contador)
            print("Média", media)
        else:
            print("Número inválido inserido.")
    
# range(5) -> 0, 1, 2, 3, 4             -> range(n) -> todos os num int de 0 a n-1
# range (5, 10) -> 5, 6, 7, 8, 9        -> range(m, n) -> tidis is num int de m a n-1
# range (4, 11, 2) -> 4, 6, 8, 10       -> range(m, n, s) -> todos os num int de m a n-1 com um step de s

range(4)    # 0 1 2 3
range(0, 4) # 0 1 2 3

range(4, 8) # 4, 5, 6, 7

range(12, 18, 2) # 12, 14, 16

print("--"*3, "for loops", "--"*3)

for i in range(4):
    print(i)

for i in range(4, 20, 2):
    print(i, end=" ")

print("")