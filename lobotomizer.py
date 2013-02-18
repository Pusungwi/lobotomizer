#!/usr/bin/env python

# lobotomizer v0.1
# Author : Yi 'Pusungwi' Yeon Jae

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from flask import Flask
import lobotomize

lobotomizerApp = Flask(__name__)

@lobotomizerApp.route('/pic/<targetWord>')
def makeLobotomyProfileFromWord(targetWord):
	#output from PIL Image
	outputImage = lobotomize.createLobotomyProfileByWord(targetWord, 500)
	
	#DEBUG CODE
	#outputImage.save("output.png", "PNG")
	
	return 'Succeed!'

@lobotomizerApp.route('/')
def hello_world():
	return "Lobotomizer App Page"

if __name__ == "__main__":
	lobotomizerApp.run()