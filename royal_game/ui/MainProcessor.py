from royal_game.controller.FrontController import FrontController
from royal_game.action.Action import *
import sys


class MainProcessor:

    # control all of flows on this program
    fc = FrontController

    while True:
        ac = None

        # print menu
        print('=== Rolay Game ===')
        print('1. Apply new account')
        print('2. Login')
        print('3. Finish')
        print('==================')

        # User input the number of menu
        num = int(input('menu: '))

        # apply new account
        if num == 1:
            ac = AddMemberAction()

        elif num == 2:
            print('num')

        elif num == 3: # Finish
            print('finish the Royal Game')
            sys.exit()


        else: # user input wrong number
            print('please check your input number')

        print()

        if ac is not None:
            fc.proessRequest(ac)
