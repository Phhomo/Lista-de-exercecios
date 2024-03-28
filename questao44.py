nome_vendedor = input("Digite o nome do vendedor: ")

num_carros_vendidos = int(input("Digite o número de carros vendidos: "))
valor_total_vendas = float(input("Digite o valor total das vendas: "))

salario_base = 500.00

comissao_por_carro = 50.00

comissao_valor_vendas = 0.05 * valor_total_vendas

salario_total = salario_base + (num_carros_vendidos * comissao_por_carro) + comissao_valor_vendas

print("O salário de", nome_vendedor, "no mês é R$", salario_total)

