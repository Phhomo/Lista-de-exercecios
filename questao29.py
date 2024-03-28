dias_trabalhados = int(input("Digite o número de dias trabalhados pelo encanador: "))
valor_bruto = dias_trabalhados * 30.00
desconto_previdencia = 0.11 * valor_bruto
valor_apos_previdencia = valor_bruto - desconto_previdencia
desconto_imposto_renda = 0.08 * valor_apos_previdencia
quantia_liquida = valor_apos_previdencia - desconto_imposto_renda
print("A quantia líquida que deverá ser paga ao encanador é R$", quantia_liquida)
