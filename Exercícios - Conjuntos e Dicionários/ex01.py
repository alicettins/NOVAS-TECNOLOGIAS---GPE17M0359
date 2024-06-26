#1. Escreva um programa que gere um dicionário, em que cada chave seja um
#caractere, e seu valor seja o número desse caractere encontrado em uma
#frase lida.
#Exemplo:O rato -> {"O":1,"r":1,"a":1,"t":1,"o":1}

def cont_caracteres(frase):
    contagem = {}
    for char in frase:
        if char in contagem:
            contagem[char] += 1
        else:
            contagem[char] = 1

    return contagem

frase = input("Digite uma frase: ")
resultado = cont_caracteres(frase)
print(resultado)
