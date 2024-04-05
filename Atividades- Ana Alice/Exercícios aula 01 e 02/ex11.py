#11. Coloque um número bem grande para ser executado no exemplo anterior,
#você perceberá que demora bastante, consegue pensar num solução na
#lógica para reduzir o tempo de procura?

import math

num = int(input("Digite o número: "))
count = 0
i = 1

while i <= math.isqrt(num):
    if num % i == 0:
        count += 1
    i += 1

if count == 1:
    print(f"O número {num} é primo!")
else:
    print(f"O número {num} não é primo!")
