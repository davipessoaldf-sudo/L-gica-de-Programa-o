matriz = [
    [0,  0,  0,  0],
    [0,  0,  0,  0],
    [0,  0,  0,  0]
]

for l in range(0, 2 + 1, 1):
    for c in range(0, 3 + 1, 1):
        matriz[l][c] = int(input("Valor para matriz: "))

for l in range(0, 2 + 1, 1):
    print('[', end='')
    for c in range(0, 3 + 1, 1):
        print(f'{matriz[l][c]:^4}', end='')
    print(']')