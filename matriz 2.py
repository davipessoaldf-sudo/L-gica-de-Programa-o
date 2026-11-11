LINHAS = 2
COLUNAS = 5
valores_maior_20 = 0

matriz = [
    [float(input(f"Valor [{i}][{j}]: ")) for j in range(COLUNAS)]
    for i in range(LINHAS)
]

soma_total = 0
for linha in matriz:
    for valor in linha:
        soma_total += valor
        if valor > 20:
            valores_maior_20 += 1

media = soma_total / (LINHAS * COLUNAS)

print("\n CALCULADORA DE MATRIZ")
for linha in matriz:
    print("  ".join(f"{valor:7.2f}" for valor in linha))

print(f"\nSoma total: {soma_total:.2f}")
print(f"Média aritmética: {media:.2f}")
print(f"Valores maiores que 20: {valores_maior_20}")