
# 1º LISTAS BASICO

#   Executar no diretório do Python:  python.exe -u d:\Cursos\Python\Basico\Listas.py

lista1 = []  # cria uma lsita vazia.


# Ou cria uma lista já com elementos dentro
lista1 = [ 3,4,1,2,'PRIMEIRA LISTA'   ]
print (lista1)  # resultado é o conteúdo : da list  [ 3,4,1,2,'PRIMEIRA LISTA'   ]
print (lista1[2])  # resultado É O TERCEIRO ELEMENTO DA LISTA:   1
print (lista1[0])  # mostra o primeiro PRIMEIRO elemento  da lista
print (lista1[-1])  # mostra o último elemento da lista
print (lista1[-2])  # mostra o penúltimo elemento da lista e assim sucessivamente


lista2 = [ "olá", "mundo", "!"]
lista3 = [0,"olá", "biscoito", "bolacha", 9.99, True ]

for i in lista2:
	print (i)


for i in lista3:
	print (i)


#  Trabalhando com lista
print  ( 1 + lista1[0])   # resultado:   4

print ( 'Antes era: %s ' % lista1)

# Adicionando um elemento à lista
lista1.append('Novo Elemento')
print ( 'Depois ficou : %s' % lista1)

# pegar somente alguns elementos da lista
print (lista1[1:-1])  # lista do segundo elemento até o penúltimo
print (lista1[1:])  # lista do segundo elemento em diante até o final
print (lista1[:-2])   # todos até o antepenúltimo ítem


## Ordenar uma lista, tem dua formar (var = lista.sorted()   ou list.sort()


lista1 = [0, 154, 120, 1000,  3,4,1,2]
var1 = sorted(lista1)
print  ( var1)   # resultado: [0, 1, 2, 3, 4, 120, 154, 1000]
print (lista1)


#  2) O método var.sort muda o ordem da lista fisicamente, 
# usando método var.sort, ele ordena a lista fisicamente, sem precisar mover para uma varíável
lista1 = [0, 154, 120, 1000,  3,4,1,2]
lista1.sort()
print (lista1)


#  2.1) Colocando em ordem decrescente: var.sort(reverse=True)
lista1 = [0, 154, 120, 1000,  3,4,1,2]
lista1.sort(reverse=True) 
print (lista1)    ## Resultado:   [1000, 154, 120, 4, 3, 2, 1, 0]


#  2.2  Invertendo os elementos de uma lista(colocando a lista ao contrário)
lista1 = [0, 154, 120, 1000,  3,4,1,2]
lista1.reverse()
print (lista1)   ##  Resultado: [2, 1, 4, 3, 1000, 120, 154, 0]



##  *************      ATENÇÃO !!!!!
#  Vai dar Erro se tentar ordenar números e strings na mesma lista:
#   lista1 = [0, 154, 120, 1000,  3,4,1,2,'PRIMEIRA LISTA']
#   print (  sorted(lista1) )
        ## Resultado: TypeError: '<' not supported between instances of 'str' and 'int'





# listar qtde elementos da lista
print ('Qtde de elementos na lista  : %s' %  len(lista1))


# Remover um elemento da lista com método 'remove'
lista1.remove(lista1[1])  # remove a 2ºelemto da lista, pois a lista começa no zero '0'
lista1.remove(lista1[-1])  # remove o último elemento da lista
print ('Depois da remoção(remove) ficou : %s' % lista1)


# Remover um elemento da lista com método 'del'
del lista1[1]   # remove a 2ºelemto da lista, pois a lista começa no zero '0'
print ('Depois da remoção(del) ficou : %s' % lista1)

# Limpar uma lista
del lista1[:]
print ('Depois da remoção(del) ficou : %s' % lista1)

nome = input("Digite seu nome:")
print(" Olá " + nome)



# 2º LISTAS AVANÇADO:



#  list comprehension
# Determinar o quadrado de cada elemento de uma lista:
x = [ 1,2,3,4,5 ] 
print (x)


# elevando cada elemento ao quadrado:
y = [i**2 for i in x]
print (y)
# Resultado: [1, 4, 9, 16, 25]




#   enumerate

# Determinar o quadrado de cada elemento de uma lista:
lista = ['abacate','bola','cachorro' ] 
print (lista)


for i, nome in enumerate(lista):
	print(i,nome)

# # Resultado:
# 0 abacate
# 1 bola
# 2 cachorro




#  Função Filter

def pares(i):
	if i % 2 == 0:
		return i


lista = [ 1,2,3,4,5,6,7,8,9,10,11,12,20,30 ] 
# a função só vai retornar o que for número par.
lista_pares = filter(pares,lista)
print(list(lista_pares))
# Resultado:   [2, 4, 6, 8, 10, 12, 20, 30]






#  Função reduce
from functools import reduce

def soma(x,y):
	return x + y
		

lista = [ 1,3,5,10,20]

# Vamos retornar o somatório dos elementos da lista
soma = reduce(soma,lista)
print (soma)
# Resultado: 39






#  Função Zip usado para concatenar várias listas


lista1=[ 1,2,3,4,5] 
lista2=["abacate","bola","cachorro","dinheiro","elefante" ] 
lista3=["sp","rj","mg","pr","ce"]


for numero, nome, valor in zip(lista1,lista2,lista3):
	print (numero, nome,valor)

## Resultado:
# 1 abacate     sp
# 2 bola        rj
# 3 cachorro    mg
# 4 dinheiro    pr
# 5 elefante    ce

#  OBS.: Se as listas não tiverem o mesmo nr. de elementos, a função trunca pelo menor nr. de elementos entre as listas;




#  Função MAP() APLICA QUALQUER FUNÇÃO A CADA ELEMENTO DE UMA LISTA

def dobro(x):
	return x *2


valor = [ 1,2,3,4,5]

valor_dobrado = map(dobro,valor)

# precisa converter para uma lista
valor_dobrado = list(valor_dobrado)  # converte em lista
print (valor_dobrado)

#Resultado: [2, 4, 6, 8, 10]



#  Função lambda() APLICA QUALQUER FUNÇÃO A CADA ELEMENTO DE UMA LISTA

valor = [ 1,2,3,4,5]

valor_dobrado = map(lambda i:i*2,valor)   # Aplica a operação à todos os elementos da listsa
valor_dobrado = (list(valor_dobrado))  # converte o resultado para lista
 
print (valor_dobrado)

#Resultado: [2, 4, 6, 8, 10]

