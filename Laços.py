
#  Comando for

for i in range(0,5):
    print (i)
    if i==3: # Se o elemento igual a 3, encerra o laço  e segue para próximas instruções
        break

print (' laço foi interrompido')


# Comando while

i=0
while i < 8:
    i +=1
    if i == 5:
        print('Pular o 5')
        continue

    print (i)
    if i == 7:
        print('Terminou')
        break

for i in range(10):
     print (i)

for i in range(10,20,2):
    print (i)
    # começa com 10 até 20, de dois em dois