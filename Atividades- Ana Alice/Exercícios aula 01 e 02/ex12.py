#12. Modifique o programa anterior de forma a ler um número n. Imprima os n
#primeiros números primos
import math

def verificar_primo(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, math.isqrt(num) + 1, 2):
            if num % i == 0:
                return False
        return True

def imprimir_n_primos(n):
    contador = 0
    num = 2
    while contador < n:
        if verificar_primo(num):
            print(num, end=" ")
            contador += 1
        num += 1

def main():
    n = int(input("Digite o valor de n: "))
    print(f"Os {n} primeiros números primos são:")
    imprimir_n_primos(n)

if __name__ == "__main__":
    main()
