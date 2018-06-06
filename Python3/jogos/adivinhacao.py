import random

print('*********************************')
print('Bem vindo no jogo de Adivinhação!')
print('*********************************')

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
nivel = 0
pontos = 100

while (total_de_tentativas == 0):

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Escolha o nível: '))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel ==3):
        total_de_tentativas = 5
    else:
        print('Nível inválido!')

for rodada in range(1,total_de_tentativas + 1):

    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute_str = input('Digite um número entre 1 e 100: ')
    print('Você digitou: ', chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print('Você deve digitar um número entre 1 e 100!')
        continue

    acertou = (chute == numero_secreto)
    maior = (chute > numero_secreto)

    if(acertou):
        print('Fim do jogo!')
        print('Você acertou e fez {} pontos!'.format(pontos))
        break

    elif(maior):
        pontos = pontos - abs(numero_secreto - chute) - nivel
        print('Você errou! O seu chute foi MAIOR do que o número secreto. Pontuação: {}'.format(pontos))

    else:
        pontos = pontos - abs(numero_secreto - chute) + nivel
        print('Você errou! O seu chute foi MENOR do que o número secreto. Pontuação: {}'.format(pontos))

    if(pontos <= 0):
        print('Fim do jogo!')
        print('Você perdeu pois não conseguiu acertar o número antes de sua pontuação zerar! Pontuação: {}'.format(pontos))
        break