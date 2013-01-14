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

@lobotomizerApp.route('/make/<targetWord>')
def makeLobotomyProfileFromWord(targetWord):
	outputImage = lobotomize.createLobotomyProfileByWord("targetWord", 500)

@lobotomizerApp.route('/')
def hello_world():
	return "Lobotomizer App Page"

if __name__ == "__main__":
	lobotomizerApp.run()