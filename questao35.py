numero = int(input("Digite um número inteiro de três dígitos (de 100 a 999): "))

if numero >= 100 and numero <= 999:
    digito_centena = numero // 100
    digito_dezena = (numero // 10) % 10
    digito_unidade = numero % 10

    numero_invertido = digito_unidade * 100 + digito_dezena * 10 + digito_centena

    print("O número formado pelos dígitos invertidos é:", numero_invertido)
else:
    print("O número digitado não possui três dígitos.")
