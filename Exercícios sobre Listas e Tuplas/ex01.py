# Vamos tentar resolver alguns desafios. Dada a lista = [12, -2, 4, 8, 29, 45,
#78, 36, -17, 2, 12, 8, 3, 3,-52] faça um programa que:
#a. imprima o maior elemento;
#b. imprima o menor elemento;
#c. imprima os números pares;
#d. imprima o número de ocorrências do primeiro elemento da lista;
#e. imprima a média dos elementos;
#f. imprima a soma dos elementos de valor negativo


lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

# a. Imprima o maior elemento
print("Maior elemento: ", max(lista))

# b. Imprima o menor elemento
print("Menor elemento: ", min(lista))

# c. Imprima os números pares
print("Números pares: ", [num for num in lista if num % 2 == 0])

# d. Imprima o número de ocorrências do primeiro elemento da lista
print("Número de ocorrências do primeiro elemento: ", lista.count(lista[0]))

# e. Imprima a média dos elementos
print("Média dos elementos: ", sum(lista) / len(lista))

# f. Imprima a soma dos elementos de valor negativo
print("Soma dos elementos negativos: ", sum(num for num in lista if num < 0))