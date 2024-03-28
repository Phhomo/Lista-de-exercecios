salario_base = float(input("Digite o salário-base do funcionário: "))
gratificacao = salario_base * 0.05
salario_com_gratificacao = salario_base + gratificacao
imposto = salario_base * 0.07
salario_a_receber = salario_com_gratificacao - imposto
print("O salário a receber é:", salario_a_receber)
