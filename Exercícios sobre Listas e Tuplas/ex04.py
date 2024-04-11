#4.A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T= [
#-10, -8, 0, 1, 2, 5, -2,-4]. Faça um programa que imprima a menor e a maior
#temperatura, assim como a temperatura média.

T = [-10, -8, 0, 1, 2, 5, -2, -4]

# Calculando menor e maior temperatura
menor_temperatura = T[0]
maior_temperatura = T[0]
for temperatura in T:
    if temperatura < menor_temperatura:
        menor_temperatura = temperatura
    if temperatura > maior_temperatura:
        maior_temperatura = temperatura

media_temperaturas = sum(T) / len(T)

print("A menor temperatura foi:", menor_temperatura)
print("A maior temperatura foi:", maior_temperatura)
print("A média da temperatura é:", media_temperaturas)
