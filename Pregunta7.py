#Implementar sobre el TDA polinomio desarrollado previamente las siguientes actividades:
#  restar;  dividir;  eliminar un término;  determinar si un término existe en un polinomio.
#explicado:




class Nodo(object):
    """Clase nodo simmplemente enlazado"""

    info, sig = None, None


class datoPolinomio(object):
    """Clase dato polinomio"""

    def __init__(self, valor, termino):
        """Crea un dato polinomio con valor y término"""
        self.valor = valor # valor equivale al coeficiente
        self.termino = termino # termino equivale al exponente


class Polinomio(object):
    """Clase polinomio"""

    def __init__(self):
        """Crea un polinomio del grado cero"""
        self.termino_mayor = None   # Nodo con el término de mayor grado, y None para polinomio de grado cero para empezar
        self.grado = -1         # Grado del polinomio, -1 para polinomio de grado cero para empezar

    def agregar_termino(polinomio, termino, valor):
        """Agrega un termino y su valor al polinomio"""
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if (termino > polinomio.grado):
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino
        else:
            actual = polinomio.termino_mayor
            while (actual.sig is not None and termino < actual.sig.info.termino):
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux

    def modificar_termino(pol, termino, valor):
        """Modifica el valor de un termino del polinomio"""
        actual = pol.termino_mayor
        while (actual is not None and actual.info.termino != termino):
            actual = actual.sig
        if (actual is not None):
            actual.info.valor = valor
    
    def eliminar_termino(pol, termino):
        """Elimina un termino del polinomio"""
        if (pol.termino_mayor is not None):
            if (pol.termino_mayor.info.termino == termino):
                pol.termino_mayor = pol.termino_mayor.sig
            else:
                actual = pol.termino_mayor
                while (actual.sig is not None and actual.sig.info.termino != termino):
                    actual = actual.sig
                if (actual.sig is not None):
                    actual.sig = actual.sig.sig
    
    def mostrar_polinomio(polinomio):
        """Muestra el polinomio"""
        aux = polinomio.termino_mayor
        pol = ""
        if (aux is not None):
            while (aux is not None):
                signo = ""
                if aux.info.valor >= 0:
                    signo += "+"
                pol += signo + str(aux.info.valor) + "x^" + str(aux.info.termino)
                aux = aux.sig
        return pol

    def evaluar_polinomio(pol, x):
        """Evalua el polinomio en x"""
        actual = pol.termino_mayor
        resultado = 0
        while (actual is not None):
            resultado += actual.info.valor * (x ** actual.info.termino)
            actual = actual.sig
        return resultado
    

    
    def restar_polinomios(pol1, pol2):
        """Resta dos polinomios"""
        pol3 = Polinomio()
        actual = pol1.termino_mayor
        while (actual is not None):
            Polinomio.agregar_termino(pol3, actual.info.termino, actual.info.valor)
            actual = actual.sig
        actual = pol2.termino_mayor
        while (actual is not None):
            Polinomio.modificar_termino(pol3, actual.info.termino, actual.info.valor - Polinomio.evaluar_polinomio(pol3, actual.info.termino))
            actual = actual.sig
        return pol3
    

    
    def dividir_polinomios(pol1, pol2): 
        """Divide dos polinomios"""
        pol3 = Polinomio()
        pol4 = Polinomio()
        actual = pol1.termino_mayor
        while (actual is not None):
            Polinomio.agregar_termino(pol4, actual.info.termino, actual.info.valor)
            actual = actual.sig
        while (pol4.grado >= pol2.grado):
            termino = pol4.grado - pol2.grado
            valor = pol4.termino_mayor.info.valor / pol2.termino_mayor.info.valor
            Polinomio.agregar_termino(pol3, termino, valor)
            actual = pol2.termino_mayor
            while (actual is not None):
                Polinomio.modificar_termino(pol4, actual.info.termino + termino, actual.info.valor * valor - Polinomio.evaluar_polinomio(pol4, actual.info.termino + termino))
                actual = actual.sig
        return pol3, pol4
    
    def existe_termino(pol, termino):
        """Verifica si existe un termino en el polinomio"""
        actual = pol.termino_mayor
        while (actual is not None and actual.info.termino != termino):
            actual = actual.sig
        return actual is not None

