#!/usr/bin/python
# -*- coding: utf-8  -*-
import pyperclip
import time
import string

russisk = {
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

#innputt = raw_input("Russisk ord: ").decode('utf-8').lower()

def transkripsjon(russiskord):
	norsk = ""
	russ = ""
	for bokstav in russiskord:
		russ += bokstav
		if isinstance(russisk[bokstav], list):
			if bokstav == u"е":
				if (" " + russ)[-2] in u" ьъ":
					if (" " + norsk)[-1] in "sz":
						norsk += russisk[bokstav][1]
					else:
						norsk += russisk[bokstav][0]
				elif (" " + norsk)[-1] in "aeiouy":
					norsk += russisk[bokstav][0]
				else:
					norsk += russisk[bokstav][2]
			elif (" " + norsk)[-1] == "j":
				norsk += russisk[bokstav][2]
			elif (" " + norsk)[-1] in "sz":
				norsk += russisk[bokstav][1]
			else:
				norsk += russisk[bokstav][0]
		else:
			norsk += russisk[bokstav]
	resultat = string.capwords(norsk)
	if not string.find(resultat, ",") == -1:
		resultat = resultat[string.find(resultat, ",")+2:] + " " + resultat[:string.find(resultat, ",")]
	pyperclip.copy(resultat)
	print "Klar for innliming: " + resultat

while True:
	try:
		transkripsjon(pyperclip.paste().decode('utf-8').lower())
	except KeyError:
		time.sleep(0.1)
