
# Função pode ou não receber parâmetros
# Função sempre retorna algo
# Função recursiva é uma função que chama ela mesma

#  from scripts import Herança  # importa  e usa a Herança.py
#  from scripts import Operadores  # importa  e usa a Operadores.py

def Retonar_Nome_Sobrenome(valor):
    if valor == 10:
       return ('# ', 'o vaor foi 10')
    else:
        return ('ataide', 'antonio')


nome, sobrenome = Retonar_Nome_Sobrenome(0)
print ( nome, sobrenome)