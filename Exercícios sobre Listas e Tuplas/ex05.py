#5.Escreva um programa que copie os valores pares para uma lista e os
#valores ímpares para outra lista. A lista inicialmente de valores é V=
#[9,8,7,12,0,13,21] .


V = [9, 8, 7, 12, 0, 13, 21]

pares = [valor for valor in V if valor % 2 == 0]
impares = [valor for valor in V if valor % 2 != 0]

print("Valores pares:", pares)
print("Valores ímpares:", impares)
