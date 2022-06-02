

""" Testando a chamada da Aplicacao_Consulta """

import SQL_Conexao_db as conn_db
            

Myclass = conn_db.Conexao_db
print(Myclass.Aplicacao_Consulta("nome, cpf","alunos","id_aluno = 1"))
print(Myclass.Aplicacao_Consulta("nome, cpf","alunos"))   # Sem where

result = Myclass.Aplicacao_Consulta("nome, cpf","alunos")

print("Consulta concluída")