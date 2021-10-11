def multiplication_table(number):
    for i in range (10):
        print(str(number) + ' x ' + str(i) + ' = ' + str(number*i))


def run():
    number = int(input('Enter the number you want to know the multiplication table: '))
    multiplication_table(number)


if __name__ == '__main__':
    run() 