#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# RSA extractor
# Zweisamkeit
# 05/07/17
# GNU/GPL v3

import argparse
from Crypto.PublicKey import RSA

# Accueil

def accueil():

  print ("\n")
  print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("\t      RSA Extractor      ")
  print ("\t       Zweisamkeit       ")
  print ("\t    GNU GPL v3 License   ")
  print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("\n")

if __name__ == "__main__" :

  accueil()

  parser = argparse.ArgumentParser(description='This program allows to extract the modulus and the exponent of an RSA public key')

  parser.add_argument('-k', dest='k',type=str,help='path of the RSA public key',required=True)

  args = parser.parse_args()

  k=args.k

  key=RSA.importKey(open(k, 'r'))

  n,e = key.n, key.e

  print("\n\tModulus: "+str(n))
  
  print("\n\tExponent: "+str(e))
