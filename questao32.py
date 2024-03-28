valor_total = float(input("Digite o valor total da venda: "))
total_com_desconto = valor_total * 0.9
valor_parcela = valor_total / 3
comissao_vista = total_com_desconto * 0.05
comissao_parcelada = valor_total * 0.05
print("a. Total a pagar com desconto de 10%:", total_com_desconto)
print("b. Valor de cada parcela no parcelamento de 3x sem juros:", valor_parcela)
print("c. Comissão do vendedor caso a venda seja à vista:", comissao_vista)
print("d. Comissão do vendedor caso a venda seja parcelada:", comissao_parcelada)
