"""

Nome: Gabriel Mendes
Turma: PIPL0924
Trabalho: Ex9 - Classes

"""

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor
    

class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudarValorLado(self, novo_tamanho):
        self.tamanho_lado = novo_tamanho

    def retornarValorLado(self):
        return self.tamanho_lado

    def calcularArea(self):
        return self.tamanho_lado ** 2
    

class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarValorLados(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB

    def retornarValorLados(self):
        return self.ladoA, self.ladoB

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return 2 * (self.ladoA + self.ladoB)
    

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        for _ in range(anos):
            self.idade += 1
            if self.idade < 21:
                self.altura += 0.5

    def engordar(self, peso_ganho):
        self.peso += peso_ganho

    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido

    def crescer(self, altura_ganho):
        self.altura += altura_ganho


class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")


class TV:
    def __init__(self, canal=1, volume=10):
        self.canal = canal
        self.volume = volume

    def mudarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("Canal inválido")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1


class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, nova_fome):
        self.fome = nova_fome

    def alterarSaude(self, nova_saude):
        self.saude = nova_saude

    def alterarIdade(self, nova_idade):
        self.idade = nova_idade

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def calcularHumor(self):
        if self.fome < 5 and self.saude > 5:
            return "Feliz"
        elif self.fome >= 5 and self.saude <= 5:
            return "Triste"
        else:
            return "Neutro"
        
        
bola1 = Bola("Vermelha", 30, "Couro")
print("\nCor da bola:", bola1.mostraCor())

print("-----------------------")

quadrado1 = Quadrado(4)
print("Área do quadrado:", quadrado1.calcularArea())

print("-----------------------")

retangulo1 = Retangulo(4, 6)
print("Perímetro do retângulo:", retangulo1.calcularPerimetro())

print("-----------------------")

pessoa1 = Pessoa("João", 20, 70, 175)
pessoa1.envelhecer(3)
print("Idade da pessoa após envelhecer:", pessoa1.idade)

print("-----------------------")

conta1 = ContaCorrente(12345, "Maria", 500)
conta1.saque(100)
print("Saldo após saque:", conta1.saldo)

print("-----------------------")

tv1 = TV()
tv1.mudarCanal(10)
print("Canal atual da TV:", tv1.canal)

print("-----------------------")

bichinho1 = BichinhoVirtual("Fido", 3, 8, 2)
print("Humor do bichinho virtual:", bichinho1.calcularHumor(), "\n")

