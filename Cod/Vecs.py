import random
from time import sleep
import os
c = 0
menu = ''
while menu != 'N':
    print('\033[32m-=\033[m'*30)
    print('                 \033[4;32mVOCÊ ESTA COM SORTE ?\033[m')
    print('\033[32m-=\033[m'*30)
    print('\033[1:33mNeste jogo você tem que descobrir em qual numero estou pensando, \nQuanto maior o seu multiplicador maior a dificuldade !\033[m')
    print('''\033[1;32m\n[1]-[JOGAR]\033[m\033[1;31m\n[2]-[SAIR]\033[m''')
    print('')
    print('\033[1:33mINFORME QUAL DESEJA')
    #SOLICITA A OPÇÃO QUE O USUARIO DESEJA SENDO 1 INICIAR O JOGO E 2 SAIR A SOLICITAÇÃO SE REPETE ATÉ QUE O USUARIO INSIRA O NUMERO VALIDO 1 OU 2
    while True:
        nv = input('DIGITE: \033[m').strip()
        if nv.isdigit():
            nv = int(nv)
            if nv in [1, 2]:
                break
            if nv != 1 or nv != 2:
                print('\033[1;31mPor favor, digite uma opção válida\033[m')
    os.system('cls')
    bet = 0
    x = 0
    odd = 0
    if nv == 1:
        print('\033[32m-=\033[m' * 30)
        print('                 \033[4;32mVOCÊ ESTA COM SORTE ?\033[m')
        print('\033[32m-=\033[m' * 30)
        #SOLICITA O VALOR QUE O USUARIO DESEJA APOSTAR, NÃO PODE SER MENOR QUE R$1.00 SE NÃO O PROGRAMA VAI SOLICITAR QUE DIGITE NOVAMENTE MESMA COISA COM NUMEROS INVALIDOS
        while True:
            bet = input('\033[mQual o Valor da aposta ?(Minimo R$1.00): ')
            if bet.replace('.','').isdigit():
                bet = float(bet)
                if bet > 1.0:
                    break
                else:
                    print('\033[31mPor favor, digite um número válido\033[m')
            else:
                print('\033[31mPor favor, digite um número válido\033[m')
        #SOLICITA O MULTIPLICADOR QUE O USUARIO DESEJA, NÃO PODE SER MENOR QUE 1.1 SE NÃO O PROGRAMA VAI SOLICITAR QUE DIGITE NOVAMENTE MESMA COISA COM NUMEROS INVALIDOS E SIMBOLOS OU LETRAS
        while True:
            x = input('Informe quantos x deseja apostar(Minimo 1.1x): ')
            if x.replace('.','').isdigit():
                x = float(x)
                if x > 1.0:
                    break
                else:
                    print('\033[31mPor favor, digite um número válido\033[m')
            else:
                print('\033[31mPor favor, digite um número válido\033[m')
        os.system('cls')
        odd = bet * x
        print('\033[32m-=\033[m' * 30)
        print('                 \033[4;32mVOCÊ ESTA COM SORTE ?\033[m')
        print('\033[32m-=\033[m' * 30)
        print('\033[32m-=\033[m'*30)
        print('\033[33mVocê apostou R${} em {}x e pode ganhar R${:.2f}'.format(bet, x, odd))
        print('\033[32m-=\033[m' * 30)
        print(end='\033[mQual o numero')
        #BASEADO NO MULTIPLICADOR É DEFINIDO A REGUA DE DESCOBERTA DO NUMERO PODENDO IR DE 0 A 5 ATÉ 0 A 70
        if x >= 1.1 and x <= 1.5:
            num = random.randint(0, 5)
            print(' entre 0 a 5!',)
        elif x > 1.5 and x < 2:
            num = random.randint(0, 10)
            print(' entre 0 a 10!')
        elif x >= 2 and x <=4:
            num = random.randint(0, 15)
            print(' entre 0 a 15!')
        elif x >4 and x <6:
            num = random.randint(0, 20)
            print(' entre 0 a 20!')
        elif x >= 6 and x < 8:
            num = random.randint(0, 35)
            print(' entre 0 a 35!')
        elif x >= 8 and x <= 10:
            num = random.randint(0, 45)
            print(' entre 0 a 45!')
        elif x > 10:
            num = random.randint(0, 70)
            print(' entre 0 a 70!')
        while True:
            elite = input('Digite: ')
            if elite.isdigit():
                elite = int(elite)
                break
            else:
                print('\033[31mPor favor, digite um número válido\033[m')
        #ACERTANDO O NUMERO QUE FOI ESCOLHIDO PELA MAQUINA INFORMA QUE A PESSOA ACERTOU E O VALOR RECEBIDO COM O MULTIPLICADOR
        if elite == num:
            print('\033[m\033[32m-=\033[m' * 30)
            print('\033[33mPARABÉNS VOCÊ ACERTOU O NUMERO É {} !'.format(num))
            print('\033[m\033[32m-=\033[m' * 30)
            print('\033[33mVocê recebeu \033[32m+ R${:.2f}\033[m \033[33mna sua conta ! '.format(odd))
        #ERRANDO O NUMERO QUE A MAQUINA ESCOLHEU O VALOR APOSTADO É PERDIDO.
        else:
            print('\033[31mVOCÊ ERROU ! O NUMERO ESCOLHIDO FOI\033[m {}'.format(num))
            print('\033[31mRETIRADO R${:.2f} DA SUA CONTA!'.format(bet))
        print('\033[m\033[32m-=\033[m' * 30)
        print('DIGITE 1 PARA RETORNAR AO MENU')
        while True:
            retmenu = input('DIGITE: ')
            if retmenu.isdigit():
                retmenu = int(retmenu)
                if retmenu == 1:
                    break
                else:
                    print('\033[31mPor favor, digite um número válido\033[m')
            else:
                print('\033[31mPor favor, digite um número válido\033[m')
        #LIMPAR TELA
        os.system('cls') 
    #SAIR DO SOFTWARE
    if nv == 2:
        print('\033[33mSaindo....')
        sleep(2)
        print('Até logo !\033[m')
        break