def encontrar_primeira_letra_nao_repetida(texto):
    contador = {}

    for letra in texto:
        contador[letra] = contador.get(letra, 0) + 1

    for letra in texto:
        if contador[letra] == 1:
            return letra

    return None

texto = input("Digite um texto: ")

primeira_letra_nao_repetida = encontrar_primeira_letra_nao_repetida(texto)

print(f"A primeira letra não repetida é: {primeira_letra_nao_repetida}" if primeira_letra_nao_repetida else "Não existem letras que não se repetem no texto informado.")


