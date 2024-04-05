# 6.Escreva um aplicativo que receba a, b e c, coeficientes de uma equação do segundo grau, 
#e calcule as raízes x’ e x” através da fórmula de Báskara.


def calcular_raizes(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None, None  # Raízes imaginárias
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        return x1, x2

def main():
    a = float(input("Entre com o valor de a: "))
    b = float(input("Entre com o valor de b: "))
    c = float(input("Entre com o valor de c: "))

    if a == 0:
        print("O valor de 'a' deve ser diferente de zero para uma equação do segundo grau.")
        return

    raiz1, raiz2 = calcular_raizes(a, b, c)

    if raiz1 is None:
        print("A equação não possui raízes reais.")
    else:
        print(f"As raízes da equação são: x' = {raiz1} e x'' = {raiz2}")

if __name__ == "__main__":
    main()
