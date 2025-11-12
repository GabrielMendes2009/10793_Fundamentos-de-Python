
lista = [1,2,3]
x2 = 12
try:
    print(x2) # NameError: name 'x2' is not defined. Did you mean: 'x'?
    int("12") # ValueError: invalid literal for int() with base 10: 'ee'
    print(lista[3]) # IndexError: list index out of range


except NameError:
    print("NameError")
except ValueError:
    print("ValueError")
except IndexError:
    print("IndexError")
except:
    print("Erro genérico")

print("--------")

lista = [1,2,3]
#x2 = 12
try:
    print(x3) # NameError: name 'x2' is not defined. Did you mean: 'x'?
    int("12w") # ValueError: invalid literal for int() with base 10: 'ee'
    print(lista[3]) # IndexError: list index out of range

except NameError as erro:
    print(f"NameError - {erro}")
except ValueError as erro:
    print(f"ValueError - {erro.args}")
except IndexError as erro:
    print(f"IndexError - {erro}")
except:
    print("Erro genérico")