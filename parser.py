#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import sys
from HTMLParser import HTMLParser

end = False

class Parser(HTMLParser):
	def handle_starttag(self, tag, attr):
		for a in attr:
			if(a[0] == "class"):
				if(a[1] == "span1"):
					print "Inscricao:"
				elif(a[1] == "span2"):
					print "Nome:"
				elif(a[1] == "span3"):
					print "Semestre:"
				elif(a[1] == "span4"):
					print "Curso:"

	def handle_data(self, data):
		print data

def main():
	url = sys.argv[1]
	response = urllib2.urlopen(url)
	page = response.read()
	p = Parser()
	p.feed(page)

if __name__ == "__main__":
	main()