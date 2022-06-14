from calculator import logo


def function_name(f_name, l_name):
    return f"{f_name} {l_name}".title()


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 29 if is_leap(year) else 28, 31, 30,
                  31, 30, 31, 31,
                  30, 31, 30, 31]

    return month_days[month - 1]


def calculator():
    print(logo)

    def add(n_1, n_2):
        return n_1 + n_2

    def subtract(n_1, n_2):
        return n_1 - n_2

    def multiply(n_1, n_2):
        return n_1 * n_2

    def divide(n_1, n_2):
        return n_1 / n_2

    result = 0
    text_display = ""
    should_continue = True

    while should_continue:
        if text_display != "" and result != 0:
            mode = input("""Pick an operation form the line above (+, -, *, /)\n
                         or Type [e] to exit or Type [c] to clear : """)
            text_display += f' {mode}'

        try:
            if mode == "e":
                should_continue = False
                return True
            elif mode == "c":
                should_continue = False
                calculator()
                return True
        except UnboundLocalError:
            pass

        u_number = int(input("What's your number? : "))

        operators = {
            "+": add(result, u_number),
            "-": subtract(result, u_number),
            "*": multiply(result, u_number),
            "/": divide(result, u_number)
        }

        result = u_number if result == 0 else operators[mode]
        text_display += f' {u_number}'

        print(f'{text_display} = {result}')


if __name__ == '__main__':

    calculator()

    # print(days_in_month(2020, 2))

    # print(function_name("angela", "yu"))