hora_inicio = int(input("Digite a hora de início (0-23): "))
minuto_inicio = int(input("Digite o minuto de início (0-59): "))
segundo_inicio = int(input("Digite o segundo de início (0-59): "))

duracao_segundos = int(input("Digite a duração da experiência em segundos: "))

segundos_inicio = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio

segundos_termino = segundos_inicio + duracao_segundos

hora_termino = segundos_termino // 3600
minuto_termino = (segundos_termino % 3600) // 60
segundo_termino = segundos_termino % 60

print("Novo horário de término da experiência:")
print("Hora:", hora_termino)
print("Minuto:", minuto_termino)
print("Segundo:", segundo_termino)
