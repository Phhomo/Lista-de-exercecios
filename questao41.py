comprimento = float(input("Digite o comprimento do terreno em metros: "))
largura = float(input("Digite a largura do terreno em metros: "))

preco_tela_por_metro = float(input("Digite o preço do metro de tela em reais: "))

perimetro = 2 * (comprimento + largura)
quantidade_tela = perimetro * preco_tela_por_metro

print("O custo para cercar o terreno com tela é de R$", quantidade_tela)
