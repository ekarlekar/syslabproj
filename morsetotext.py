import requests
from requests.exceptions import HTTPError
from gtts import gTTS
from playsound import playsound
def morseToText(morse_string):

	url = 'http://www.morsecode-api.de/decode?string=' + morse_string
	r = requests.get(url)
	r.raise_for_status()
	j = r.json()
	return j.get('plaintext')


'''morse_list format:
   [[letter, letter, letter, etc.], [letter, letter, letter, etc.], ...]]'''
def toMorseFormat(morse_list):
	
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

def textToSpeech(text_string, language): # can support English, Hindi, Tamil, French, and German 
	myobj = gTTS(text=text_string, lang=language, slow=False)
	myobj.save("texttospeech.mp3")
	#playsound("texttospeech.mp3")

morse_list = [[['.','.','.','.'], ['.'], ['.', '-', '.', '.'], ['.', '-', '.', '.'], ['-','-','-']],[['.', '-', '-'], ['-','-','-'], ['.','-','.'], ['.','-','.','.'], ['-','.','.']]] # hello world

morse_string = toMorseFormat(morse_list)

text = morseToText(morse_string)

textToSpeech(text, 'en')

print(text)
