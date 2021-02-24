def calcula_media(media1, media2, media3, media4, media5):
    media_geral = (media1 + media2 + media3 + media4 + media5) / 5
    print(f"A média geral é {media_geral}")

print("Vamos calcular a média de 5 alunos!")
media_aluno1 = float(input("Digite a média do aluno 1:"))
media_aluno2 = float(input("Digite a média do aluno 2:"))
media_aluno3 = float(input("Digite a média do aluno 3:"))
media_aluno4 = float(input("Digite a média do aluno 4:"))
media_aluno5 = float(input("Digite a média do aluno 5:"))

calcula_media(media_aluno1, media_aluno2, media_aluno3, media_aluno4, media_aluno5)
