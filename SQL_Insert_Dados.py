

import SQL_Conexao_db as conn_db

# """  Testando o insert da aplicação
values = [
    "DEFAULT, 'Celso Nomura', '2012/06/22', 'Av.das Raias 323','Itaí',  'SP','425i2197910'",
    "DEFAULT, 'Maria Helisa', '1999/03/01', 'Av.das Pedras 123','Betim','MG','44004723391'",
    "DEFAULT, 'João Pedro',  '2000/01/01', 'Av. das Pedras 123','Betim', 'MG','425i7297911'",
    "DEFAULT, 'Maria Pedro', '1998/03/11', 'Av. das Pedras 123','Betim', 'MG','354i7257698'"]
  
###                          ****    Cria a instância da classe     *****   ####

Myclass = conn_db.Conexao_db
Myclass.Aplicacao_Insert(values, "alunos")
print ("dados inseridos com sucesso!!")

## Verifica os dados inseridos
print(Myclass.Aplicacao_Consulta("*","alunos"))

