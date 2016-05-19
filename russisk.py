#!/usr/bin/python
# -*- coding: utf-8  -*-
import pyperclip
import time
import string
import re
import os

ru_no = {
	u"а": "a",
	u"б": "b",
	u"в": "v",
	u"г": "g",
	u"д": "d",
	u"е": ["je", "ie", "e"], # "e" vanligvis, "je" først i ord eller etter vokal, Ь eller Ъ, "ie" etter transkripsjon som slutter på "s" eller "z"
	u"ё": ["jo", "io", "o"], # "jo" vanligvis, "io" etter "s" og "z", "o" etter "j"
	u"ж": "zj",
	u"з": "z",
	u"и": "i",
	u"й": "j",
	u"к": "k",
	u"л": "l",
	u"м": "m",
	u"н": "n",
	u"о": "o",
	u"п": "p",
	u"р": "r",
	u"с": "s",
	u"т": "t",
	u"у": "u",
	u"ф": "f",
	u"х": "kh",
	u"ц": "ts",
	u"ч": "tsj",
	u"ш": "sj",
	u"щ": "sjtsj",
	u"ъ": "",
	u"ы": "y",
	u"ь": "",
	u"э": "e",
	u"ю": ["ju", "iu", "u"], # "ju" vanligvis, "iu" etter "s" og "z", "u" etter "j"
	u"я": ["ja", "ia", "a"], # "ja" vanligvis, "ia" etter "s" og "z", "a" etter "j"
	u" ": " ",
	u"-": "-",
	u",": ",",
}
ru_en = {
	u"а": "a",
	u"б": "b",
	u"в": "v",
	u"г": "g",
	u"д": "d",
	u"е": ["ye", "e"], # "e" vanligvis, "ye" først i ord eller etter vokal, Ь eller Ъ
	u"ё": ["yo", "o"], # "yo" vanligvis, "o" etter y
	u"ж": "zh",
	u"з": "z",
	u"и": "i",
	u"й": "y",
	u"к": "k",
	u"л": "l",
	u"м": "m",
	u"н": "n",
	u"о": "o",
	u"п": "p",
	u"р": "r",
	u"с": "s",
	u"т": "t",
	u"у": "u",
	u"ф": "f",
	u"х": "kh",
	u"ц": "ts",
	u"ч": "ch",
	u"ш": "sh",
	u"щ": "shch",
	u"ъ": "",
	u"ы": "y",
	u"ь": "",
	u"э": "e",
	u"ю": ["yu", "u"], # "yu" vanligvis, "u" etter y
	u"я": ["ya", "a"], # "ya" vanligvis, "a" etter y
	u" ": " ",
	u"-": "-",
	u",": ",",
}

def kommafiks(navn):
	if string.find(navn, ",") != -1:
		return navn[string.find(navn, ",")+2:] + " " + navn[:string.find(navn, ",")]
	else:
		return navn

def nortrans(russiskord):
	nor = ""
	rus = ""
	for bokstav in russiskord:
		rus += bokstav
		if isinstance(ru_no[bokstav], list):
			if bokstav == u"е":
				if (" " + rus)[-2] in u" ьъ":
					if (" " + nor)[-1] in "sz":
						nor += ru_no[bokstav][1]
					else:
						nor += ru_no[bokstav][0]
				elif (" " + nor)[-1] in "aeiouy":
					nor += ru_no[bokstav][0]
				else:
					nor += ru_no[bokstav][2]
			elif (" " + nor)[-1] == "j":
				nor += ru_no[bokstav][2]
			elif (" " + nor)[-1] in "sz":
				nor += ru_no[bokstav][1]
			else:
				nor += ru_no[bokstav][0]
		else:
			nor += ru_no[bokstav]
	nor = string.capwords(nor)
	nor = kommafiks(nor)
	pyperclip.copy(nor)
	print "Klar for innliming (norsk): " + nor

def engtrans(russiskord):
	orig = re.sub(u"[иы]й(\\s|\\-|$)", u"й\\1", kommafiks(russiskord))
	eng = ""
	rus = ""
	for bokstav in orig:
		rus += bokstav
		if isinstance(ru_en[bokstav], list):
			if bokstav == u"е":
				if ((" " + rus)[-2] in u" ьъ") or ((" " + eng)[-1] in "aeiouy"):
					eng += ru_en[bokstav][0]
				else:
					eng += ru_en[bokstav][1]
			elif (" " + eng)[-1] == "y":
				eng += ru_en[bokstav][1]
			else:
				eng += ru_en[bokstav][0]
		else:
			eng += ru_en[bokstav]
	eng = string.capwords(eng)
	pyperclip.copy(eng)
	print "Klar for innliming (engelsk): " + eng
	os.system('paplay /usr/share/sounds/ubuntu/notifications/Blip.ogg')

def motor():
	orig = ""
	while True:
		liminn = pyperclip.paste().decode('utf-8').lower()
		if orig == liminn:
			try:
				engtrans(liminn)
			except KeyError:
				time.sleep(0.1)
		else:
			try:
				nortrans(liminn)
			except KeyError:
				time.sleep(0.1)
		if re.search("[aeiouy]", liminn):
			time.sleep(0.1)
		else:
			orig = liminn

motor()
