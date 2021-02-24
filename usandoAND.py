print('Responda com sim ou nao')
usa_mascara = input("Você está de mascara?").strip().lower()
passou_alcool = input("Você passou álcool em gel nas mãos?").strip().lower()

if (usa_mascara == 'sim') and (passou_alcool == 'nao'):
    print('Pode entrar na minha casa')
elif usa_mascara == 'nao':
    print('Por favor, coloque a máscara')
elif passou_alcool == 'nao':
    print('Por favor, passe alcool em gel')
else:
    print('Não pode entrar na minha casa')