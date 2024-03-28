numero = int(input("Digite um número inteiro de 4 dígitos (de 1000 a 9999): "))
if numero >= 1000 and numero <= 9999:
    digito_milhar = numero // 1000
    digito_centena = (numero // 100) % 10
    digito_dezena = (numero // 10) % 10
    digito_unidade = numero % 10

    print(digito_milhar)
    print(digito_centena)
    print(digito_dezena)
    print(digito_unidade)
else:
    print("O número digitado não possui quatro dígitos.")
