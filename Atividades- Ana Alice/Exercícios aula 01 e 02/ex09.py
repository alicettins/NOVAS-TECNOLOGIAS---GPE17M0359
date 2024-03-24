#9. Escreva um programa que exiba uma lista de opções (menu): adição,
#subtração, divisão, multiplicação e sair. Imprima a tabuada da operação
#escolhida. Repita até que a opção saída seja escolhida.

# n soube fazer a tabuada
def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Não é possível dividir por zero."

def exibir_menu():
    print("\nMenu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Saindo do programa...")
            break

        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))

        if opcao == "1":
            print("Soma:", adicao(num1, num2))
        elif opcao == "2":
            print("Diferença:", subtracao(num1, num2))
        elif opcao == "3":
            print("Produto:", multiplicacao(num1, num2))
        elif opcao == "4":
            print("Divisão:", divisao(num1, num2))
        else:
            print("Erro")

if __name__ == "__main__":
    main()
