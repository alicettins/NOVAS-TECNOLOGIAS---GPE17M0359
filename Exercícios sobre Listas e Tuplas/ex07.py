#7.Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde
#você quer jogar e alternar entre os jogadores. A cada jogada, verifique se a
#posição está livre. Verifique também quando um jogador venceu a partida.
#Um jogo da velha pode ser visto como uma lista de 3 elementos, na qual
#cada elemento é outra lista também com três elementos.

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def jogo_da_velha():
    tabuleiro = [[" "]*3 for _ in range(3)]
    jogador = "X"

    while True:
        imprimir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador}, escolha a linha (1-3): ")) - 1
        coluna = int(input(f"Jogador {jogador}, escolha a coluna (1-3): ")) - 1

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada. Escolha outra.")
            continue

        tabuleiro[linha][coluna] = jogador

        # Verificar se houve um vencedor
        for i in range(3):
            if all(mark == jogador for mark in tabuleiro[i]) or all(tabuleiro[j][i] == jogador for j in range(3)):
                imprimir_tabuleiro(tabuleiro)
                print(f"Parabéns, jogador {jogador} venceu!")
                return

        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns, jogador {jogador} venceu!")
            return

        jogador = "O" if jogador == "X" else "X"

jogo_da_velha()
