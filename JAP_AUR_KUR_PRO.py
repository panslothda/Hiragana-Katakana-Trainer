#!/usr/bin/env python3


Hiragana_English = {
     	'a': 'あ',
     	'i': 'い',
     	'u': 'う',
     	'e': 'え',
     	'o': 'お'
    	 }

print('If you want to translate from Hiragana to English enter 1 and if you want to translate English to Hiragana enter 2')
exercise = int(input(':'))
print(exercise)
if exercise == 1:	
	print('Type the translation of the Hiragana in English and press Enter to see if you were right')
	for key, value in Hiragana_English.items():
		go_on = 0
		while go_on == 0 :
			print('What is ' + value + ' ?')
			answer = input(':')
			if key == answer:
				print('Congratulations !')
				go_on = 1
			else: 
				print('Try again ^_^')
				go_on = 0

elif exercise == 2:
	print('Type the translation from the English word in Hiragana and press Enter to see if you were right')
	for key, value in Hiragana_English.items():
		go_on = 0
		while go_on == 0 :
			print('What is ' + key + ' ?')
			answer = input(':')
			if value == answer:
				print('Congratulations !')
				go_on = 1
			else: 
				print('Try again ^_^')
				go_on = 0
