secret_word = 'pyyyme'
check_word = secret_word
users_word = len(secret_word) * '_'
error_counter = 0
stages = [
    "________        ",
    "|               ",
    "|       |       ",
    "|       0       ",
    "|      /|\      ",
    "|      / \      ",
    "|               "]


def game_start():
    print('Execution has begun')
    print('Keyword is ', users_word)
    for i in range(error_counter):
        print(stages[i])
    try_to_guess(check_word)


def try_to_guess(word):
    global error_counter
    global users_word
    global check_word
    print('Try to guess word letter')
    letter = input()
    str_list = list(check_word)
    str1_list = list(users_word)
    if letter in word:
        str_list[word.index(letter)] = '_'
        check_word = ''.join(str_list)
        str1_list[word.index(letter)] = letter
        users_word = ''.join(str1_list)
        if users_word == secret_word:
            print('You won, gratz')
        else:
            game_start()
    else:
        error_counter += 1
        if error_counter == 8:
            print('Game over')
        else:
            game_start()


def main():
    game_start()


if __name__ == '__main__':
    main()
