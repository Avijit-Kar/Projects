

from tkinter import N
from turtle import onclick
import requests
from difflib import get_close_matches
import  json


#function for calling api
def input(word):

    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+ word

    headers = {}

    response = requests.request("GET", url, headers=headers)

    
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
    
    # if word is NOT correct
    except:
        data = json.load(open('data.json')) # word stacks
        p_w = list(get_close_matches(word, data.keys(), cutoff=0.5)) # closest word 
        
        if p_w:
            window['-OUTPUT-'].update('did you mean :' + str(p_w)) # result warning (closest words)
        
        return {'meaning' : 'NO WORD FOUND !!',
    'synonyms':'',
    'antonyms': ''
    }
    
       
# GUI APP

import PySimpleGUI as sg

MLINE_KEY1 = '-MLINE1-' # input key
MLINE_KEY2 = '-MLINE2-' # output key
right_click_menu1 = ['', ['Copy', 'Paste', 'Cut']] # menu options 
right_click_menu2 = ['', ['Copy']] 

# app layout
layout = [[sg.Text("What's your word?")],
          [sg.Multiline(key=MLINE_KEY1,right_click_menu=right_click_menu1)],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Multiline(key=MLINE_KEY2, size=[50,10], right_click_menu=right_click_menu2, do_not_clear=False)],
            [sg.Button('search'), sg.Button('clear'), sg.Button('quit')]]


# Create the window
window = sg.Window('Dictionary', layout, size=(300, 350))
mline1:sg.Multiline = window[MLINE_KEY1] # option window set for input
mline2:sg.Multiline = window[MLINE_KEY2] # option window set for output

# Display and interact with the Window using an Event Loop
while True:    
    event, values = window.read()

    # if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'quit':
        break

    # copy paste cut option 
    
    elif event == 'Copy':
        try:
            text = mline1.Widget.selection_get()
            text = mline2.Widget.selection_get()
            window.TKroot.clipboard_clear()
            window.TKroot.clipboard_append(text)
            #window.TKroot.clipboard_append(text2)
        except:
            pass

    elif event == 'Paste':
        mline1.Widget.insert(sg.tk.INSERT, window.TKroot.clipboard_get())
        #mline2.Widget.insert(sg.tk.INSERT, window.TKroot.clipboard_get())

    elif event == 'Cut':
        try:
            text = mline1.Widget.selection_get()
            window.TKroot.clipboard_clear()
            window.TKroot.clipboard_append(text)
            mline1.update('')
            mline2.update('')
        except:
            pass
        
    #clear all
    
    if event == 'clear':
        window.find_element(MLINE_KEY1).Update('')            
        window.find_element(MLINE_KEY2).Update('')
        window['-OUTPUT-'].Update('')
        
        
    # taking input word and sending output
    if isinstance(values['-MLINE1-'], str):
        if str(values['-MLINE1-']).isalpha():
            word_d = input(values['-MLINE1-'])
            
            window['-MLINE2-'].update(str(word_d['meaning']) + '\n \n synonyms: '+ str(word_d['synonyms']) +
            '\n \n antonyms: '+ str(word_d['antonyms']))
        else:
            if event == 'search':
                window['-MLINE2-'].update('need word')
                 # if word is wrong
    else:
        if event == 'search':
  
                window['-MLINE2-'].update('need word') # if word is wrong


# Finish up by removing from the screen

window.close()