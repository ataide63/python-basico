
# Im porta os Módulos que eu criei
import Modulo_Introducao  # criado por mim
import sys  # Módulo do python


# definição da classe


class Retangulo:
    lado_a = None
    lado_b = None

    # Definindo um objeto "função" dentro da classe Retangulo
    def __init__(self, lado_a, lado_b):  # objeto protegido inicia com __
        self.lado_a = lado_a
        self.lado_b = lado_b
        print ('Criando nova instancia do Rentangulo')

    def calcula_area(self):
        return self.lado_a * self.lado_b

    def calcula_petimetro(self):
        return 2 * self.lado_a * self.lado_b

#  Criando uma instancia da classe Retangulo:
r = Retangulo(12,15)  #  Cria uma instancia
print (r.calcula_area())
print (r.calcula_petimetro())
