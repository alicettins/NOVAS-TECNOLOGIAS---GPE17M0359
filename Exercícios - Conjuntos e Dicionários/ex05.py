#5. Comece com o programa que você escreveu no Exercício 4. Crie dois
#novos dicionários que representem pessoas diferentes e armazene os três
#dicionários em uma lista chamada people . Percorra sua lista de pessoas
#com um laço. À medida que percorrer a lista, apresente tudo que você sabe sobre cada pessoa.

pessoa1 = {
    "first_name": "Ana Alice",
    "last_name": "Martins",
    "age": 20,
    "city": "Brasília"
}
pessoa2 = {
    "first_name": "Pedro",
    "last_name": "Santos",
    "age": 25,
    "city": "Rio de Janeiro"
}
pessoa3 = {
    "first_name": "Gabriel",
    "last_name": "Ferreira",
    "age": 23,
    "city": "Belo Horizonte"
}
people = [pessoa1, pessoa2, pessoa3]

for pessoa in people:
    print("Nome completo:", pessoa["first_name"], pessoa["last_name"])
    print("Idade:", pessoa["age"])
    print("Cidade:", pessoa["city"])
    print()  
