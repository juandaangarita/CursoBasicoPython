def prime_number(number):
    if number == 1:
        return False
    else:
        flag = 0
        for i in range(1, number + 1):
            if i ==1 or i == number:
                continue
            if number % i == 0:
                flag += 1
    if flag == 0:
        return True
    else:
        return False


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        fact = 1
        while number > 1:
            fact *= number
            number -= 1
        return fact



def prime_number_Wilson(number):
    if number == 1:
        return False
    elif (factorial(number - 1) + 1) % number == 0:
        return True
    else:
        return False


def run():
    number = int(input('Write the number you want to know if it is a prime number: '))
    if prime_number(number):
        print(str(number) + ' is a prime number')
    else:
        print(str(number) + ' is not a prime number')
    number = int(input('Write the number you want to know if it is a prime number: '))
    if prime_number_Wilson(number):
        print(str(number) + ' is a prime number')
    else:
        print(str(number) + ' is not a prime number')


if __name__ == '__main__':
    run()