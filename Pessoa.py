class Pessoa:

    def __init__ (self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return "Pessoa:" + self.nome + "data_nascimento" + self.data_nascimento