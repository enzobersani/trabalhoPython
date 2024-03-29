def verificar_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True

numero = int(input("Digite um número: "))

resultado = "é um número primo" if verificar_primo(numero) else "não é um número primo"
print(f"{numero} {resultado}.")
