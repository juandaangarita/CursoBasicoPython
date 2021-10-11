def print_power(number,nth):
    i = 0
    while (i <= nth):
        nth_power = number ** i
        print(str(number) + " raised to " + str(i) +" power is: "+ str(nth_power))
        i += 1


def run():
    number = int(input('Enter a number you want to raised until to the nth power: '))
    nth = int(input('Enter the nth power: '))
    print_power(number,nth)


if __name__ == '__main__':
    run()        