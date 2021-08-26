import requests
from requests.exceptions import HTTPError


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
			morse_string+= letter
			morse_string+= "%20" # space between letters
		morse_string+= "%20%20" # space between words

	print(morse_string)
	return morse_string

morse_list = [["....", ".", ".-..", ".-..", "---"],[".--", "---", ".-.", ".-..", "-.."]] # hello world

morse_string = toMorseFormat(morse_list)

text = morseToText(morse_string)

print(text)