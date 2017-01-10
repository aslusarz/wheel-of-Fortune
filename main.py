#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: aslusarz

# FROM ZERO TO PYTHON HERO series
# Script No#3: Simple game called: Koło Fortuny (Wheel of fortune)
# File created: 08.01.17
# Last modified: 00.00.17
# Version: P.3.001-0 [P:Prototype, F:Final]

import os
import random

CATEGORIES = {0: 'Film', 1:'Muzyka', 2:'Zwierzęta', 3:'Ptaki', 4:'Literatura', 5:'Motoryzacja', 6:'Sławne postacie'}
VALUES = {  0: [    'Drive',
                    '12 gniewnych ludzi',
                    'Matrix',
                    'Pojutrze'],
            1: [    'I Am The Architect',
                    'Kiss',
                    'The Killers'],
            2: [    'Kot',
                    'Pies',
                    'Krokodyl'],
            3: [    'Kuropatwa',
                    'Bocian',
                    'Pliszka'],
            4: [    'Ogniem i Mieczem',
                    'Lalka',
                    'Nad Niemnem'],
            5: [    'Filtr cząstek stałych',
                    'Koło dwumasowe',
                    'Wał rozrządu'],
            6: [    'Bolesław Prus',
                    'Adam Mickiewicz']}

WHEEL = ['BANKRUT', 10, 25, 50, 100, 200, 250, 500, 1000, 1500, 2000, '+']
SUP = []
TUP = []

def random_category():
    category = random.randint(0, 5)
    category_name = CATEGORIES[category]
    return [category, category_name]

def random_question(category):
    categories_length = len(VALUES[category])
    question = random.randint(0, categories_length - 1)
    return VALUES[category][question].upper()

def print_question(question):
    new_question = ''
    for l in question:
        if l in SUP:
            new_question += ' ' + l + ' '
        elif l == ' ':
            new_question += '-'
        else:
            new_question += ' _ '
        if l not in TUP and l != ' ':
            TUP.append(l)
    return new_question

def check_sign(sign, question):
    i = 0
    for l in question:
        if l == sign and l not in SUP:
            i += 1
    if i > 0 and sign not in SUP:
        SUP.append(sign)
    return i

def check_pass():
    len_1 = len(SUP)
    len_2 = len(TUP)
    if len_1 == len_2:
        return True
    else:
        return False

def start_new_game():
    game_continue = True
    while game_continue:
        points = 0
        lives = 5
        quest_pass = False
        category = random_category()
        category_name = category[1]
        question_original = random_question(category[0])
        while quest_pass != True:
            os.system('clear')
            key = ''
            print ('PUNKTY: {0} | Pozostało prób: {1}'.format(points, lives))
            print ('Wylosowana kategoria: {0}'.format(category_name))
            print ('Hasło: {0}'.format(print_question(question_original)))
            if check_pass():
                quest_pass = True
                break
            while key != 'L':
                key = input('\nZakręć kołem fortuny [L] lub odgadnij hasło [H]: ').upper()
            if key == 'L':
                wheel = random.randint(0,len(WHEEL) - 1)
                wheel_points = WHEEL[wheel]
                key = None
            print ('Wynik losowania koła fortuny: {0}\n'.format(wheel_points))
            if wheel_points not in ['BANKRUT', '+']:
                sign = input('Zgadnij literę: ').upper()
                result = check_sign(sign, question_original)
                print ('Znak {0} wystąpił {1} razy w zgadywanym haśle'.format(sign, result))
                if result == 0:
                    lives -= 1
                    if lives == 0:
                        break
                points += result * wheel_points
            elif wheel_points == '+':
                lives += 1
                print ('Zyskałeś dodatką próbę')
            else:
                print ('Utrata punktów')
                points = 0
            while key != 'A':
                key = input('\nNaciśnij klawisz [A] i zatwierdź klawiszem ENTER').upper()
        key = input('\nKontynuuj [T] lub zakończ grę [N]: ').upper()
        if key == 'T':
            continue
        else:
            break


def main():
    key = ''
    keys = ('N', 'W')
    print('KOŁO FORTUNY')
    while key not in keys:
        key = input('[N] - Nowa gra \n[W] - Wyjście \n Twój wybór:').upper()
        if key == 'N':
            start_new_game()
        elif key == 'W':
            continue

main()
