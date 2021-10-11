def palindrome(word):
    word = word.replace(' ','')
    word = word.lower()
    word_inverted = word[::-1]
    if word == word_inverted:
        return True
    else:
        return False


def run():
    word = input('Please write a word: ')
    is_palindrome = palindrome(word)
    if is_palindrome :
        print('The word you enter is a palindrome')
    else:
        print('The word is not a palindrome')

# Este bloque lo que le indica a Python es la funcion inicial que debe correr al iniciar el proceso, es una buena práctica para identificar el orden preciso de lo que debe realizar lo que estamos programando. Es una buena práctica, además de esto es importante que entre dos funciones existan 2 líneas para separarlas como una buena práctica.

if __name__ == '__main__':  # Definición de la función que se va a inicializar
    run()                    # Acá se escribe la función inicial que debe ejecutar el programa.