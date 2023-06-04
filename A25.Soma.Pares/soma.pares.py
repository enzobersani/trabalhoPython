numeros = []
continuar = True

while continuar:
    numero = int(input("Digite um número (ou 0 para finalizar): "))
    if numero == 0:
        continuar = False
    else:
        numeros.append(numero)

media = sum(numeros) / len(numeros) if numeros else 0
print(f"A média dos números informados é: {media}")
