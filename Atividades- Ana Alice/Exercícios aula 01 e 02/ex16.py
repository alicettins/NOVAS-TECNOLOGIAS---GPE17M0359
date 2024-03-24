#16. A série de Fibonacci é 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, … Os dois primeiros
#termos são iguais a 1, e a partir do terceiro, o termo é dado pela soma dos
#dois termos anteriores. Dado um número n≥ 3, exiba o n-ésimo termo da série de Fibonacci.

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

n = int(input("Digite o valor de n (n >= 3): "))
if n < 3:
    print("O valor de n precisa ser maior ou igual a 3.")
else:
    enesimo = fibonacci_recursivo(n-1)  
    print(f"O {n}-ésimo termo da série de Fibonacci é: {enesimo}")
