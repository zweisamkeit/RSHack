#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from os import getcwd

import argparse

import Crypto

import sys

class Tool(object):

	def __init__(self, args):

		self.args = args

		return

	def extractor(self):

		path = getcwd() + '/Tools/Extractor'
		sys.path.append(path)
		from extractor import Extractor

		extractor = Extractor(self.args.k)

	def privkeyconstruct(self):

		path = getcwd() + '/Tools/Private_Key'
		sys.path.append(path)
		from privkey import PrivkeyConstruct

		if 'o' not in dir(self.args):

			self.args.o = None

                else:

                        self.args.o = getcwd() + "/" + self.args.o
                        print(self.args.o)


		pubkey = PrivkeyConstruct(self.args.p, self.args.q, self.args.e, self.args.o)

	def pubkeyconstruct(self):

		path = getcwd() + '/Tools/Public_Key'
		sys.path.append(path)
		from pubkey import PubkeyConstruct

		if 'o' not in dir(self.args):

			self.args.o = None

                else:

                        self.args.o = getcwd() + "/" + self.args.o

		pubkey = PubkeyConstruct(self.args.n, self.args.e, self.args.o)

	def encipher(self):

		path = getcwd() + '/Tools/Encipher'
		sys.path.append(path)
		from encipher import Encipher

		encipher = Encipher(self.args.n, self.args.e, self.args.p)

	def decipher(self):

		path = getcwd() + '/Tools/Decipher'
		sys.path.append(path)
		from decipher import Decipher

		decipher = Decipher(self.args.n, self.args.d, self.args.c)

