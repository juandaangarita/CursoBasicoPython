def aproximation_solution(objective, epsilon = 0.001):
    step = epsilon ** 2
    answer = 0.0

    while abs(answer ** 2 - objective) >= epsilon and answer <= objective:
        answer += step

    if abs(answer ** 2 - objective) >= epsilon:
        print(f'Could not obtein the square root of {objective}')
    else:
        print(f'The square root of {objective} is {answer}')


def run():
    number = int(input('Please enter a number: '))
    aproximation_solution(number)


if __name__ == '__main__':
    run()