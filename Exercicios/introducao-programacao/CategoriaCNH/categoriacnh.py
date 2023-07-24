
print('CATEGORIAS CNH\n')

# print('Passe algumas informacoes sobre o veiculo, e ajudarei a encontrar a melhor categoria de habilitacao.\n')
# qntdRodas = int(input('Informe a quantidade de rodas do veiculo: '))
# pesoBruto = int(input('Informe o peso bruto do veiculo, em quilogramas: '))
# qntdPessoas = int(input('Informe a quantidade de pessoas que o veiculo acomoda: '))

qntdRodas = 4
pesoBruto = 5500
qntdPessoas = 8
catCNH = ''

if qntdRodas <= 3:                  #até 3 rodas, cat A
    catCNH = 'A'
elif pesoBruto <= 6000:             #mais que 3 rodas, até 6000kg, cat B C D
    if qntdPessoas <= 8:            #mais que 3 rodas, até 6000kg, ate 8 pessoas,  cat B C
        if pesoBruto <= 3500:       #mais que 3 rodas, até 3500kg, ate 8 pessoas,  cat B
            catCNH = 'B'
        else:                       #mais que 3 rodas, mais que 3500 ate 6000kg, ate 8 pessoas,  cat C
            catCNH = 'C'            
    else:                           #mais que 3 rodas, até 6000 kg, mais que 8 pessoas, cat D
        catCNH = 'D'                
else:                               #mais que 6000kg, cat E
    catCNH = 'E'                    

#print(f'A melhor categoria de habilitacao para o veiculo informado é: {catCNH}')
print('A melhor categoria de habilitacao para o veiculo informado é:', catCNH)
