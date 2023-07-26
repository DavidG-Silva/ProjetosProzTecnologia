def buscaElemento(elemento, array):
    for i in range(len(array)):
        if str(array[i]) == elemento:
            return i
    return None


numeros = [1, 2, 3, 0, 4, "teste", True]
indice = None
while indice == None:
    item = input("Informe o elemento que quer encontrar: ")
    indice = buscaElemento(item, numeros)
    if indice != None:
        print(f"O elemento {item} foi encontrado no índice {indice}")
