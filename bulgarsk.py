#!/usr/bin/python
# -*- coding: utf-8  -*-
import pyperclip
import time
import string

bulgarsk = {
	u"а": "a",
	u"б": "b",
	u"в": "v",
	u"г": "g",
	u"д": "d",
	u"е": "e",
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
	u"щ": "sjt",
	u"ъ": "ă",
	u"ь": ["j", "i"],
	u"ю": ["ju", "iu"],
	u"я": ["ja", "ia"],
	u" ": " ",
	u"-": "-"
}

#innputt = raw_input("Bulgarsk ord: ").decode('utf-8').lower()

def transkripsjon(bulgarskord):
	norsk = ""
	for bokstav in bulgarskord:
		if isinstance(bulgarsk[bokstav], list):
			if (" " + norsk)[-1] in "sz":
				norsk += bulgarsk[bokstav][1]
			else:
				norsk += bulgarsk[bokstav][0]
		else:
			norsk += bulgarsk[bokstav]
	pyperclip.copy(string.capwords(norsk))
	print "Klar for innliming: " + string.capwords(norsk)

while True:
	try:
		transkripsjon(pyperclip.paste().decode('utf-8').lower())
	except KeyError:
		time.sleep(0.1)
