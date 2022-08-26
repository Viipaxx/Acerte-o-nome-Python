from random import choice
from os import system

chave = ['Clayton', 'Vitor', 'Pedro', 'Lucas', 'Andre', 'Bruno', 'Italo', 'David', 'Saulo', 'Maria', 'Mario', 'Pedro', 'Marco', 'Julia', 'Julio', 'Jesus', 'Saulo', 'Elias', 'Alice', 'Laura', 'Sofia', 'Sarah', 'Carol', 'Thais', 'Emily', 'Denis', 'Isaac', 'Roger', 'Steve', 'Kevin', 'Peter', 'Diego', 'Diogo', 'Marta', 'Zelia', 'Celia', 'Drake', 'Cesar', 'Paulo', 'Jakob', 'Carla', 'Igor',
         'Juraci', 'Inacio', 'Inadilson', 'Fernanda', 'Fernando', 'Junior', 'Leandro', 'Patricia', 'Mariane', 'Mariane', 'Iara', 'Kelvin', 'Manoel', 'Jose', 'Marlon', 'Cleverton', 'Miguel', 'Luiz', 'Joao', 'Amanda', 'Larissa', 'Anna', 'Beatriz', 'Gabriel', 'Gabriela', 'Marcelo', 'Hentony', 'Wanderson', 'Geivison', 'Caua', 'Kaua', 'Yuri', 'Vanessa', 'Analyce', 'Caio', 'Vitoria', 'Adelmo', 'Sergio', 'Luiza', 'Rafael', 'Maggie', 'Chico', 'Karen', 'Mirela', 'Marcia', 'Anunciada', 'Clarice']
palavra = ''
chave = choice(chave).lower()
print('\033[35mRegras: \n1ª - O usuário tem 5 chances para acertar o nome; \n2ª - Letras vermelhas não tem na palavra chave; \n3ª - Letras amarelas estão na posição errada; \n4ª - Letras verdes estão na posição certa; \nBoa Sorte!!!\033[m')
resp = str(input('\n\n\033[35mQuer Começar? [S / N]: \033[m'))
if resp in 'Ss':
    i = 1
    system('cls')
    while i <= 5 and palavra != chave:
        print(f'\033[34mTentativa {i}\033[m')
        palavra = input(
            f'\033[34mDigite um nome ({len(chave)} letras):  \033[m').lower()
        while len(palavra) != len(chave):
            palavra = input(f'\033[34mErro! insira uma palavra com {len(chave)} letras: \033[m').lower()
        for c in range(0, len(chave), 1):
            if palavra[c] in chave:
                if palavra[c] == chave[c]:
                    print(f'\033[32m{palavra[c]}\033[m', end='')
                else:
                    print(f'\033[33m{palavra[c]}\033[m', end='')
            else:
                print(f'\033[31m{palavra[c]}\033[m', end='')

        print('')
        i += 1
    if palavra == chave:
        print('\033[32mParabéns\033[m')
    else:
        print('\033[31mNão foi dessa vez! Tente Novamente!\033[m')
        print(f'\033[32mNome correto: {chave}\033[m')
    input('Aperte "Enter" para sair!')
