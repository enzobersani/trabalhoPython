def validar_sudoku(tabuleiro):
    for i in range(9):
        linha = tabuleiro[i]
        coluna = [tabuleiro[j][i] for j in range(9)]
        regiao = []

        regiao_inicio_linha = 3 * (i // 3)
        regiao_inicio_coluna = 3 * (i % 3)

        regiao = [tabuleiro[regiao_inicio_linha + x][regiao_inicio_coluna + y] for x in range(3) for y in range(3)]

        if tem_repeticao(linha) or tem_repeticao(coluna) or tem_repeticao(regiao):
            return False

    return True


def tem_repeticao(lista):
    numeros = [num for num in lista if num != 0]
    return len(numeros) != len(set(numeros))


def imprimir_celulas_incorretas(tabuleiro):
    for i in range(9):
        for j in range(9):
            valor = tabuleiro[i][j]

            if valor != 0:
                linha = tabuleiro[i]
                coluna = [tabuleiro[k][j] for k in range(9)]
                regiao = []

                regiao_inicio_linha = 3 * (i // 3)
                regiao_inicio_coluna = 3 * (j // 3)

                regiao = [tabuleiro[regiao_inicio_linha + x][regiao_inicio_coluna + y] for x in range(3) for y in range(3)]

                if tem_repeticao(linha) or tem_repeticao(coluna) or tem_repeticao(regiao):
                    print(f"Célula incorreta: ({i}, {j})")


tabuleiro = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if validar_sudoku(tabuleiro):
    print("O tabuleiro de Sudoku é válido.")
else:
    print("O tabuleiro de Sudoku contém erros.")

imprimir_celulas_incorretas(tabuleiro)






