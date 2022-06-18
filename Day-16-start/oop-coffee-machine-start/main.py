from unittest.main import main
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


if __name__ == "__main__":
    all_report = CoffeeMaker()
    all_report.report()

    money_machine = MoneyMachine()
    money_machine.report()