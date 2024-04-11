#Faça um programa que leia uma expressão com parênteses. Usando
#pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
#Exemplo:
#(()) OK
#()()(()()) OK
#( ) ) Erro
#Você pode adicionar elementos à pilha sempre que encontrar abre
#parênteses e desempilhá-la a cada fecha parênteses. Ao desempilhar,
#Listas, Dicionários, Tuplas e Conjuntos 16 verifique se o topo da pilha é um abre parênteses.
#Se a expressão estiver correta, sua pilha estará vazia no final.

def verifica_parentheses(expressao):
    pilha = []
    for char in expressao:
        if char == "(":
            pilha.append(char)
        elif char == ")":
            if not pilha:
                return False
            pilha.pop()
    return not pilha

# Exemplo de expressões
expressoes = [
    "(())",
    "()()(()())",
    "( ) )",
    "(()",
    "())",
    "()("
]

for expressao in expressoes:
    if verifica_parentheses(expressao):
        print(f"A expressão '{expressao}' está balanceada.")
    else:
        print(f"A expressão '{expressao}' não está balanceada.")
