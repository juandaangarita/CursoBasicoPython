# def print_message ():
#     print ("This is a especial message: ")
#     print("I am practicing functions with python on Platzi 💚")

# print_message()

def conversation_with_the_machine (message):
    print("Hi, Welcome 😎")
    print("How are you?")
    print (message)
    print("See you soon")


option = int(input("Please choose an option (1, 2, 3): "))
if option == 1:
    conversation_with_the_machine("You choose the option 1")
elif option == 2:
    conversation_with_the_machine("You choose the option 2")
elif option == 3:
    conversation_with_the_machine("You choose the option 3")
else:
    print("You didn't choose anything, please try it again.")


