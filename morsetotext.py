import requests
from requests.exceptions import HTTPError
from gtts import gTTS
import os
from tkinter import *
from tkinter import ttk
from functools import partial
import time
import numpy

def morseToText(morse_string):
	'''
	Take a formatted morse string as input and returns English translation.

	Args:
		morse_string (string): String to be parsed through, contains '/'' between letters and '*' between words.

	'''
	translations = {
	'.-': 'a',
	'-...': 'b',
	'-.-.': 'c', 
	'-..': 'd', 
	'.': 'e', 
	'..-.': 'f', 
	'--.': 'g',
	'....': 'h',
	'..': 'i',
	'.---': 'j',
	'-.-': 'k',
	'.-..': 'l',
	'--': 'm',
	'-.': 'n',
	'---': 'o',
	'.--.': 'p',
	'--.-': 'q',
	'.-.': 'r',
	'...': 's', 
	'-': 't',
	'..-': 'u', 
	'...-': 'v',
	'.--': 'w', 
	'-..-': 'x', 
	'-.--': 'y',
	'--..': 'z',
	'.----': '1',
	'..---': '2',
	'...--': '3',
	'....-': '4',
	'.....': '5',
	'-....': '6',
	'--...': '7',
	'---..': '8',
	'----.': '9',
	'-----': '0',
	'*': ' ',
	'': '  '
	}
	split = morse_string.split('/')
	translation = ""
	for letter in split:
		if '*' in letter:
			sub_split = letter.split('*')
			translation+=translations[sub_split[0]]
			translation+= " "
			translation+=translations[sub_split[1]]
		else:
			translation+=translations[letter]
	print(translation)
	return translation


def textToSpeech(text_string, language): 
	'''
	Takes English text string as input and uses Google Cloud to make and play an .mp3 file speaking the input text.

	Args:
		text_string (string): String to be translated.

		language (string): Language of desired output. In theory, can support English, Hindi, Tamil, French, and German but functionality needs to be added. English should be formatted as 'en'.

	'''	
	myobj = gTTS(text=text_string, lang=language, slow=False)
	myobj.save("texttospeech.mp3")
	os.system('afplay texttospeech.mp3')

def morseToSpeech(filename):
	'''
	Takes morse list as input and prints out and speaks aloud English translation.

	Args:
		morse_list (3-layer nested list): List of words containing a sublist of letters containing a sublist of symbols (dots and dashes). To be passed into toMorseFormat.

		language (string): Language of desired output. In theory, can support English, Hindi, Tamil, French, and German but functionality needs to be added. English should be formatted as 'en'. To be passed into textToSpeech.

	'''
	morse_string = create_morse_string(filename) #toMorseFormat(morse_list)
	text = morseToText(morse_string)

	return text, morse_string
	print(text)

def display_connected(root, frm, is_connected, morse_string):
	is_connected = "   Connected    "
	ttk.Label(frm, text=is_connected).grid(column=0, row=7)
	start_button(root, frm, morse_string)

def update_label(root, to_display):
	l_r.set(to_display)

def start_button(root, frm, morse_string):
	global txt, txt2, txt3
	txt = ttk.Label(frm, text="Hello")
	txt2 = ttk.Label(frm, text="Hello2")
	txt3 = ttk.Label(frm, text="Hello3")
	txt.grid(column=1, row=17)
	txt2.grid(column=2, row=17)
	txt3.grid(column=0, row=17)
	display_blinks(root, frm, morse_string)

def display_blinks(root, frm, morse_string):
	global txt, txt2, txt3
	to_display = []
	for x in morse_string:
		if x == '.':
			to_display.append('l')
		if x == '-':
			to_display.append('r')
	count = 0
	refresher(to_display, count, root)
	print(to_display)
def refresher(to_display, count, root):
	global txt, txt2, txt3
	count+=1
	if(count >= len(to_display)):
		return
	x = to_display[count]
	if x == 'l':
		txt.configure(text="Left Blink", font='Helvetica 18 bold')
		txt2.configure(text="Right Blink", font='Helvetica 18 normal')
		txt3.configure(text="Detected Blink #" + str(count)+":", font='Helvetica 18 normal')
	elif x == 'r':
		txt.configure(text="Left Blink", font='Helvetica 18 normal')
		txt2.configure(text="Right Blink", font='Helvetica 18 bold')
		txt3.configure(text="Detected Blink #" + str(count)+":", font='Helvetica 18 normal')
	root.after(600, refresher, to_display, count, root)
	if(count >= len(to_display)):
		return

def create_morse_string(filename): # right now assuming look left is to signal between letters and look right is between words, we can change it to be for diff # of neutrals in between
	morse_string = ""
	with open(filename) as f:
		for line in f:
			expression = line.strip()
			if expression == "winkL":
				morse_string += '.'
			if expression == "winkR":
				morse_string += '-'
			if expression == "lookL":
				morse_string += '/' # slash between letters
			if expression == "lookR":
				morse_string += '*' # asterisk between words
	return morse_string

def display_translation(root, frm, text, morse_string):
	ttk.Label(frm, text=text).grid(column=0, row=11)
	ttk.Label(frm, text="Morse Code (from blinks): "+morse_string).grid(column=0, row=11)
	ttk.Label(frm, text="English Translation: "+text).grid(column=0, row=12)

def display(root, text, language, morse_string):
	logo = PhotoImage(file='logologo.png')
	logo = logo.zoom(10)
	logo = logo.subsample(30)
	translations = PhotoImage(file='translations.png')
	translations = translations.zoom(10) 
	translations = translations.subsample(30)
	play = PhotoImage(file='playbutton.png')
	is_connected = "Not Connected"
	play = play.subsample(30)
	morse_string = morse_string.replace('/', '')
	morse_string = morse_string.replace('*', ' ')
	frm = ttk.Frame(root, padding=10)
	frm.grid()
	ttk.Label(frm, image=logo).grid(column=0, row=0)
	ttk.Label(frm, image=translations).grid(column=0, row=18)
	frm1 = ttk.Frame(frm, padding=1)
	ttk.Label(frm, text=is_connected).grid(column=0, row=7)
	ttk.Label(frm, text="Wink Left = dot (.) \nWink Right = dash (-) \nLook Left = new letter \nLook Right = new word").grid(column=0, row=19)
	ttk.Button(frm, text="Play Sound", width=10, command=partial(textToSpeech, text, language)).grid(column=0, row=14)
	ttk.Button(frm, text="Quit", width=10, command=root.destroy).grid(column=0, row=15)
	ttk.Button(frm, text="Connect to EEG", command=partial(display_connected, root, frm, is_connected, morse_string)).grid(column=0, row=6)
	ttk.Button(frm, text="Stop and Translate", command=partial(display_translation, root, frm, text, morse_string)).grid(column=0, row=10)

	root.mainloop()
	return

def main():
	root = Tk()
	root.title('Blinks to Speech')
	language = 'en'
	text, morse_string = morseToSpeech("output4.txt")
	display(root, text, language, morse_string)

if __name__ == '__main__': main()
