nota_g1 = float(input("Digite a nota de G1: "))
nota_g2 = float(input("Digite a nota de G2: "))
media_semestre = nota_g1 + (nota_g2 * 2) / 3
print("A média do semestre é:", media_semestre)
if media_semestre >= 7.0:
    print("Parabéns! Você foi aprovado!")
else:
    print("Infelizmente, você foi reprovado.")
