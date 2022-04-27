
class Manip_Files:
    Nome_Arq = None
    import os
    from os import path
    import sys

  # Comandos de leitura:
  # arq.read()  # Lê o arquivo inteiro$
  # arq.readline()  # Le uma linha do arquivo
  # arq.readlines()  # Le o arquivo e joga em uma lista

    # Definindo um objeto "função" dentro da classe Retangulo
    def __init__(self, Nome_Arq):  # objeto protegido inicia com __
        self.Nome_Arq = Nome_Arq
        # print ('Arquivo a ser criado: %s' % Nome_Arq)
        print ('1º Arquivo a ser criado: %s' % self.Nome_Arq)

    def Grava_Arq(self, linha):
       # Gravar o arquivo no disco.
       from os import path
       
       self.linha = linha
       print ('2º Arquivo a ser criado: %s' % self.Nome_Arq)
       # NO arquivo já aberto eu adiciona as linhas com o parâmetro 'a'
       if path.exists(self.Nome_Arq) == True:
          Arq_Saida = open(self.Nome_Arq, 'a')
       else:
           Arq_Saida = open(self.Nome_Arq, 'w')
           
       Arq_Saida.write(self.linha )
       Arq_Saida.close()
       # Agora vai mostrar as linhas do arquivo.linha
       MyArq = open(self.Nome_Arq  , 'rb')
       print (MyArq.read() )
       MyArq.close
       return ('Gravado')

       # Posso abrir o arquivo e jogar as linhas numa lista
       MyArq = open("teste.txt")
       linhas = MyArq.readlines()
       print(linhas)

## Obs.: os.path.isdir(var)   # retorna true se var é um diretório
## Obs.: os.path.isfile(var)  # retorna true se var é um arquvo
##  os.remove(var)  #apaga o arquivo do diretório corrente
##  os.removedirs   #apaga todos os subdiretórios a partir do atual 

# Opções de abertura de uma arquivo:
# arquivo = "Modo_Abertura.txt"
# var = open(arquivo, 'w')  #  w =  Escrita , se já existir o arquivo, cria um novo
# var = open(arquivo, 'r')  #  r =  Somente leitura
# var = open(arquivo, 'a')  #  a =  Leitura e escrita, adiciona novas linhas ao arquivo.
# var = open(arquivo, 'r+') #  r+ = leitura  e escrita, adiciona novas linhas ao arquivo.
# var = open(arquivo, 'w+') #  w+ = Escrita, apaga o conteúdo anterior. 
# var = open(arquivo, 'a+') #  a+ = Leitura e escrita. Adiciona dados ao arquivo.




