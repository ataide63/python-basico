
##########  SUBSTRING ==>> Python não tem a função substring, em vez disso, usa-se slice ou o indice da variavel

myString = "Mississippi"
print(  myString[slice(3)]    )   #  Resultado: Mis
print(  myString[slice(2,7)]   )   # Resultado: ssiss
print(  myString[slice(-6, -1 )]  )   #  Resultado: ssipp



a = "Diego"
b = "Mariano" 
concatenar = a + " " + b
print (concatenar)

print (concatenar[0:4])

print (concatenar.lower())
print (concatenar.upper())

var1 = " texto com caracter especial\n"
print(var1)  # mostra o texto sem alteração
print(var1.strip())   # mostra o texto removendo carcteres especiais e espaços.

# Convertendo uma string em lista:
var1 = "O rato roeu a roupa do rei de Roma"
print ("tamanho da variavel: " + str(len(var1)))
var1 = var1.split()  # cada palavra se torna elemento da lista
print ("tamanho da variavel: %s" %  len(var1))


### Quebra os elementos a partir de um determinado caracter:
var2 = "O rato roeu a roupa do rei de Roma"
var2 = var2.split("r")  # cada palavra com "r' se torna elemento da lista  sem a letra 'r'
print(var2)

## Pesquisando dentro de uma string
var1 = "O rato roeu a roupa do rei de Roma"
pesquisa = var1.find("roupa")  # retorna a posição da palavra dentro da string
print(pesquisa)


### Validar só números(faltou o "."  e a ",")
var1 = str('101281012801201.88')
for var in var1:
	if var.upper() in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ!?/@#$%¨&*()_+=-[´{`]~}^;:><'):
		print (var + ' está na lista')


## Substituindo parte da  string
var1 = "O rato roeu a roupa do rei de Roma"
pesquisa = var1.replace("roupa", "sandalia")  # substitui "roupa" por "sandalia" 
print(pesquisa)


## pegando parte  uma string
var1 = "O rato roeu a roupa do rei de Roma"
pesquisa = var1[3:12] 
print(pesquisa)

s = "ordem e progresso"
print(s.capitalize())

# Como verificar se uma string só possui números.
'12345'.isdigit()
'12345abc'.isdigit()

# Como verificar se uma string é alfanumérica (só possui letras e números).
'12345abc'.isalnum()


## Variavel s
s = "Olá, mundo!"


# Tipo de uma string.
type(s)

# Tamanho de uma string.
len(s)

# Substitui uma substring por alguma outra coisa.
s1 = s.replace("mundo", "meu abacate")

print(s1)

# A string s começa com "Olá"?
print(s.startswith("Olá"))
resultado=True

# A string s termina com "mundo"?
print(s.endswith("mundo"))
resultado=False porque foi trocado por Abacate


## Entrada de dados pelo usuário com Input:
print('Digite seu nome: ')
nome = input()
Tipo de entrada de dados
Como comentamos anteriormente, a função input retorna a entrada sempre com o tipo string, o que pode ser conferido com o emprego da função type():

type(nome)
Caso seja necessário obter o valor digitado pelo usuário com um tipo especificado, diferente de string (o que é comum), podemos associar funções de conversão específicas, como os exemplos a seguir mostram:

Obter a entrada como inteiro

a = int(input('Digite um número: '))
5
Obter a entrada como float

a = float(input('Digite um número: '))
5.6
Obter a entrada como fração

from fractions import Fraction
a = Fraction(input('Entre com um número em forma de fração: '))
7/8
type(a)

Obter a entrada como número complexo

a = complex(input('Entre com um número complexo no formato a + bj: '))
6+12j #sem espaços entre os valores!
type(a)


n1 = int(input('Enter a number: '))
n2 = int(input('Enter another number: '))

print('The sum of two numbers is:', n1+n2)