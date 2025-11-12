class filme:
    def __init__(self, titulo, ano, genero, duracao, diretor):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.duracao = duracao
        self.diretor = diretor

class maquina_do_tempo:
    def __init__ (self, ano, cordenadas, mes, dia, hora, minuto, segundo, ):
        self.ano = ano
        self.cordenadas = cordenadas
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        self.is_on = False

filme1 = filme("Interestelar", 2014, "Ficção Científica", 169, "Christopher Nolan")

maquina1 = maquina_do_tempo(2050, "37.7749° N, 122.4194° W", 12, 25, 10, 30, 0)

print("\nFilme:")
print("Título:", filme1.titulo)
print("Ano:", filme1.ano)
print("Gênero:", filme1.genero) 
print("Duração:", filme1.duracao, "minutos")
print("Diretor:", filme1.diretor)

print("-----------------------")

print("Máquina do Tempo:")
print("Ano:", maquina1.ano)
print("Coordenadas:", maquina1.cordenadas)
print("Data:", f"{maquina1.dia}/{maquina1.mes}/{maquina1.ano}")
print("Hora:", f"{maquina1.hora}:{maquina1.minuto}:{maquina1.segundo}\n")

print("-----------------------")

print("Estado da Máquina do Tempo:")
print("Ligada" if maquina1.is_on else "Desligada")