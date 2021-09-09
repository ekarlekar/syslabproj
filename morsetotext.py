import requests
from requests.exceptions import HTTPError
from gtts import gTTS
import os

def toMorseFormat(morse_list):
	'''
	Take a morse list as input and returns a string able to be parsed through by a morse-to-text API.

	Args:
		morse_list (3-layer nested list): List of words containing a sublist of letters containing a sublist of symbols (dots and dashes).

	'''
	morse_string = ""
	for word in morse_list:
		for letter in word:
			sing_letter = ''
			for symbol in letter:
				sing_letter += symbol
			morse_string += sing_letter
			morse_string+= "%20" # space between letters
		morse_string+= "%20%20" # space between words

	print(morse_string)
	return morse_string

def morseToText(morse_string):
	'''
	Take a formatted morse string as input and returns English translation using morsecode-api.de.

	Args:
		morse_string (string): String to be parsed through, contains one space between letters and two spaces between words.

	'''
	url = 'http://www.morsecode-api.de/decode?string=' + morse_string
	r = requests.get(url)
	r.raise_for_status()
	j = r.json()
	return j.get('plaintext')

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

def morseToSpeech(morse_list, language):
	'''
	Takes morse list as input and prints out and speaks aloud English translation.

	Args:
		morse_list (3-layer nested list): List of words containing a sublist of letters containing a sublist of symbols (dots and dashes). To be passed into toMorseFormat.

		language (string): Language of desired output. In theory, can support English, Hindi, Tamil, French, and German but functionality needs to be added. English should be formatted as 'en'. To be passed into textToSpeech.

	'''
	morse_string = toMorseFormat(morse_list)
	text = morseToText(morse_string)
	textToSpeech(text, 'en')
	print(text)

def main():

	morse_list = [[['.','.','.','.'], ['.'], ['.', '-', '.', '.'], ['.', '-', '.', '.'], ['-','-','-']],[['.', '-', '-'], ['-','-','-'], ['.','-','.'], ['.','-','.','.'], ['-','.','.']]] # hello world
	language = 'en'
	morseToSpeech(morse_list, language)

if __name__ == '__main__': main()
