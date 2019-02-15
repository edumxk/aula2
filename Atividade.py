class Atividade:

    def __init__ (self, nome, prioridade, pessoa, projeto, data_inicio, data_fim):
        self.nome = nome
        self.prioridade = prioridade
        self.pessoa = pessoa
        self.projeto = projeto
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = "ativa"

    def finalizar_atividade(self):
        self.status = "finalizada"