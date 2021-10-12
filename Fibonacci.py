def fibonacci(nth):
    fibonacci_sequence = [0, 1]
    for i in range(2, nth + 1):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    print(fibonacci_sequence) 


def run():
    print('This is a program to calculate a Fibonacci sequence')
    nth = int(input('Enter the number nth number you want to calculate: '))
    fibonacci(nth)


if __name__=='__main__':
    run()