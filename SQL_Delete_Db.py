
import SQL_Conexao_db as conn_db    
Myclass = conn_db.Conexao_db

"""  Testand oo Delete  """
Myclass.Aplicacao_Delete("alunos", "ID_ALUNO = 9") # apagar de tab alunos where id=9
print(Myclass.Aplicacao_Consulta("*","alunos", "ID_ALUNO=  9")) # apagar tudo(*) de tab alunos where id=9

print("Exclusão realizada com sucesso!!")