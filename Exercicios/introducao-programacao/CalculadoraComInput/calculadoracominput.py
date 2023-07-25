def calculadora():
    num1 = 0
    num2 = 0
    operador = None
    
    while True:
        try:
            num1 = float(input("Informe o primeiro numero: "))
            break
        except:
            print("Informe um numero valido!")

    while True:
        try:
            num2 = float(input("Informe o segundo numero: "))
            break
        except:
            print("Informe um numero valido!")

    while True:
        try:
            operador = int(input("Informe a operacao a realizar [1 - SOMA] [2 - SUBTRACAO] [3 - MULTIPLICACAO] [4 - DIVISAO] [0 - SAIR]: "))
            if operador in range (1,5):
                break
            elif operador == 0:
                return 'sair'
            else:
                print("Essa opcao nao existe!!")
        except:
            print("Essa opcao nao existe!!")
    

    if operador == 1:
        return num1 + num2
    elif operador == 2:
        return num1 - num2
    elif operador == 3:
        return num1 * num2
    elif operador == 4:
        if num2 == 0:
            return "Nao e possivel dividir por zero!"
        else:
            return num1 / num2


while True:
    print('\nVamos calcular!')
    resultado = calculadora()
    if resultado == 'sair':
        print('Saindo... Até logo!')
        break
    print(f'O resultado e: {resultado}')
