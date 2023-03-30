listado_numeros = [18, 50, 210, 80, 145, 333, 70, 30]

#Imprimir el número en caso de que sea múltiplo de 10 y menor que 200
def imprimir(lista):
    multiplosde10 = []
    for n in lista:
        if n % 10 == 0 and n < 200:
            multiplosde10.append(n)
    return multiplosde10


#Parar el programa si llega a un número mayor que 300
def imprimirrr(lista):
    multiplos10 = []
    for n in lista:
        if n > 300:
            break
        if n % 10 == 0 and n < 200:
            multiplos10.append(n)
    return multiplos10


#Organizar la lista mediante el método de ordenamiento merge sort 
def merge_sort(collection: list) -> list:
    
    def merge(left: list, right: list) -> list:
        def _merge():
            while left and right:
                yield (left if left[0] <= right[0] else right).pop(0)
            yield from left
            yield from right

        return list(_merge())

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))
