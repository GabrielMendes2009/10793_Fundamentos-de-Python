
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        print("Pessoa Criada")

    def envelhecer(self, anos=1):
        for i in range(anos):
            if self.idade < 25:
                self.idade += 1
                self.altura += 1.5  
            else:
                self.idade += 1  
