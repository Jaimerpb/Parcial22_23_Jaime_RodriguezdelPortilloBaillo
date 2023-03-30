#Implementar sobre el TDA polinomio desarrollado previamente las siguientes actividades:
#  restar;  dividir;  eliminar un término;  determinar si un término existe en un polinomio.
class Node(object):
    info, sig = None, None

class datopolinomio(object):
    def __init__(self,valor,termino):
        self.valor=valor
        self.termino=termino 
        