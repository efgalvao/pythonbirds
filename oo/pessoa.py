class Pessoa:
    def __init__(self, nome=None, idade=38):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {p.nome}'


if __name__ == '__main__':
    p = Pessoa('Solfierii')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.idade)
    print(p.nome)
