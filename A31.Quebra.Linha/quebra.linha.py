def quebra_linha(frase, colunas):
    palavras = frase.split()
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        if len(linha_atual) + len(palavra) + 1 <= colunas:
            linha_atual += palavra + " "
        else:
            linhas.append(linha_atual.strip())
            linha_atual = palavra + " "

    linhas.append(linha_atual.strip())

    return linhas


frase = input("Digite a frase: ")
colunas = int(input("Digite a quantidade de colunas: "))

linhas_quebradas = quebra_linha(frase, colunas)

print("\n".join(linhas_quebradas))





