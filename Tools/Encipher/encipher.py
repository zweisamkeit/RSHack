#!/usr/bin/env python
# -*- coding: utf-8 -*-

# RSA Encipher
# Zweisamkeit - zweisamkeit.fr
# 07/05/17
# GNU GPL v3

import sys
import argparse

class Encipher(object):

  # Accueil

  def accueil(self):

    print ("\n")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\t\t      RSA Encipher       ")
    print ("\t\t       Zweisamkeit       ")
    print ("\t\t    GNU GPL v3 License   ")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n")

  def __init__(self,n,e,p):

    c = pow(p,e,n)

    print("\t[+] The ciphertext is: {}\n".format(c))
    
"""
if __name__ == "__main__" :

  self.accueil()

  parser = argparse.ArgumentParser(description='This simple program allows to encipher a message using RSA')
  parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
  parser.add_argument('-e', dest='e',type=int,help='RSA public key exponent',required=True)
  parser.add_argument('-p', dest='p',type=int,help='plaintext',required=True)

  args = parser.parse_args()

  n,e,p = args.n,args.e,args.p

  c = pow(p,e,n)

  print("\t[+] The ciphertext is: {}\n".format(c))
"""
