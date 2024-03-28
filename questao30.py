valor_hora = float(input("Digite o valor da hora de trabalho em reais: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
valor_bruto = valor_hora * horas_trabalhadas
valor_total = valor_bruto * 1.10  # 10% de acréscimo
print("O valor total a ser pago ao funcionário é R$", valor_total)
