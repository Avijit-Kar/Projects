
from tkinter import N
import requests
from difflib import get_close_matches
import  json

#function for calling api
def input(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+ word

    headers = {}

    response = requests.request("GET", url, headers=headers)

    #print(response.json())
    try:
        window['-OUTPUT-'].update('results:')
        s = response.json()[0]['meanings'][0]['synonyms']
        a = response.json()[0]['meanings'][0]['antonyms']
        d = response.json()[0]['meanings'][0]['definitions'][0]['definition']
    # results if word is correct
        return {'meaning' : d,
    'synonyms':s,
    'antonyms': a
    }

    # if word is correct
    except:
        data = json.load(open('data.json')) # word stacks
        p_w = list(get_close_matches(word, data.keys(), cutoff=0.5)) # closest word 
        if p_w:
            window['-OUTPUT-'].update('did you mean :' + str(p_w)) # result warning (closest words)
        
        #url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+ p_w
        #response = requests.request("GET", url, headers=headers)
        

        # results if word is not correct
        #s = response.json()[0]['meanings'][0]['synonyms']
        #a = response.json()[0]['meanings'][0]['antonyms']
        #d = response.json()[0]['meanings'][0]['definitions'][0]['definition']
        return {'meaning' : None,
    'synonyms':None,
    'antonyms': None
    }
   

import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("What's your word?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Multiline(key='-ML1-', size=[30,10])],
            [sg.Button('search'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Dictionary', layout, size=(250, 350))

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    word_d = input(values['-INPUT-'])
    
    window['-ML1-'].update(str(word_d['meaning']) + '\n \n synonyms: '+ str(word_d['synonyms']) +
    '\n \n antonyms: '+ str(word_d['antonyms']))
  
   

# Finish up by removing from the screen

window.close()