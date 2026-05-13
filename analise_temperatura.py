temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]
contador = 0

for i in range(len(temperaturas)):
    print(f"Pos: {i} -- Valor: {temperaturas[i]}")
sala = 0
maior_registro = 0
sala_registro = 0
for num in temperaturas:
    media = (num[0] + num[1] + num[2] + num[3]) / 4
    contador = 0
    for temp in num:
        if temp >= 33:
            contador += 1
    sala += 1
    print(f"Sala {sala+1}")
    print(f"Média: {media}")
    print(f"Registro crítico: {contador}")
    if contador > maior_registro:
        maior_registro = contador
        sala_registro = sala
print(f"Sala com maior risco: {sala_registro}")
