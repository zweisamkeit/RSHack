#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import getcwd

import argparse

import Crypto

import sys

class Attack(object):

	def __init__(self, args):

		self.args = args

		return

	def wiener(self):

		path = getcwd() + '/Attacks/Wiener'
		sys.path.append(path)
		from wiener import Wiener

		wiener = Wiener(self.args.n, self.args.e)

		d = wiener.d

	def hastad(self):

		path = getcwd() + '/Attacks/Hastad'
		sys.path.append(path)
		from hastad import Hastad

		hastad = Hastad(self.args.k0, self.args.k1, self.args.k2, self.args.c0, self.args.c1, self.args.c2)

	def fermat(self):

		path = getcwd() + '/Attacks/Fermat'
		sys.path.append(path)
		from fermat import Fermat
		fermat = Fermat(self.args.n, self.args.e)
		d = fermat.d

	def bleichenbacher(self):

		path = getcwd() + '/Attacks/Bleichenbacher'
		sys.path.append(path)
		from bleichenbacher import Bleichenbacher
		bleich = Bleichenbacher(self.args.n, self.args.e, self.args.c, self.args.host, self.args.port, self.args.error)

	def comod(self):

		path = getcwd() + '/Attacks/Common_Modulus'
		sys.path.append(path)
		from comod import Comod
		comod = Comod(self.args.n, self.args.e1, self.args.e2, self.args.c1, self.args.c2)

	def chopla(self):

		path = getcwd() + '/Attacks/Chosen_Plaintext'
		sys.path.append(path)
		from chopla import Chopla
		chopla = Chopla(self.args.n, self.args.e, self.args.c)
