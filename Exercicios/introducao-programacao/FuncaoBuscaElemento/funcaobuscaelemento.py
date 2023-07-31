def buscaElemento(array, elemento=None):
    while True:
        if elemento == None:
            elemento = input("Informe o elemento que quer encontrar: ")

        for i in range(len(array)):
            if str(array[i]) == str(elemento):
                return (
                    f"O elemento {elemento} foi encontrado na {i+1}a posicao da lista."
                )
        
        elemento = input("Informe o elemento que quer encontrar: ")


numeros = [1, 2, 3, 0, 4, "teste", True]

print(buscaElemento(numeros))

print(buscaElemento(numeros,3))
