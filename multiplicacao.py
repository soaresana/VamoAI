def multiplicacao(valor1, valor2):
    if valor1 <=0 or valor1 >50 and valor2 <= 0 or valor2 >50:
        print('Valores inválidos, insira valores entre 1 e 50')
    else:
        resultado = valor1*valor2
        print(f"{valor1} * {valor2} = {resultado}")

print("Vamos multiplicar!!!")

valor1 = int(input("Insira um valor entre 1 e 50: "))
valor2 = int(input("Insira outro valor entre 1 e 50: "))
print("Calculando...")

multiplicacao(valor1, valor2)