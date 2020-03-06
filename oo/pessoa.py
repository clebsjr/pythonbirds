class Pesssoa():
    def __init__(self, *filhos, nome, idade=24):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == "__main__":
    f = Pesssoa(nome='Lucca')
    p = Pesssoa(f, nome='Junior')
    print(Pesssoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome, p.idade)
    for filho in p.filhos:
        print(filho.nome)