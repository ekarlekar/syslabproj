import requests
from requests.exceptions import HTTPError
from gtts import gTTS
import os
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

def create_morse_string(filename):
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


def follow(thefile):
	thefile.seek(0,2)
	while True:
		line = thefile.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line

def main():
	language = 'en'
	logfile = open("output.txt","r")
	loglines = follow(logfile)
	for line in loglines:
		if(line.strip() == "lookL" or line.strip() == "lookR"):
			text, morse_string = morseToSpeech("output.txt")
			print(text)


if __name__ == '__main__': main()
