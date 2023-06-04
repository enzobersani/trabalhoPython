def verificar_jokenpo(jogada1, jogada2):
    if jogada1 == jogada2:
        return "Empate"
    elif jogada1 == "Pedra" and jogada2 == "Tesoura" or \
         jogada1 == "Tesoura" and jogada2 == "Papel" or \
         jogada1 == "Papel" and jogada2 == "Pedra":
        return "Jogador 1 venceu"
    else:
        return "Jogador 2 venceu"

jogada1 = input("Jogador 1, escolha Pedra, Papel ou Tesoura: ")
jogada2 = input("Jogador 2, escolha Pedra, Papel ou Tesoura: ")

resultado = verificar_jokenpo(jogada1, jogada2)
print(resultado)