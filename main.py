#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: aslusarz

# FROM ZERO TO PYTHON HERO series
# Script No#3: Simple game called: Koło Fortuny (Wheel of fortune)
# File created: 08.01.17
# Last modified: 26.01.17
# Version: P.3.001-B [P:Prototype, F:Final]

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

WHEEL = ['BANKRUT', 10, 25, 50, 100, 150, 200, 250, 300, 500, 600, 1000, 1500, 2000, '+']

def random_category():
    category = random.randint(0, 5)
    category_name = CATEGORIES[category]
    return [category, category_name]

def random_question(category):
    categories_length = len(VALUES[category])
    question = random.randint(0, categories_length - 1)
    return VALUES[category][question].upper()

def print_question(question, SUP, TUP):
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
    return (new_question, TUP)

def check_sign(sign, question, SUP):
    i = 0
    for l in question:
        if l == sign and l not in SUP:
            i += 1
    if i > 0 and sign not in SUP:
        SUP.append(sign)
    return (i, SUP)

def check_pass(SUP, TUP):
    len_1 = len(SUP)
    len_2 = len(TUP)
    if len_1 == len_2:
        return True
    else:
        return False

def start_new_game():
    game_continue = True
    while game_continue:
        SUP = []
        TUP = []
        points = 0
        lives = 5
        quest_pass = False
        category = random_category()
        category_name = category[1]
        question_original = random_question(category[0])
        while quest_pass != True:
            os.system('clear')
            key = ''
            computed_question = print_question(question_original, SUP, TUP)
            prnt_question = computed_question[0]
            TUP = computed_question[1]
            print ('PUNKTY: {0} | Pozostało prób: {1}'.format(points, lives))
            print ('Wylosowana kategoria: {0}'.format(category_name))
            print ('Hasło: {0}'.format(prnt_question))
            if check_pass(SUP, TUP):
                quest_pass = True
                break
            while key not in ['L', 'H']:
                key = input('\nZakręć kołem fortuny [L] lub odgadnij hasło [H]: ').upper()
            if key == 'L':
                wheel = random.randint(0, len(WHEEL) - 1)
                wheel_points = WHEEL[wheel]
                key = None
            elif key == 'H':
                key = None
                print ('Wpisz hasło i naciśnij ENTER')
                passw = input().upper()
                if passw == question_original:
                    print ('Hasło prawidłowe! Zyskałeś bonus')
                    points += round(points * 0.25)
                    break
                else:
                    print ('Nieprawidłowe hasło, utrata 0.25 punktów')
                    points -= round(points * 0.25)
                while key != 'A':
                    key = input('\nNaciśnij klawisz [A] i zatwierdź klawiszem ENTER: ').upper()
            print ('Wynik losowania koła fortuny: {0}\n'.format(wheel_points))
            if wheel_points not in ['BANKRUT', '+']:
                sign = input('Zgadnij literę: ').upper()
                computed_result = check_sign(sign, question_original, SUP)
                result = computed_result[0]
                SUP = computed_result[1]
                print ('Znak {0} wystąpił {1} razy w zgadywanym haśle'.format(sign, result))
                if result == 0:
                    print ('Utrata liczby prób')
                    lives -= 1
                    if lives == 0:
                        print ('Utracono wszystkie próby, koniec gry :-(')
                        break
                points += result * wheel_points
            elif wheel_points == '+':
                lives += 1
                print ('Zyskałeś dodatką próbę')
            else:
                print ('Utrata punktów')
                points = 0
            while key != 'A':
                key = input('\nNaciśnij klawisz [A] i zatwierdź klawiszem ENTER: ').upper()
        os.system('clear')
        print ('Zdobyłeś {0} punków!'.format(points))
        key = input('\nKontynuuj [T] lub zakończ grę [N]: ').upper()
        if key == 'T':
            del (SUP)
            del (TUP)
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
