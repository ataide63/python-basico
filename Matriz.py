
# Matriz difere das listas

# Neste exemplo criamos uma matriz com 03 linha, cada linha com 03 elementos
matriz1 = [ [ 1 , 2, 3 ] , [ 'a','b','c' ]  ,  [ 11 , 12, 13 ]  ]
print (matriz1)   # lista  matriz inteira
print (matriz1[0])  # Lista a 1º linha da matriz
print (matriz1[-1])  # Lista a última linha da matriz

# Lista o 2º element da última linha
print (matriz1[-1] [1])  # Lista a última linha da matriz

# PArfa somar as matrizes, usa-se o sinal de +
matriz2 = [ 5, 2, 3]
matriz3 = [ 9, 1, 8 ]
print ( matriz2 + matriz3  )  # resultado é o acréscimos dos elementos na segunda matriz

print ( matriz2[0] + matriz3[2]  )  # resultado é a soma dos dois elementos

# COmando sorted   para ordenar a matriz ou uma lista
print (sorted(matriz2))

# Qtde de elementos na matriz
print ('Qtde de elementos na mastriz  : %s' %  len(matriz2))
print (sorted(matriz2))
