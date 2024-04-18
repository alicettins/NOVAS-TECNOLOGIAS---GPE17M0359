#6. Crie vários dicionários, em que o nome de cada dicionário seja o nome de
#um animal de estimação. Em cada dicionário, inclua o tipo do animal e o
#nome do dono. Armazene esses dicionários em uma lista chamada pets .
#Em seguida, percorra sua lista com um laço e, à medida que fizer isso,
#apresente tudo que você sabe sobre cada animal de estimação.

# Criando dicionários para representar animais de estimação
animal1 = {
    "nome": "Safira",
    "tipo": "Cadela",
    "dono": "Ana"
}

animal2 = {
    "nome": "Kenai",
    "tipo": "Gato",
    "dono": "Alice"
}

animal3 = {
    "nome": "Kodah",
    "tipo": "Furão",
    "dono": "Alves"
}

animal4 = {
    "nome": "Cookie",
    "tipo": "Cadela",
    "dono": "Martins"
}

pets = [animal1, animal2, animal3, animal4]

for pet in pets:
    print("Nome:", pet["nome"])
    print("Tipo:", pet["tipo"])
    print("Dono:", pet["dono"])
    print(
        
    )  