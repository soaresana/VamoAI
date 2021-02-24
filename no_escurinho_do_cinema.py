nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
estuda_python = input("Você é estudante de python? [s/n]")
valor_entrada = 0.0

if idade >= 18:
    entrada = input("Temos dois tipos de entrada padrão e VIP, digite [P ou V]")
    if entrada.upper() == "P":
        valor_entrada = 35.00

    elif entrada.upper() == "V":
        valor_entrada = 60.00

    elif estuda_python.upper() == "S":
        valor_entrada /= 2
        
    print(f"{nome}, Sua entrada será {valor_entrada}")

else:
    falta_maior_idade = 18 - idade
    print(f"Infelizmente você não pode entrar no clube. Falta {falta_maior_idade} ano(s) para você poder entrar.")


