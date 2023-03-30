listado_numeros = [18, 50, 210, 80, 145, 333, 70, 30]


def imprimir(lista):
    multiplosde10 = []
    for n in lista:
        if n % 10 == 0 and n < 200:
            multiplosde10.append(n)
    return multiplosde10



def imprimirrr(lista):
    multiplos10 = []
    for n in lista:
        if n > 300:
            break
        if n % 10 == 0 and n < 200:
            multiplos10.append(n)
    return multiplos10


