#!/usr/bin/python3
# -*- coding: utf-8 -*-

# RSA Public Key parameters extractor
# Zweisamkeit
# 05/07/17
# GNU/GPL v3

import argparse
from Crypto.PublicKey import RSA

class Pubex(object):

  # Accueil

  def accueil():

    print ("\n")
    print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\t RSA Public Key Extractor")
    print ("\t       Zweisamkeit       ")
    print ("\t    GNU GPL v3 License   ")
    print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n")

  def __init__(self, k):

    key=RSA.importKey(open(k, 'r').read())

    n,e = key.n, key.e

    print("\n\t[+] Modulus: {}".format(str(n)))
  
    print("\n\t[+] Exponent: {}".format(str(e)))
