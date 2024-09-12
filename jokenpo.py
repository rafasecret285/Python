def resultado(player1, player2):
    if player1 == player2:
        ganhador ='empate'
    elif player1 == 'pedra' and player2 == 'tesoura':
        ganhador = player1
    elif player1 == 'pedra' and player2 == 'papel':
        ganhador = player2
    elif player1 == 'papel' and player2 == 'tesoura':
        ganhador = player2
    elif player1 == 'papel' and player2 == 'pedra':
        ganhador = player1
    elif player1 == 'tesoura' and player2 == 'pedra':
        ganhador = player2
    elif player1 == 'tesoura' and player2 == 'papel':
        ganhador = player2
    else:
        ganhador = 'selecione pedra, papel ou tesoura'

    return ganhador
    

player1 = input('Jogador1: ')
player2 = input('Jogador2: ')

ganhador = resultado(player1, player2)

if ganhador == player1:
    print('O jogador 1 ganhou!')
elif ganhador == player2:
    print('O jogador 2 ganhou!')
elif ganhador == 'empate':
    print('Deu empate')
else:
    print(ganhador)


    
    
