str = input()


def palindrom(str):
    a = str[::-1]
    if str == a:
        return print(True)
    else:
        return print(False)


palindrom(str)