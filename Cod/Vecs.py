import random
from time import sleep
import sys
c = 0
print('\033[32m-=\033[m'*30)
print('                 \033[4;32mVOCÊ ESTA COM SORTE ?\033[m')
print('\033[32m-=\033[m'*30)
print('\033[1:33mNeste jogo você tem que descobrir em qual numero estou pensando,')
print('Quanto maior o seu multiplicador maior a dificuldade !\033[m')
print('''\033[1;32m
[1]-[JOGAR]\033[m\033[1;31m
[2]-[SAIR]\033[m''')
print('')
print('\033[1:33mINFORME QUAL DESEJA')

nv = int(input('DIGITE: \033[m').strip())
bet = 0
x = 0
odd = 0
if nv == 1:
    print('\033[32m-=\033[m' * 30)
    print('                 \033[4;32mVOCÊ ESTA COM SORTE ?\033[m')
    print('\033[32m-=\033[m' * 30)
    bet = float(input('\033[1;33mQual o Valor da aposta ?(Minimo R$1.00): '))
    if bet < 1.0:
        while bet < 1.0:
            print('Valor invalido! Digite um valor acima de R$1.00')
            bet = float(input('Digite um valor acima de R$1.00: '))
    x = float(input('Informe quantos x deseja apostar(Minimo 1.1x): '))
    if x < 1.1:
        while x < 1.1:
            print('Multiplicador Invalido !')
            x = float(input('Digite um multiplicador acima de 1.1x: '))
    odd = bet * x
    print('\033[32m-=\033[m'*30)
    print('\033[33mVocê apostou R${} em {}x e pode ganhar R${:.2f}'.format(bet, x, odd))
    print('\033[32m-=\033[m' * 30)
    print(end='\033[4;33mQual o numero ?')
    if x >= 1.1 and x <= 1.5:
        num = random.randint(0, 5)
        print(' Entre 0 a 5',)
    elif x > 1.5 and x < 2:
        num = random.randint(0, 10)
        print(' Entre 0 a 10')
    elif x >= 2 and x <=4:
        num = random.randint(0, 15)
        print(' Entre 0 a 15')
    elif x >4 and x <6:
        num = random.randint(0, 20)
        print(' Entre 0 a 20')
    elif x >= 6 and x < 8:
        num = random.randint(0, 35)
        print(' Entre 0 a 35')
    elif x >= 8 and x <= 10:
        num = random.randint(0, 45)
        print(' Entre 0 a 45')
    elif x > 10:
        num = random.randint(0, 70)
        print(' Entre 0 a 70')
    print('\033[m\033[32m-=\033[m' * 30)
    elite = int(input('\033[m\033[33mQual é o numero? '))
    if elite == num:
        print('\033[m\033[32m-=\033[m' * 30)
        print('\033[33mPARABÉNS VOCÊ ACERTOU O NUMERO É {} !'.format(num))
        print('\033[m\033[32m-=\033[m' * 30)
        print('\033[33mVocê recebeu \033[32m+ R${}\033[m \033[33mna sua conta ! '.format(odd))
    else:
        print('É uma pena você ERROU !, o numero era {}'.format(num))
        print('Você perdeu R${} na sua conta !'.format(bet))
    print('\033[m\033[32m-=\033[m' * 30)
    nv = int(input('Digite 0 para voltar ao Inicio: '))
    #Fazer o voltar ao inicio

