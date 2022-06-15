from menu import MENU, resources

profit = 0


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True


def process_coins():
    coins = {'quarters': 0.25,
             'dimes': 0.1,
             'nickles': 0.5,
             'pennies': 0.01}

    total = 0

    for c in coins:
        total += int(input(f"How many {c}?: ")) * coins[c]

    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change.')

        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money.  Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕')


def coffee_machine():
    is_no = True

    while is_no:
        choose_menu = input('What would you like? (espresso/latte/cappuccino): ')

        if choose_menu == 'off':
            is_no = False
            return is_no
        elif choose_menu == 'report':
            print('Machine Status: ')
            [print(f'{k} = {v}{"ml" if k is not "coffee" else "g"}.') for k, v in resources.items()]
            print(f'Money: ${profit}')
        elif choose_menu in MENU.keys():
            drink = MENU[choose_menu]
            if is_resource_sufficient(drink['ingredients']):
                payment = process_coins()
                if is_transaction_successful(payment, drink['cost']):
                    make_coffee(choose_menu, drink['ingredients'])


if __name__ == '__main__':
    coffee_machine()