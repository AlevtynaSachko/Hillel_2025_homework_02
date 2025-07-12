while True:
    word = input("Введіть слово з літерою 'h': ")
    if 'h' in word.lower():
        print("Дякую, у слові є літера 'h'!")
        break
    else:
        print("Нажаль,в цьому слові літера 'h' відсутня. Спробуйте ще раз!")