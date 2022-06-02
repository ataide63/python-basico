
# Para conectar o BD, vamos precisar de uma biblioteca(Móduilo) MySQLdb  ou  pymysql

# import MySQLdb     ou      import pymysql

class Conexao_db:

    var_server = 'localhost'
    var_user = 'root'
    var_pwd = 'mypwd'
    var_db = 'escola_curso'
    var_port = 3306
    import MySQLdb

    ## Faço a conexão no bancoô&
    global conn  # global em toda classe
    conn = MySQLdb.connect(var_server, var_user,var_pwd, var_db,var_port)
    global c   ## Defino como global em toda classe antes de usar
    c = conn.cursor     ## defino que o retorno será um cursor(set nornmal)

    ###  Ou Defino que o retorno será um cursor tipo dicionário
    c = conn.cursor(MySQLdb.cursors.DictCursor)

    def Aplicacao_Insert(values, tables, fields = None):
        #global c, conn  # indica que é uma variável é global lá na classe
        myquery = "INSERT INTO " + tables
        if (fields):
            myquery = myquery + " (" + fields + ") "
        myquery = myquery + " VALUES " + ",".join(["(" + v + ")" for v in values])
        c.execute(myquery)
        conn.commit()

    def Aplicacao_Consulta(fields, tables, where=None):

       #global c  # indica que é uma variável é global lá na classe

       myquery = None
       myquery = " SELECT " + fields + " from " + tables
       if (where):
           myquery = myquery + "  where " + where
       c.execute(myquery)
       return c.fetchall()
    # print(Myclass.Aplicacao_Consulta("*","alunos", "ID_ALUNO = 8")) # trazer tudo(*) de tab alunos where id=8


    def Aplicacao_Update(sets, tables, where = None):
        #global c, conn  # indica que é uma variável é global lá na classe
        myquery = "UPDATE " + tables
        myquery = myquery + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
        if (where):
            myquery = myquery + " WHERE " + where
        c.execute(myquery)
        conn.commit()
        #return (print(Myclass.Aplicacao_Consulta("*","alunos", "ID_ALUNO = 8"))) # trazer tudo(*) de tab alunos where id=8



    def Aplicacao_Delete( tables, where):   # No delete o se tiver o "where" vai apagar a tabela toda
        #global c, conn  # indica que é uma variável é global lá na classe
        myquery = "DELETE FROM " + tables +  " WHERE " + where
        c.execute(myquery)
        conn.commit()


        