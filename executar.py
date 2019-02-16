from Projeto import Projeto
from Pessoa import Pessoa
from Atividade import Atividade
from projeto_atividade import Projeto_Atividade

p= Projeto("Projeto1","15-02-2019","31-12-2019")
pe=Pessoa ("Matheus", "23-02-2000")
a=Atividade ("Atividade1", 1, pe, "17-02-2019", "19-02-2019")
pa=Projeto_Atividade(p,a)

print(a.pessoa.nome)
print(a.status)
a.finalizar_atividade()
print(pa.atividade.status)
