def add(*args):
    result = 0
    for n in args:
        result += n

    return result


def calculate(**kwargs):
    print(kwargs)


if __name__ == "__main__":
    calculate(add=3, multiply=5)