preco_hamburguer = 3.00
preco_cheeseburger = 2.50
preco_fritas = 2.50
preco_refrigerante = 1.00
preco_milkshake = 3.00

quantidade_hamburguer = int(input("Digite a quantidade de hambúrgueres consumidos: "))
quantidade_cheeseburger = int(input("Digite a quantidade de cheeseburgers consumidos: "))
quantidade_fritas = int(input("Digite a quantidade de porções de fritas consumidas: "))
quantidade_refrigerante = int(input("Digite a quantidade de refrigerantes consumidos: "))
quantidade_milkshake = int(input("Digite a quantidade de milkshakes consumidos: "))

total_conta = (preco_hamburguer * quantidade_hamburguer) + (preco_cheeseburger * quantidade_cheeseburger) + (preco_fritas * quantidade_fritas) + (preco_refrigerante * quantidade_refrigerante) + (preco_milkshake * quantidade_milkshake)

print("O total da conta é R$", total_conta)
