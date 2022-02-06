import random
import time


def displayIntro():
    print('Вы находитесь в землях заселёными драконами.')
    print('Перед вами две пещеры в одной хороший в')
    print('другой плохой выберите одну из двух')
    print()


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('в какую пещеру зайдёте? Нажмите клавишу (1 или 2)')
        cave = input()
    return cave


def checkCave(chosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Её темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('большой дракон выскакивает перед вами!...')
    print()
    time.sleep(2)
    friendlyCave = random.randint(1, 2)
    if chosenCave == str(friendlyCave):
        print('Делится с вами своими сокровищами!')
    else:
        print('....моментально вас седает!!!')


playAgain = 'да'
while playAgain != '':

    if playAgain == 'да' or playAgain == 'д':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
        print('Попытаешь удачу еще раз? (да или нет)')
        playAgain = input()

    elif playAgain != 'да' and playAgain != 'д' and playAgain != 'нет' and playAgain != 'н':

        print('Я ограничен в ответах напиши пожалуйста (да или нет)')
        playAgain = input()

    elif playAgain == 'нет' or playAgain == 'н':
        print('Ладно пока мой друг')
        break
