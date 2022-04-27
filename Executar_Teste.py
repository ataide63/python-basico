

##  1º Executa o módulo Criar uma arquivo


## Importar o módulo de manipulação de Arquivos
import Manipulando_Arquivo
import SQL_Conexao_db
from  datetime import datetime as tempo
data_atual =  tempo.now() 


#Cria e Manipula o arquivo na pasta atual
#var1 = open('teste.txt', 'w')  # O paraâmetro 'w' arquivo na pasta para gravação.
#var1.close()  # Fecha o arquivo para adicionar novas linhas com 'a'

var1 = Manipulando_Arquivo.Manip_Files('teste.txt')
x = var1.Grava_Arq('Em  ' + str(data_atual)  + ' Gravando linha 1.\n')
print (x)

x = var1.Grava_Arq('Em  ' + str(data_atual)  + ' Gravando linha 2.\n')
print (x)

x = var1.Grava_Arq('Em  ' + str(data_atual)  + ' Gravando linha 3.\n')
print (x)

