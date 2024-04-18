#2. Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
#a. os valores comuns às duas listas
#b. os valores que só existem na primeira
#c. os valores que existem apenas na segunda
#d. uma lista com os elementos não repetidos das duas listas.
#e. a primeira lista sem os elementos repetidos na segunda

def comparar_listas(lista1, lista2):
    set_lista1 = set(lista1)
    set_lista2 = set(lista2)

    comuns = set_lista1.intersection(set_lista2)
    print("Valores comuns às duas listas:", comuns)

    apenas_na_lista1 = set_lista1.difference(set_lista2)
    print("Valores que só existem na primeira lista:", apenas_na_lista1)

    apenas_na_lista2 = set_lista2.difference(set_lista1)
    print("Valores que só existem na segunda lista:", apenas_na_lista2)

    elementos_unicos = set_lista1.union(set_lista2)
    print("Elementos não repetidos das duas listas:", list(elementos_unicos))

    lista1_sem_repetidos_na_lista2 = set_lista1.difference(comuns)
    print("A primeira lista sem os elementos repetidos na segunda:", list(lista1_sem_repetidos_na_lista2))

frutas = [{"nome": "maçã", "tipo": "fruta"}, {"nome": "banana", "tipo": "fruta"}, {"nome": "laranja", "tipo": "fruta"}, {"nome": "uva", "tipo": "fruta"}, {"nome": "pera", "tipo": "fruta"}]
verduras = [{"nome": "alface", "tipo": "verdura"}, {"nome": "cenoura", "tipo": "verdura"}, {"nome": "beterraba", "tipo": "verdura"}, {"nome": "banana", "tipo": "fruta"}, {"nome": "tomate", "tipo": "fruta"}]

nomes_frutas = [fruta["nome"] for fruta in frutas]
nomes_verduras = [verdura["nome"] for verdura in verduras]
comparar_listas(nomes_frutas, nomes_verduras)
