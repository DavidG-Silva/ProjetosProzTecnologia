anoNascimento = 0
anoValido = False

nomeCompleto = input('Informe o nome completo: ')
while not(anoValido):
    try:
        anoNascimento = int(input('Digite o ano de nascimento, entre 1922 e 2021: '))
        if anoNascimento > 1922 and anoNascimento < 2021:
            anoValido = True
        else:
            print('Erro de valor.')
    except:
        print('Erro de tipo.')


        

idade = 2022 - anoNascimento
print(f'O usuario {nomeCompleto} completa {idade} anos em 2022')
