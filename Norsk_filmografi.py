#!/usr/bin/python
# -*- coding: utf-8  -*-
import urllib2
import re

nfid = 1757221
while nfid < 2000000:
	try:
		sideinnhold = urllib2.urlopen("http://www.nb.no/filmografi/show?id=" + str(nfid)).read()
		with open("data/nfid.txt", "a") as minfil:
			minfil.write("# {{/fmt|" + str(nfid) + "}}\n")
		print "ID-en " + str(nfid) + " EKSISTERER!!!!!"
	except urllib2.HTTPError:
		print "ID-en " + str(nfid) + " eksisterer ikke"
	nfid += 1
