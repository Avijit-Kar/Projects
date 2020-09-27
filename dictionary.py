"Hello World"
import json
import webbrowser
import time
from difflib import get_close_matches


def GOOGLE(word):
    print('Loading...')
    time.sleep(1)
    url = 'https://www.google.com/search?q={}'.format(word)
    return webbrowser.open(url)


def translate(word):
    data = json.load(open('data.json'))
    w = word.lower()
    if w in data:

        print(data[w])

    elif len(get_close_matches(w, data.keys())) > 0:
        possibe_word = list(get_close_matches(w, data.keys(), cutoff=0.5))
        print(f'Did you mean {get_close_matches(w, data.keys(), cutoff=0.5)}?')
        while True:
            search = input('If not to Search in Google type "y" else "n": ')
            if search.lower() == 'y' or search.lower() == 'n':

                break
            else:
                print('Give Proper Command !!')
        while search.lower() == 'n':
            print(f'Did you mean {get_close_matches(w, data.keys(), cutoff=0.5)}?')

            choose_word = int(input('To choose the word, Type 0, 1 or 2 :  '))

            if choose_word == 0 or choose_word == 1 or choose_word == 2:
                print(f'word is "{possibe_word[choose_word]}" and defination of this word is:- \n {data[possibe_word[choose_word]]}')
                break
            else:
                print('Sorry! give a proper command.')


        if search.lower() == 'y':

            GOOGLE(w)

    else:
        while True:
            inp = input('Want to search in Google? Type "y" else type "n": ')
            if inp.lower() == 'y':
                GOOGLE(w)
                break
            elif inp.lower() == 'n':
                print('THANK YOU !!')
                break

            else:
                print('Give Proper Command.')


word = input('Type word: ')

translate(word)




