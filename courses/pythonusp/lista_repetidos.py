def remove_repetidos(lista):
    lista = list(set(lista))
    lista.sort()
    return lista
print(remove_repetidos([2, 4, 2, 2, 3, 3, 1]))
print(remove_repetidos([1, 2, 3, 3, 3, 4]))
