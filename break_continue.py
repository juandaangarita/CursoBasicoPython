def run():
    # for i in range (100):
    #     if i % 2 != 0:
    #         continue
    #     print(i)
    
    # for i  in range (1000):
    #     print(i)
    #     if i == 578:
    #         break

    text = input('Write a text: ')
    for letter in text:
        if letter =='o':
            break
        print(letter)



if __name__ =='__main__':
    run()