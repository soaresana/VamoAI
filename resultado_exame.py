def resultado_exame (valor_exame):
    if valor_exame >= 0 and valor_exame <=  3:
        print('Procurar a equipe médica')
    elif valor_exame >= 4 and valor_exame <= 6: 
        print('Buscar se cuidar mais e fazer acompanhamento médico')
    elif valor_exame >= 7 and valor_exame <= 10:
        print('Continuar assim')
    else:
        print('Valor inválido')


print('***** Resultados dos Exames *****')

paciente1 = int(input('Digite o número do resultado do exame do Paciente 1:'))
paciente2 = int(input('Digite o número do resultado do exame do Paciente 2:'))
paciente3 = int(input('Digite o número do resultado do exame do Paciente 3:'))

print('Resultado Paciente 1:')
resultado_exame(paciente1)

print('Resultado Paciente 2:')
resultado_exame(paciente2)

print('Resultado Paciente 3:')
resultado_exame(paciente3)

