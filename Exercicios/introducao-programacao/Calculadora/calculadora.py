
def calculadora():

    num1 = float(input('Informe o primeiro numero: '))
    num2 = float(input('Informe o segundo numero: '))
    operador = int(input('Informe a operacao a realizar [01 - SOMA] [02 - SUBTRACAO] [03 - MULTIPLICACAO] [04 - DIVISAO]: '))
    resultado = 0

    if operador == 1:
        resultado = num1 + num2
    elif operador == 2:
        resultado = num1 - num2
    elif operador == 3:
        resultado = num1 * num2
    elif operador == 4:
        resultado = num1 / num2

    print('O resultado sera:', resultado) 


calculadora()
