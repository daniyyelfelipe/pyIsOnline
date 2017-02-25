#!/usr/bin/python
#coding: utf-8

import httplib
import time


def check_andress(web_andress):
	# web_andress = raw_input("Type the web andress: ")

	conn = httplib.HTTPConnection(web_andress)
	conn.request("HEAD", "/")
	r1 = conn.getresponse()

	if r1.status == 200:
		if r1.reason == "OK":
			print time.strftime('%X %x %Z') + " --- The web andress is online!"
			raw_input()
	elif r1.status == 302:
		if r1.reason == "Found":
			print time.strftime('%X %x %Z') + " --- The web andress is online!"
			raw_input()

	else:
		print time.strftime('%X %x %Z') + " --- " + str(r1.status) + " " + str(r1.reason)
		raw_input()

def main():
	try:
		web_andress = ""
		while web_andress == "":
			web_andress = raw_input("Type the web andress: ")
			check_andress(web_andress)
			web_andress = ""	

	except Exception, e:
		print time.strftime('%X %x %Z') + " --- " + str(e)
		raw_input()
		main()


main()