temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

maior_critico = 0
maior_sala = 0

for i in range(len(temperaturas)):
    soma = 0
    critico = 0
    for temp in temperaturas[i]:
        soma += temp
        if temp >= 33:
            critico += 1

    media = soma / len(temperaturas[i])
    print(f"Sala {i + 1}")
    print(f"Média: {media:.2f}")
    print(f"Registros críticos: {critico}")
    print()

    if critico > maior_critico:
        maior_critico = critico
        sala_maior = i + 1
print(f"Sala com maior risco: Sala {maior_sala}")