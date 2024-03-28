altura_degrau = float(input("Digite a altura do degrau da escada (em metros): "))
altura_desejada = float(input("Digite a altura que deseja alcançar subindo a escada (em metros): "))
degraus_necessarios = altura_desejada / altura_degrau
print("O número de degraus que o usuário deverá subir é:", int(degraus_necessarios))
