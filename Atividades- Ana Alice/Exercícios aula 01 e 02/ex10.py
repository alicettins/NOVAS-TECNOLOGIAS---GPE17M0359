#10. Escreva um programa que leia um número e verifique se é ou não um número primo.

num=int(input("Digite o num:"))
count=0
i = 1

while i<num:
    if num%i==0:
        count=count +1

    i = i + 1
if count==2:
    print(f"0 num {num} é primo!")
else:
    print(f"0 num {num} não é  primo!")
