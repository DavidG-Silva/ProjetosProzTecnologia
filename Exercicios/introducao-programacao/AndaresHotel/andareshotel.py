andarFaltante = 13
totalAndares = 20

print('Laco FOR')
i = totalAndares
for i in range(totalAndares, 0, -1):
    if i == andarFaltante:
        continue
    print(f"{i}o andar")


print('\nLaco WHILE')
j = totalAndares
while j > 0:
    if j != andarFaltante:
        print(f"{j}o andar")
    j -= 1


# Do While (nao existe em Python)
"""
int contador = 20;
do {
    if i != 13:
        printf("%d", i);
    contador = contador + 1;
} while (contador > 1)
"""
