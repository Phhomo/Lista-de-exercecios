nome_aluno = input("Digite o nome do aluno: ")

nota_prova = float(input("Digite a nota da prova (de 0 a 10): "))
nota_qualitativa = float(input("Digite a nota qualitativa (de 0 a 10): "))

if nota_prova < 0 or nota_prova > 10 or nota_qualitativa < 0 or nota_qualitativa > 10:
    print("As notas devem estar entre 0 e 10.")
else:
    media = (nota_prova * 2 + nota_qualitativa) / 3

    print("A média do aluno", nome_aluno, "na disciplina de ED é:", media)
