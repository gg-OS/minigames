import random


def jogada(r):
    linha = r[0].title()
    if len(r) == 2:
        coluna = int(r[1])
    else:
        coluna = int(r[1:])
    for i2 in range(len(linhas)):
        if linhas[i2] == linha:
            linha = i2 + 1
    return linha, coluna


def contador(coordenada):
    kaboom = 0
    linha_contador = coordenada[0]
    coluna_contador = coordenada[1]
    if linha_contador == 1:
        if coluna_contador == 1:
            if (linha_contador + 1, coluna_contador + 1) in bomba:
                kaboom += 1
            if (linha_contador, coluna_contador + 1) in bomba:
                kaboom += 1
            if (linha_contador + 1, coluna_contador) in bomba:
                kaboom += 1
        if coluna_contador == 15:
            if (linha_contador + 1, coluna_contador) in bomba:
                kaboom += 1
            if (linha_contador + 1, coluna_contador - 1) in bomba:
                kaboom += 1
            if (linha_contador, coluna_contador - 1) in bomba:
                kaboom += 1
        else:
            if (linha_contador, coluna_contador + 1) in bomba:
                kaboom += 1
            if (linha_contador, coluna_contador - 1) in bomba:
                kaboom += 1
            if (linha_contador + 1, coluna_contador + 1) in bomba:
                kaboom += 1
            if (linha_contador + 1, coluna_contador) in bomba:
                kaboom += 1
            if (linha_contador + 1, coluna_contador - 1) in bomba:
                kaboom += 1
    elif linha_contador == 15:
        if coluna_contador == 1:
            if (linha_contador - 1, coluna_contador) in bomba:
                kaboom += 1
            if (linha_contador - 1, coluna_contador + 1) in bomba:
                kaboom += 1
            if (linha_contador, coluna_contador + 1) in bomba:
                kaboom += 1
        if coluna_contador == 15:
            if (linha_contador - 1, coluna_contador) in bomba:
                kaboom += 1
            if (linha_contador - 1, coluna_contador - 1) in bomba:
                kaboom += 1
            if (linha_contador, coluna_contador - 1) in bomba:
                kaboom += 1
        else:
            if (linha_contador, coluna_contador + 1) in bomba:
                kaboom += 1
            if (linha_contador, coluna_contador - 1) in bomba:
                kaboom += 1
            if (linha_contador + 1, coluna_contador + 1) in bomba:
                kaboom += 1
            if (linha_contador + 1, coluna_contador) in bomba:
                kaboom += 1
            if (linha_contador + 1, coluna_contador - 1) in bomba:
                kaboom += 1
    else:
        if (linha_contador - 1, coluna_contador - 1) in bomba:
            kaboom += 1
        if (linha_contador - 1, coluna_contador) in bomba:
            kaboom += 1
        if (linha_contador - 1, coluna_contador + 1) in bomba:
            kaboom += 1
        if (linha_contador, coluna_contador - 1) in bomba:
            kaboom += 1
        if (linha_contador, coluna_contador + 1) in bomba:
            kaboom += 1
        if (linha_contador + 1, coluna_contador - 1) in bomba:
            kaboom += 1
        if (linha_contador + 1, coluna_contador) in bomba:
            kaboom += 1
        if (linha_contador + 1, coluna_contador + 1) in bomba:
            kaboom += 1
    return kaboom


print('E COMEÇA UMA PARTIDA DE CAMPO MINADO ggOS!\n')
matriz = []
linhas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
c = 0
# Inserção da dificuldade
dificuldade = input('Insira a dificuldade do jogo de 1 a 5 (diferente disso será aleatório): ')
dificuldade = int(dificuldade)
bombas = 0
if dificuldade == 1:
    bombas = 23
elif dificuldade == 2:
    bombas = 46
elif dificuldade == 3:
    bombas = 69
elif dificuldade == 4:
    bombas = 92
elif dificuldade == 5:
    bombas = 115
else:
    bombas = random.randint(23, 115)
# Montagem do tabuleiro
for i in range(16):
    matriz.append([])
    for j in range(16):
        if i == 0 and j == 0:
            matriz[i].append(' ')
        elif j == 0:
            matriz[i].append(linhas[c])
            c += 1
        elif i == 0:
            matriz[i].append(j)
        else:
            matriz[i].append(' ')
bomba = []
jogadas_efetuadas = []
b = 0
while b != bombas:
    l = random.randint(1, 15)
    c = random.randint(1, 15)
    if (l, c) in bomba:
        continue
    else:
        b += 1
        bomba.append((l, c))
print()
# Jogar
contador_de_jogadas = 0
print('Instruções:\n'
      '- Você deve fazer a sua jogada selecionando a coordenada do tabuleiro')
while True:
    for i in range(16):
        for j in range(16):
            print(f'[{matriz[i][j]:^2}]', end='')
        print()
    rodada = input('Faça sua jogada: ')
    if len(rodada) > 3 or len(rodada) < 2:
        print('Jogada inválida')
        continue
    x, y = jogada(rodada)
    if (x, y) in bomba:
        matriz[x][y] = '@'
        for i in range(16):
            for j in range(16):
                print(f'[{matriz[i][j]:^2}]', end='')
            print()
        print()
        print('KABOOOOOOM !\n')
        print('Você perdeu!')
        break
    else:
        if (x, y) in jogadas_efetuadas:
            print('Você já jogou nesse campo!\n')
        else:
            jogadas_efetuadas.append((x, y))
            matriz[x][y] = contador((x, y))
            contador_de_jogadas += 1
    if 225 - bombas == contador_de_jogadas:
        print('PARABÉNS! VOCÊ VENCEU!')
        break
print()
print('powered by ggOS')
