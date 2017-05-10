#!/usr/bin/python3
# -*- coding: utf-8 -*-

# RSA Public Key Constructor
# Zweisamkeit
# 05/07/17
# GNU/GPL v3

import sys
import argparse
from Crypto.PublicKey import RSA

# Accueil

def accueil():

  print ("\n")
  print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("\t  Public Key Constructor ")
  print ("\t       Zweisamkeit       ")
  print ("\t    GNU GPL v3 License   ")
  print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("\n")

if __name__ == "__main__" :

  accueil()

  parser = argparse.ArgumentParser(description='This program allows to construct an RSA Public Key with its parameters')

  parser.add_argument('-n', dest='n',type=int,help='modulus',required=True)
  parser.add_argument('-e', dest='e',type=int,help='public exponent',required=True)

  args = parser.parse_args()

  n,e = args.n,args.e

  rsaobj = RSA.construct((n,e))

  key = rsaobj.exportKey()

  print("The corresponding RSA public key is : \n\n\t\t{}\n".format(key.decode('utf-8').replace('\n','\n\t\t')))

