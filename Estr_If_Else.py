
#if elif else



a=10
b=5
c=1
d='a'

if a == 1:
    f = 1000  # variável 'f' sí existirá se a == 1 (escopo de variável)
    print (' a é igual a 1')
elif c > b:
      print (f)  #  Vai dar erro porque 'f'não existe aqui
      print ('c é maior que b ')
else:
    print(' nenhuma das alternativas')

