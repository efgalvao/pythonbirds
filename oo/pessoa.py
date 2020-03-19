class Pessoa:
    def __init__(self, *filhos, nome=None, idade=38):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {solfierii.nome}'


if __name__ == '__main__':
    solfierii = Pessoa(nome='Solfieri')
    ze = Pessoa(solfierii, nome='Zé')
    print(Pessoa.cumprimentar(solfierii))
    print(id(solfierii))
    print(ze.cumprimentar())
    print(ze.idade)
    print(ze.nome)
    ze.sobrenome = 'Ferreira'
    print(ze.nome, ze.sobrenome)
    del ze.filhos
    print(ze.__dict__)
    print(solfierii.__dict__)
    #for filhos in ze.filhos:
        #print(filhos.nome)
