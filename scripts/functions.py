def numbers_to_words (number):
    number2word = {'1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six",
            '7': "seven", '8': "eight", '9': "nine", '0': "zero"}
    return " ".join(map(lambda i: number2word[i], str(number)))