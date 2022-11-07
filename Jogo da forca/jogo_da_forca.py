import random
print('Bem vindo ao jogo da forca ggOS')
arquivo = open('palavras.txt', 'r')
palavras = arquivo.readlines()
palavra = palavras[random.randint(0, len(palavras))]
palavra = palavra[:len(palavra) - 1]
digitadas = []
chances = 5
arquivo.close()
while True:
    if chances == 0:
        print('Você perdeu!')
        break
    letra = input('Digite uma letra: ')
    print()
    if len(letra) > 1:
        print("Por favor insira apenas uma letra.\n")
        continue

    digitadas.append(letra)

    if letra in palavra:
        print(f'A letra "{letra}" está na palavra secreta.')
    else:
        print(f'A letra "{letra}" não está na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in palavra:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '_'

    if secreto_temporario == palavra:
        print(f'Parabéns, você ganhou!!! A palavra era {palavra}')
        break
    else:
        print(secreto_temporario)
    if letra not in palavra:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')