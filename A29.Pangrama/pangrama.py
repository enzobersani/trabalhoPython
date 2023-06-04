def verificar_pangrama(frase):
    letras = set(frase.lower())
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")

    return letras == alfabeto

frase = input("Digite uma frase: ")

resultado = "é um pangrama" if verificar_pangrama(frase) else "não é um pangrama"
print(f"A frase {resultado}.")




