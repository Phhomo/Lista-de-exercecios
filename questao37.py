total_segundos = int(input("Digite um valor inteiro em segundos: "))
horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60
print("Valor convertido:")
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)
