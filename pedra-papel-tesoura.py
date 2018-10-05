from random import choice
from time import sleep

print('-=' * 25)
user = input('Escreva \033[1;34mPEDRA\033[m, \033[1;33mPAPEL\033[m ou \033[1;31mTESOURA\033[m: ')
print('-=' * 25)

user = user.upper()
user = user.strip()
pedra , papel, tesoura = 1, 2, 3
lista = [pedra, papel, tesoura]
pc = choice(lista)

sleep(0.2)
print('\033[1mJO\033[m')
sleep(0.5)
print('\033[1mKEN\033[m')
sleep(0.5)
print('\033[1mPO\033[m')
sleep(0.25)
print('-='*35)

if user == 'PEDRA':
    if pc == pedra:
        print('EMPATE, você escolheu \033[1;34mPEDRA\033[m e o computador também escolheu \033[1;34mPEDRA\033[m')
    elif pc == papel:
        print('DERROTA, você escolheu \033[1;34mPEDRA\033[m e o computador escolheu \033[1;33mPAPEL\033[m')
    elif pc == tesoura:
        print('VITÓRIA, você escolheu \033[1;34mPEDRA\033[m e computador escolheu \033[1;31mTESOURA\033[m')
elif user == 'PAPEL':
    if pc == pedra:
        print('VITÓRIA, você escolheu \033[1;33mPAPEL\033[m e o computador escolheu \033[1;34mPEDRA\033[m')
    elif pc == papel:
        print('EMPATE, você escolheu \033[1;33mPAPEL\033[m e o computador também escolheu \033[1;33mPAPEL\033[m')
    elif pc == tesoura:
        print('DERROTA, você escolheu \033[1;33mPAPEL\033[m e o computador escolheu \033[1;31mTESOURA\033[m')
elif user == 'TESOURA':
    if pc == pedra:
        print('DERROTA, você escolheu \033[1;31mTESOURA\033[m e o computador escolheu \033[1;34mPEDRA\033[m')
    elif pc == papel:
        print('VITÓRIA, você escolheu \033[1;31mTESOURA\033[m e o computador escolheu \033[1;33mPAPEL\033[m')
    elif pc == tesoura:
        print('EMPATE, você escolheu \033[1;31mTESOURA\033[m e o computador também escolheu \033[1;31mTESOURA\033[m')
else:
    print('ERRO, COMANDO INVÁLIDO')

print('-='*35)
