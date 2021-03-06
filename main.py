#!/usr/bin/env python3


hiragana_english = {'あ':'a','い':'i','う':'u','え':'e','お':'o','か':'ka','き':'ki','く':'ku','け':'ke','こ':'ko','きゃ':'kya','きゅ':'kyu','きょ':'kyo','さ':'sa','し':'shi','す':'su','せ':'se','そ':'so','しゃ':'sha','しゅ':'shu','しょ':'sho','た':'ta','ち':'chi','つ':'tsu','て':'te','と':'to','ちゃ':'cha','ちゅ':'chu','ちょ':'cho','な':'na','に':'ni','ぬ':'nu','ね':'ne','の':'no','にゃ':'nya','にゅ':'nyu','にょ':'nyo','は':'ha','ひ':'hi','ふ':'fu','へ':'he','ほ':'ho','ひゃ':'hya','ひゅ':'hyu','ひょ':'hyo','ま':'ma','み':'mi','む':'mu','め':'me','も':'mo','みゃ':'mya','みゅ':'myu','みょ':'myo','や':'ya','ゆ':'yu','よ':'yo','ら':'ra','り':'ri','る':'ru','れ':'re','ろ':'ro','りゃ':'rya','りゅ':'ryu','りょ':'ryo','わ':'wa','ゐ':'i/wi','ゑ':'e/we','を':'o/wo','が':'ga','ぎ':'gi','ぐ':'gu','げ':'ge','ご':'go','ぎゃ':'gya','ぎゅ':'gyu','ぎょ':'gyo','ざ':'za','じ':'ji','ず':'zu','ぜ':'ze','ぞ':'zo','じゃ':'ja','じゅ':'ju','じょ':'jo','だ':'da','ぢ':'ji','づ':'zu','で':'de','ど':'do','ぢゃ':'ja','ぢゅ':'ju','ぢょ':'jo','ば':'ba','び':'bi','ぶ':'bu','べ':'be','ぼ':'bo','びゃ':'bya','びゅ':'byu','びょ':'byo','ぱ':'pa','ぴ':'pi','ぷ':'pu','ぺ':'pe','ぽ':'po','ぴゃ':'pya','ぴゅ':'pyu','ぴょ':'pyo','ゔ':'vu/u'}

katakana_english = {'ア':'a','イ':'i','ウ':'u','エ':'e','オ':'o','カ':'ka','キ':'ki','ク':'ku','ケ':'ke','コ':'ko','キャ':'kya','キュ':'kyu','キョ':'kyo','サ':'sa','シ':'shi','ス':'su','セ':'se','ソ':'so','シャ':'sha','シュ':'shu','ショ':'sho','タ':'ta','チ':'chi','ツ':'tsu','テ':'te','ト':'to','チャ':'cha','チュ':'chu','チョ':'cho','ナ':'na','ニ':'ni','ヌ':'nu','ネ':'ne','ノ':'no','ニャ':'nya','ニュ':'nyu','ニョ':'nyo','ハ':'ha','ヒ':'hi','フ':'fu','ヘ':'he','ホ':'ho','ヒャ':'hya','ヒュ':'hyu','ヒョ':'hyo','マ':'ma','ミ':'mi','ム':'mu','メ':'me','モ':'mo','ミャ':'mya','ミュ':'myu','ミョ':'myo','ヤ':'ya','ユ':'yu','ヨ':'yo','ラ':'ra','リ':'ri','ル':'ru','レ':'re','ロ':'ro','リャ':'rya','リュ':'ryu','リョ':'ryo','ワ':'wa','ヰ':'wi','ヱ':'we','ヲ':'wo','ガ':'ga','ギ':'gi','グ':'gu','ゲ':'ge','ゴ':'go','ギャ':'gya','ギュ':'gyu','ギョ':'gyo','ザ':'za','ジ':'ji','ズ':'zu','ゼ':'ze','ゾ':'zo','ジャ':'ja','ジュ':'ju','ジョ':'jo','ダ':'da','ヂ':'ji','ヅ':'zu','デ':'de','ド':'do','ヂャ':'ja','ヂュ':'ju','ヂョ':'jo','バ':'ba','ビ':'bi','ブ':'bu','ベ':'be','ボ':'bo','ビャ':'bya','ビュ':'byu','ビョ':'byo','パ':'pa','ピ':'pi','プ':'pu','ペ':'pe','ポ':'po','ピャ':'pya','ピュ':'pyu','ピョ':'pyo',}

def hiragana_training_hira_2_eng():
		print(' Type the translation of the Hiragana in English and press Enter to see if you were right')
		for key, value in hiragana_english.items():
			go_on = 0
			while go_on == 0 :
				print(' What is ' + value + ' ?')
				answer = input(':')
				if key == answer:
					print(' Congratulations !')
					go_on = 1
				else: 
					print(' Try again ^_^')
					go_on = 0

def hiragana_training_eng_2_hira():
	print(' Type the translation from the English word in Hiragana and press Enter to see if you were right')
	for key, value in hiragana_english.items():
		go_on = 0
		while go_on == 0 :
			print(' What is ' + key + ' ?')
			answer = input(':')
			if value == answer:
				print(' Congratulations !')
				go_on = 1
			else: 
				print(' Try again ^_^')
				go_on = 0

def katakana_training_kata_2_eng():
		print(' Type the translation of the Katakana in English and press Enter to see if you were right')
		for key, value in katakana_english.items():
			go_on = 0
			while go_on == 0 :
				print(' What is ' + value + ' ?')
				answer = input(':')
				if key == answer:
					print(' Congratulations !')
					go_on = 1
				else: 
					print(' Try again ^_^')
					go_on = 0

def katakana_training_eng_2_kata():
	print(' Type the translation from the English word in Katakana and press Enter to see if you were right')
	for key, value in katakana_english.items():
		go_on = 0
		while go_on == 0 :
			print(' What is ' + key + ' ?')
			answer = input(':')
			if value == answer:
				print(' Congratulations !')
				go_on = 1
			else: 
				print(' Try again ^_^')
				go_on = 0



if __name__ == '__main__':
	print('\n Choose what you want to train:')
	print('\n 1. Hiragana')
	print(' 2. Katakana\n')
	exercise = int(input(':'))
	if exercise == 1:
		print('\n Choose what you want to train:')
		print('\n 1. Hiragana to English')
		print(' 2. English to Hiragana\n')
	exercise_2 = int(input(':'))
	if exercise_2 == 1:
		hiragana_training_hira_2_eng() 
	if exercise_2 == 2:
		hiragana_training_eng_2_hira()

	if exercise == 2:
		print('\n Choose what you want to train:')
		print('\n 1. Katakana to English')
		print(' 2. English to Katakana\n')
	exercise_3 = int(input(':'))
	if exercise_3 == 1:
		katakana_training_kata_2_eng() 
	if exercise_3 == 2:
		katakana_training_eng_2_kata()

