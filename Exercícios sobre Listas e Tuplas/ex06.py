#6.Escreva um programa que controla a utilização das salas de um cinema.
#Imagine que a lista lugares_vagos=[10,2,1,3,0] contenha o número de
#lugares vagos nas salas 1,2,3,4 e 5, respectivamente. Esse programa lerá o
#número da sala e a quantidade de lugares solicitados. Ele deve informar se
#é possível vender o número de lugares solicitados, ou seja, se ainda há
#lugares livres. Caso seja, possível vender os bilhetes, atualizará o número
#de lugares livres. A saída ocorre quando se digita 0 no número da sala.

lugares_vagos = [10, 2, 1, 3, 0]

while True:
    num_sala = int(input("Digite o número da sala (ou 0 para sair): "))
    if num_sala == 0:
        print("Saindo do programa...")
        break
    
    if num_sala < 1 or num_sala > len(lugares_vagos):
        print("Número de sala inválido.")
        continue
    
    qtd_lugares = int(input("Digite a quantidade de lugares desejados: "))
    
    if qtd_lugares > lugares_vagos[num_sala - 1]:
        print("Desculpe, não há lugares suficientes nesta sala.")
    else:
        lugares_vagos[num_sala - 1] -= qtd_lugares
        print(f"Bilhetes vendidos com sucesso! Lugares restantes na sala {num_sala}: {lugares_vagos[num_sala - 1]}")

print("Estado final das salas:")
for sala, lugares in enumerate(lugares_vagos, start=1):
    print(f"Sala {sala}: {lugares} lugares vagos")
