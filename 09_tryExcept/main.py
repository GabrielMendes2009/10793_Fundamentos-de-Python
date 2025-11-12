# try
# except
try:
    x = int(input("digite um numero: "))
except:
    print("algo correu mal")

print("O codigo continua ")
print("---------------")

try:
    x2 = int(input("digite um numero: "))
except:
    print("algo correu mal")
else: # so correr qd o código não gera um erro
    print(f"foi digitado um numero  inteiro ({x2})")

print(f"O codigo continua {x2}")


# NameError: name 'x2' is not defined. Did you mean: 'x'?

# ValueError: invalid literal for int() with base 10: 'ee'

# IndexError: list index out of range



print("-------try - except - else - finally ---------")

try:
    x3 = int(input("digite um numero: "))

except:# quando ha um erro no try
    #lidar com o erro, faz o tratamento do erro
    print("algo correu mal")

else: # so correr qd o código não gera um erro
    print(f"foi digitado um numero  inteiro ({x3})")

finally: # corre sempre independentemente de haver erro ou não
    # usado para criar um log
    print(f"O codigo continua no finally")

print(f"O codigo continua")