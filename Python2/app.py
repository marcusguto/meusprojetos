#python2/app.py
# -*- coding: UTF-8 -*-

from datetime import date
import re

def cadastrar(nomes):
    print 'Digite o nome:'
    nome = raw_input()
    nomes.append(nome)

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def remover(nomes):
    print 'Qual nome gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)

def procurar(nomes):
    print 'Digite o nome a procurar:'
    nome_a_procurar = raw_input()
    if(nome in nomes):
        print 'Nome %s está cadastrado!' %(nome)
    else:
        print  'Nome %s NÃO está cadastrado!' %(nome)

def procurar_regex(nomes):
    print 'Digite a expressão regular'
    regex = raw_input()
    nomes_concatenados = ' '.join(nomes)
    resultados = re.findall(regex, nomes_concatenados)
    print resultados

def alterar(nomes):
    print 'Qual nome deseja alterar?'
    nome_a_alterar = raw_input()
    if(nome_a_alterar in nomes):
        posicao = nomes.index(nome_a_alterar)
        print 'Digite o novo nome:'
        nome_novo = raw_input()
        nomes[posicao] = nome_novo
    else:
        print 'Nome não consta da lista!'

def idade(idade):
    print 'Digite o ano de nascimento:'
    ano_como_string = raw_input()
    ano_como_int = int(ano_como_string)
    idade = date.today().year - ano_como_int
    print 'A idade e: %s' %(idade)

def remover(nomes):
    print 'Qual nome voce gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print 'Digite: 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para procurar, 6 para procurar por regex, 0 para terminar'
        escolha = raw_input()
        
        if(escolha == '1'):
            cadastrar(nomes)

        if(escolha == '2'):
            listar(nomes)

        if(escolha == '3'):
            remover(nomes)

        if(escolha == '4'):
            alterar(nomes)

        if(escolha == '5'):
            procurar(nomes)

        if(escolha == '6'):
            procurar_regex(nomes)

menu()