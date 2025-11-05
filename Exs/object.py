class Morada:
    def __init__(self, rua, codigoPostal, porta, apt):
        self.rua = rua
        self.codigoPostal = codigoPostal
        self.porta = porta
        self.apt = apt
        print("Morada Criada")

class Pessoa:
    def __init__(self, nome, idade, altura, morada):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.morada = morada
        print("Pessoa Criada")

    def envelhecer(self, anos=1):
        for i in range(anos):
            if self.idade < 25:
                self.idade += 1
                self.altura += 1.5  
            else:
                self.idade += 1  

    def info(self):
        print("Infos:")
        print(f"  Nome: {self.nome}")
        print(f"  Idade: {self.idade} anos")
        print(f"  Altura: {self.altura} cm")
        print("Morada:")
        print(f"  Rua: {self.morada.rua}")
        print(f"  Código Postal: {self.morada.codigoPostal}")
        print(f"  Porta: {self.morada.porta}")
        print(f"  Apartamento: {self.morada.apt}")

m1 = Morada("Rua das Flores", "1234-567", 10, 2)
p1 = Pessoa("Adalberto Silva da Cunha dos Santos Pereira Miguel Dumond", 20, 170, m1)
p1.info()