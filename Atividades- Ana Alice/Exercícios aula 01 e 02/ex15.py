#15. O quadrado de um número natural n é dado pela soma dos n primeiros
#números ímpares consecutivos. Por exemplo, 1^2 =1, 2^2 = 1+3 etc. Dado
#um número n, calcule seu quadrado usando a soma de ímpares ao invés de produto.

def quadrado_com_soma_de_impares(n):
    if n == 1:
        return 1
    
    soma_impares = 1  
    proximo_impar = 3  

    for _ in range(2, n + 1): 
        soma_impares += proximo_impar
        proximo_impar += 2  # O próximo número ímpa
    return soma_impares

n = int(input("Digite um número natural para calcular o quadrado: "))
quadrado = quadrado_com_soma_de_impares(n)
print(f"O quadrado de {n} é {quadrado}.")
