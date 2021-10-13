import aproximation_solutions
import binary_search
import exhaustive_enumeration


def run():
    print("""This are the options to calculate the square root of a number
    1 - Exhaustive solution
    2 - aproximation solution
    3 - Binary search
    4 - Exit""")
    option = 0
    while option != 4:
        option = int(input('Choose an option: '))
        if option == 4:
            print('Bye 😉')
            break
        elif option == 1:
            number = int(input('Please enter a number: '))
            exhaustive_enumeration.exhaustive_enumeration(number)
        elif option == 2:
            number = int(input('Please enter a number: '))
            aproximation_solutions.aproximation_solution(number)
        elif option == 3:
            number = int(input('Please enter a number: '))
            binary_search.binary_search(number)
        else:
            print('Choose a valid option')


if __name__ == '__main__':
    run()