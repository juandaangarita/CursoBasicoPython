def exhaustive_enumeration(objective):
    answer = 0

    while answer ** 2 < objective:
        answer += 1

    if answer ** 2 == objective:
        print(f'The square root of {objective} is {answer}')
    else:
        print(f'{objective} does not have an exact square root')


def run():
    number = int(input('Please choose a number: '))
    exhaustive_enumeration(number)


if __name__ == '__main__':
    run()