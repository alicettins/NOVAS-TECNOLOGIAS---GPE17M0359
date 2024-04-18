#3. Escreva um programa que compare duas listas. Considere a primeira lista como a versão 
#inicial e a segunda como a versão após alterações. Utilizando operações com conjuntos, 
#seu programa deverá imprimir a lista de modificações entre essas duas versões, listando:
# ◦ os elementos que não mudaram
# ◦ os novos elementos
# ◦ os elementos que foram removidos

class Bebida:
    def __init__(self, nome, tipo, versao):
        self.nome = nome
        self.tipo = tipo
        self.versao = versao

def comparar_versoes(versao_inicial, versao_atual):

    set_versao_inicial = set(versao_inicial)
    set_versao_atual = set(versao_atual)

    nao_mudaram = set_versao_inicial.intersection(set_versao_atual)
    print("Elementos que não mudaram:")
    for bebida in nao_mudaram:
        print(f"{bebida.nome} ({bebida.tipo})")

    novos_elementos = set_versao_atual.difference(set_versao_inicial)
    print("\nNovos elementos adicionados:")
    for bebida in novos_elementos:
        print(f"{bebida.nome} ({bebida.tipo})")

    removidos = set_versao_inicial.difference(set_versao_atual)
    print("\nElementos removidos:")
    for bebida in removidos:
        print(f"{bebida.nome} ({bebida.tipo})")

versao_inicial = [
    Bebida("Coca-Cola", "Refrigerante", 1),
    Bebida("Suco de Laranja", "Suco", 2),
    Bebida("Café", "Bebida Quente", 3),
    Bebida("Água Mineral", "Água", 4),
    Bebida("Vinho Tinto", "Vinho", 5)
]

versao_atual = [
    Bebida("Coca-Cola", "Refrigerante", 1),
    Bebida("Suco de Laranja", "Suco", 2),
    Bebida("Chá Verde", "Chá", 6),
    Bebida("Água Mineral", "Água", 4),
    Bebida("Cerveja", "Bebida Alcoólica", 7)
]
comparar_versoes(versao_inicial, versao_atual)
