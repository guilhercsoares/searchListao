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
					print "},"
					print "{"
					sys.stdout.write("\"inscricao\": ")
				elif(a[1] == "span2"):
					sys.stdout.write("\"nome\": ")
				elif(a[1] == "span3"):
					sys.stdout.write("\"semestre\": ")
				elif(a[1] == "span4"):
					sys.stdout.write("\"curso\": ")

	def handle_data(self, data):
		if(data != '*' and data != "Há outro candidato com nome idêntico. Confirme pelo número de inscrição."):
			sys.stdout.write("\"")
			sys.stdout.write(data)
			print("\",")

def main():
	url = sys.argv[1]
	response = urllib2.urlopen(url)
	page = response.read()
	p = Parser()
	print "["
	p.feed(page)
	print "}"
	print "]"

if __name__ == "__main__":
	main()
