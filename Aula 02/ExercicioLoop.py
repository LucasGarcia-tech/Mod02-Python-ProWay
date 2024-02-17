inicial = float(input("Digite o valor inicial: "))
final= float(input("Digite o valor final: "))


pares = 0
impar = 0
qtd_impar = 0

numero = inicial

while numero <= final:
    if numero % 2 == 0:
        pares += 1
    else:
        impar += numero
        qtd_impar += 1
    numero += 1

media_impares = impar / qtd_impar

print(f"Valores pares: {pares}")
print(f"Média de números impares: {media_impares}")
