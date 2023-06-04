def verificar_jokenpo(jogada1, jogada2):
    if jogada1 == jogada2:
        return "Empate"
    elif jogada1 + jogada2 in ["TesouraPapel", "TesouraLagarto", "PapelPedra", "PapelSpock", "PedraLagarto",
                               "PedraTesoura", "LagartoSpock", "LagartoPapel", "SpockTesoura", "SpockPedra"]:
        return "Jogador 1 venceu"
    else:
        return "Jogador 2 venceu"

jogada1 = input("Jogador 1, escolha entre Tesoura, Papel, Pedra, Lagarto ou Spock: ")
jogada2 = input("Jogador 2, escolha entre Tesoura, Papel, Pedra, Lagarto ou Spock: ")

resultado = verificar_jokenpo(jogada1, jogada2)
print(resultado)
