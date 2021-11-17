def fibonacci(nth):
    fibonacci_sequence = [0, 1]
    for i in range(2, nth + 1):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    print(fibonacci_sequence) 


def fibonacci_recursion(nth):
    """
    Calculate fibonacci sequence of a number in a recursive way
    :param nth: Number nth you want to calculate fibonnaci sequence
    type: int
    returns: Fibonnaci sequence of nth
    """
    if nth == 0 or nth == 1:
        return 1

    return fibonacci_recursion(nth - 1) + fibonacci_recursion(nth - 2)

def run():
    print('This is a program to calculate a Fibonacci sequence')
    nth = int(input('Enter the number nth number you want to calculate: '))
    fibonacci(nth)
    print(fibonacci_recursion(nth))


if __name__=='__main__':
    run()