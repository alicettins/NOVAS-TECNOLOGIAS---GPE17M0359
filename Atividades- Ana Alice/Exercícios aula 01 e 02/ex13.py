#13. O fatorial de um inteiro não negativo n é escrito como n! (pronuncia-se “n
#fatorial”) e é definido como segue:
#n! = n · (n – 1) · (n – 2) · ... · 1 (para valores de n maiores ou iguais a 1) e n! =
#1 (para n = 0)
#Por exemplo, 5! = 5 · 4 · 3 · 2 · 1, o que dá 120

def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Digite um número inteiro não negativo: "))
fatorial_resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {fatorial_resultado}.")
