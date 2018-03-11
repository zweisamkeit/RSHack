#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import getcwd

import argparse

import sys

class Tool(object):

	def __init__(self, args):

		self.args = args

		return

	def pubex(self):

		path = getcwd() + '/Tools/Public_Extractor'
		sys.path.append(path)
		from pubex import Pubex

		pubex = Pubex(self.args.k)

	def privex(self):

		path = getcwd() + '/Tools/Private_Extractor'
		sys.path.append(path)
		from privex import Privex

		privex = Privex(self.args.k)


	def privkeyconstruct(self):

		path = getcwd() + '/Tools/Private_Key'
		sys.path.append(path)
		from privkey import PrivkeyConstruct

		if self.args.o is not None:

			self.args.o = getcwd() + "/" + self.args.o
			print(self.args.o)


		pubkey = PrivkeyConstruct(self.args.p, self.args.q, self.args.e, self.args.o)

	def pubkeyconstruct(self):

		path = getcwd() + '/Tools/Public_Key'
		sys.path.append(path)
		from pubkey import PubkeyConstruct
			
		if self.args.o is not None:

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

