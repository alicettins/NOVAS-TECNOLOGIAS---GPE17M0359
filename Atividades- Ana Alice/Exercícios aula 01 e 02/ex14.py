#14. Escreva um aplicativo que lê um inteiro não negativo, calcula e imprime seu
#fatorial.

def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Digite um número inteiro não negativo: "))
fatorial_resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {fatorial_resultado}.")
