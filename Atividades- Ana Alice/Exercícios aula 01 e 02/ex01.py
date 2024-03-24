#1. Escreva um aplicativo que solicita ao usuário inserir dois inteiros, 
#obtém do usuário esses números e imprime sua soma, produto, diferença e divisão 


def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    soma = num1 + num2
    mult = num1 * num2
    sub = num1 - num2
    divisao = num1 / num2
    

    print("Soma:", soma)
    print("Produto:", mult)
    print("Diferença:", sub)
    print("Divisão:", divisao)
2
if __name__ == "__main__":
    main()
