num = input("Enter first number: ")
nth = int(input("Enter second number: "))


def find_digits(num, nth):
    while True:
        if nth < 0:
            print(-1)
            break
        if len(num) < nth:
            print(0)
            break
        else:
            print(num[-nth])


find_digits(num, nth)
