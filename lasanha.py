
def quebra_linha():
    print(" ")

def cozimento(quantidade_agua, tempo):
    print(f"A massa da lasanha foi cozida em {quantidade_agua} litro de água por {tempo} minutos")
    quebra_linha()

def tempero(tempero):
    print(f"Foi adicionado {tempero}")
    quebra_linha()

def camada(ingrediente):
    print(f"Foi adicionado uma camade de {ingrediente}")
    quebra_linha()

def aquece_forno(temperatura, tempo):
    print(f"O forno foi pré-aquecido à {temperatura}°C por {tempo} minutos")
    quebra_linha()

def assar(tempo):
    print(f'A lasanha assou por {tempo} minutos')
    quebra_linha()



print("Olá, vamos fazer uma lasanha :P")

print("Primeiro vamos cozinhar a massa")

quantidade_agua = int(input("Digite a quantidade de água para o cozimento da massa:"))

quebra_linha()

tempo = int(input("Digite por quanto tempo vamos cozinhar a massa:"))

quebra_linha()

print("Cozinhando...")

quebra_linha()

cozimento(quantidade_agua, tempo)

quebra_linha()

print("Agora vamos cozinhar a carne moída... Quais temperos vamos colocar?")

quebra_linha()

tempero1 = input("Digite o primeiro tempero:")

quebra_linha()

tempero(tempero1)

quebra_linha()

tempero2 = input("Digite o segundo tempero:")

quebra_linha()

tempero(tempero2)

quebra_linha()

tempero3 = input("Digite o terceito tempero:")

tempero(tempero3)

quebra_linha()

print("Huuummm.... Essa lasanha vai ficar gostosa :P")
print("Agora vamos montar a nossa lasanha, quais camadas vamos colocar?")

quebra_linha()

camada("Molho")
quebra_linha()
camada("Massa")
quebra_linha()
camada("Presunto e queijo")
quebra_linha()
camada("Molho")
quebra_linha()
camada("Massa")
quebra_linha()
camada("Presunto e queijo")
quebra_linha()
camada("Molho")
quebra_linha()
camada("Massa")
quebra_linha()
camada("Presunto e queijo")

quebra_linha()

print("Agora vamos pré-aquecer o forno")
quebra_linha()
temperatura_pre = int(input("Qual temperatura vamos pré-aquecer o forno?"))
tempo_pre = int(input("Por quanto tempo vamos pré-aquecer o forno?"))
quebra_linha()
aquece_forno(temperatura_pre,tempo_pre)

quebra_linha()
print("Agora vamos assar a nossa lasanha...")
tempo_assar = int(input("Digite por quanto tempo vamos assar a nossa lasanha:"))

quebra_linha()

assar(tempo_assar)

quebra_linha()

print("A nossa lasanha está pronta, tenho certeza que está uma delícia!")
print("Bom apetite!!")
