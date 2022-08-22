class Pessoa():
    def __init__(self, nome, sexo, idade):
        self.__nome = nome
        self.__sexo = sexo
        self.__idade = idade

    def get_nome(self):
        return self.nome
    def get_sexo(self):
        return self.sexo
    def get_idade(self):
        return self.idade

    def set_nome(self, nome):
        self.nome = nome
    def set_sexo(self, sexo):
        self.sexo = sexo
    def set_idade(self):
        self.idade = idade
   
if __name__ == "__main__":
    pessoa1 = Pessoa('Joao', 'm', '25')
    pessoa2 = Pessoa('Marcos', 'm', '45')
    pessoa3 = Pessoa('Beatriz', 'f', '20')
    pessoa4 = Pessoa('Deric', 'm', '17')

    
