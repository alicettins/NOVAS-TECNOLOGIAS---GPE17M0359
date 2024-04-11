#Faça um jogo da Forca utilizando listas. Dada uma palavra, dê algumas
#chances para o usuário acertar.

import random

# Lista de frutas para o jogo
frutas = ["banana", "laranja", "uva", "abacaxi", "manga", "morango"]

# Função principal do jogo
def jogar_forca():
    palavra = random.choice(frutas)
    letras_certas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Força!")
    print("Adivinhe a palavra: ", "_ " * len(palavra))

    while tentativas > 0:
        palpite = input("Digite uma letra ou a palavra inteira: ").lower()

        if len(palpite) == 1:  # Palpite de uma letra
            if palpite in palavra:
                letras_certas.append(palpite)
            else:
                tentativas -= 1
            palavra_mascarada = "".join([letra if letra in letras_certas else "_ " for letra in palavra])
            print("Palavra: ", palavra_mascarada)
        else:  # Palpite de palavra inteira
            if palpite == palavra:
                print("Parabéns! Você acertou a palavra!")
            else:
                print("Ops! Palavra incorreta. Você perdeu.")
                print("A palavra correta era:", palavra)
            break

        if set(palavra) <= set(letras_certas):
            print("Parabéns! Você adivinhou a palavra corretamente!")
            break

        print("Tentativas restantes:", tentativas)

    if tentativas == 0:
        print("Você perdeu! A palavra era:", palavra)

# Chamada da função principal
jogar_forca()
