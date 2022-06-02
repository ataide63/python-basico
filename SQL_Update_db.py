
import SQL_Conexao_db as conn_db
         
Myclass = conn_db.Conexao_db

"""  TEstando o Update  """
##   Myclass = Conexao_db
Myclass.Aplicacao_Update({"nome":"João Martins","cidade":"Curitiba"}, "alunos","id_aluno = 8")
print(Myclass.Aplicacao_Consulta("*","alunos", "ID_ALUNO = 8")) # trazer tudo(*) de tab alunos where id=8

print("Alteração Concluída")
# antes do update
# ({'id_aluno': 8, 'nome': 'João Pedro', 'data_nascimento': datetime.date(2000, 1, 1), 'endereco': 'Av. das Pedras 123', 'cidade': 'Betim', 'estado': 'MG', 'CPF': '425i7297911'},)
# Depois do update
# ({'id_aluno': 8, 'nome': 'João Martins', 'data_nascimento': datetime.date(2000, 1, 1), 'endereco': 'Av. das Pedras 123', 'cidade': 'Curitiba', 'estado': 'MG', 'CPF': '425i7297911'},)
       
