import random

def jogar():
    print('*********************************')
    print('** Bem vindo no jogo de Forca! **')
    print('*********************************')

    palavras = []

    with open('palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    # enquanto não enforcou e não acertou
    while(not acertou and not enforcou):

        chute = input('Qual letra? ')
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print('Ops, você errou!! Faltam {} tentativas!!'.format(len(palavra_secreta)-erros))

        enforcou = erros == len(palavra_secreta)
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('\nVocê ganhou!!\n')
        print('A palavra secreta é: {}!!\n'.format(palavra_secreta))
    else:
        print('\nVocê perdeu!!\n')
        print('A palavra secreta era: {}!!\n'.format(palavra_secreta))

    print('Fim do jogo!!')

if(__name__ == '__main__'):
    jogar()