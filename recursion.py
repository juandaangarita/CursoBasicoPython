def factorial(number):
    """
    Calculate the factorial of a integer number > 0

    :param number: Number you want to know the factorial n > 0
    :type number: int
    :returns: Factorial of number n!
    """
    if number == 1 or number == 0:
        return 1
    return number * factorial(number - 1)


def run():
    
    n = int(input('Write a integer: '))
    print(factorial(n))


if __name__ == '__main__':
    run()
