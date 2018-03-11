#!/usr/bin/python3
# -*- coding: utf-8 -*-

# RSA Private Key parameters extractor
# Zweisamkeit
# 06/27/17
# GNU/GPL v3

import argparse
from Crypto.PublicKey import RSA

class Privex(object):

  # Accueil

  def accueil():

    print ("\n")
    print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\tRSA Private Key Extractor")
    print ("\t       Zweisamkeit       ")
    print ("\t    GNU GPL v3 License   ")
    print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n")

  def __init__(self, k):

    key=RSA.importKey(open(k, 'r').read())

    n,e,d,p,q = key.n, key.e, key.d, key.p, key.q

    print("\n\t[+] Modulus: {}".format(str(n)))
  
    print("\n\t[+] Public Exponent: {}".format(str(e)))
    
    print("\n\t[+] Private Exponent: {}".format(str(d)))
    
    print("\n\t[+] p factor: {}".format(str(p)))
    
    print("\n\t[+] q factor: {}".format(str(q)))
