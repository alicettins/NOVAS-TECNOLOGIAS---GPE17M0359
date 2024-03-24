# 7.Escreva um programa que leia a quantidade em segundos e imprima o resultado 
#em dias, horas, minutos e segundos.

def converter_segundos(segundos):
    dias = segundos // 86400  # 86400 segundos em um dia
    segundos %= 86400

    horas = segundos // 3600  # 3600 segundos em uma hora
    segundos %= 3600

    minutos = segundos // 60  # 60 segundos em um minuto
    segundos %= 60

    return dias, horas, minutos, segundos

# Exemplo de uso
segundos = int(input("Digite a quantidade de segundos que deseja converter: "))
dias, horas, minutos, segundos_restantes = converter_segundos(segundos)

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos_restantes} segundo(s)')