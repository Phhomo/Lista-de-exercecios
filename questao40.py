investimento1 = float(input("Digite o valor investido pelo primeiro apostador: "))
investimento2 = float(input("Digite o valor investido pelo segundo apostador: "))
investimento3 = float(input("Digite o valor investido pelo terceiro apostador: "))

premio = float(input("Digite o valor do prêmio: "))

total_investido = investimento1 + investimento2 + investimento3

parte1 = investimento1 / total_investido * premio
parte2 = investimento2 / total_investido * premio
parte3 = investimento3 / total_investido * premio

print("O primeiro apostador ganharia:", parte1)
print("O segundo apostador ganharia:", parte2)
print("O terceiro apostador ganharia:", parte3)
