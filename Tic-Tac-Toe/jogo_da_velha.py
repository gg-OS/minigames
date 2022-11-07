def conversor(n):  # Erro de input F10 H12
    n = int(n)
    if n == 1:
        coordenada = [0, 0]
    elif n == 2:
        coordenada = [0, 1]
    elif n == 3:
        coordenada = [0, 2]
    elif n == 4:
        coordenada = [1, 0]
    elif n == 5:
        coordenada = [1, 1]
    elif n == 6:
        coordenada = [1, 2]
    elif n == 7:
        coordenada = [2, 0]
    elif n == 8:
        coordenada = [2, 1]
    else:
        coordenada = [2, 2]
    return coordenada


def verificador(matriz):  # Função verificadora de vitória
    # Horizontais
    if matriz[0][0] == matriz[0][1] == matriz[0][2] != ' ':
        v = 1
    elif matriz[1][0] == matriz[1][1] == matriz[1][2] != ' ':
        v = 1
    elif matriz[2][0] == matriz[2][1] == matriz[2][2] != ' ':
        v = 1
    # Verticais
    elif matriz[0][0] == matriz[1][0] == matriz[2][0] != ' ':
        v = 1
    elif matriz[0][1] == matriz[1][1] == matriz[2][1] != ' ':
        v = 1
    elif matriz[0][2] == matriz[1][2] == matriz[2][2] != ' ':
        v = 1
    # Diagonais
    elif matriz[0][0] == matriz[1][1] == matriz[2][2] != ' ':
        v = 1
    elif matriz[0][2] == matriz[1][1] == matriz[2][0] != ' ':
        v = 1
    else:
        v = 0
    return v


print('Bem vindo ao jogo da velha ggOS')
print()
print('Instruções:\n'
      'Pense em um teclado de telefone na hora de fazer sua jogada\n'
      '[1] [2] [3]\n'
      '[4] [5] [6]\n'
      '[7] [8] [9]\n ')
tabuleiro = []
c = 0
vf = 0
jogadas = []
# Criação da matriz, transformar em List Comprehension
for i in range(3):
    tabuleiro.append([])
    for j in range(3):
        tabuleiro[i].append(' ')

while c != 9 and vf != 1:
    if c % 2 == 0:
        jogada = input('(Jogador 1) Insira sua jogada: ')
        if not jogada.isnumeric() or int(jogada) in jogadas or int(jogada) > 9 or int(jogada) < 1:
            print()
            print('Jogada inválida\n')
            continue
        else:
            jogadas.append(int(jogada))
            jogada = conversor(jogada)
            x = jogada[0]  # Otimizar
            y = jogada[1]
            tabuleiro[x][y] = 'X'
            c += 1
            vf = verificador(tabuleiro)
        if vf == 1:
            print()
            print('Jogador 1 venceu!\n')
    else:  # Nesse laço condicional será construída a jogada do robô
        jogada = input('(Jogador 2) Insira sua jogada: ')
        if not jogada.isnumeric() or int(jogada) in jogadas or int(jogada) > 9 or int(jogada) < 1:
            print()
            print('Jogada inválida\n')
            continue
        else:
            jogadas.append(int(jogada))
            jogada = conversor(jogada)
            x = jogada[0]  # Otimizar
            y = jogada[1]
            tabuleiro[x][y] = 'O'
            c += 1
            vf = verificador(tabuleiro)
        if vf == 1:
            print()
            print('Jogador 2 venceu!\n')
        if c == 9:
            print('Não houve vencedor')
    for i in range(3):
        for j in range(3):
            print(f'[{tabuleiro[i][j]:^1}]', end='')
        print()
    print()
print()
print('powered by ggOS')
