from re import T
import re
from turtle import width
from unittest.main import main
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


if __name__ == "__main__":
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    menu = Menu()
    is_on = True

    while is_on:
        option = menu.get_items()
        choice = input(f'What would you like? ({option}): ')

        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
            else:
                print('no')