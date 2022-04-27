

# Uma classe é derivada quando herda as propriedades de outra classe (a classe base)


# Cria a classe base
class Classe_base:
    def Dobro(self, valor):
        try:
            return valor * 2
        except (IndexError, e):
            print ('' %s, e)
        finally:
            print ('Dobro:PASSEI PELO FINALLY')


    def Metade(self, valor):

        try:
            return valor / 2
        except (IndexError, e):
            print ('' %s, e)
        finally:
            print ('Metade:PASSEI PELO FINALLY')


# Cria a classe que vai herdar a classe base(herds todas os seus objetos)
class ClasseDerivada(Classe_base):
    def Calcular(self, valor):
        return Classe_base.Dobro(self, valor) + 10

# cria a instancia da classe Derivada antes de usá-las
# A Classe derivada vai trazer junto os objetos herdados da classe base
c = ClasseDerivada()
print(c.Calcular(10))
print(c.Metade(50))