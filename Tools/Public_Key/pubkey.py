#!/usr/bin/env python
# -*- coding: utf-8 -*-

# RSA Public Key Constructor
# Zweisamkeit
# 05/07/17
# GNU/GPL v3

import sys
import argparse
from Crypto.PublicKey import RSA

class PubkeyConstruct(object):

  # Accueil

  def accueil():

    print ("\n")
    print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\t  Public Key Constructor ")
    print ("\t       Zweisamkeit       ")
    print ("\t    GNU GPL v3 License   ")
    print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n")

  def __init__(self, n, e, o):

    rsaobj = RSA.construct((n,e))

    key = rsaobj.exportKey().decode('utf-8')

    print("\tThe corresponding RSA public key is : \n\n\t\t{}\n".format(key.replace('\n','\n\t\t')))

    print(o)

    if o is not None: 

      out = open(o,'w+')

      out.write(key)

      out.close()

      print("\tThe key has been saved in {}\n".format(o))

"""
if __name__ == "__main__" :

  accueil()

  parser = argparse.ArgumentParser(description='This program allows to construct an RSA Public Key with its parameters')

  parser.add_argument('-n', dest='n',type=int,help='modulus',required=True)
  parser.add_argument('-e', dest='e',type=int,help='public exponent',required=True)
  parser.add_argument('-o',dest='o',type=str,help='output file')

  args = parser.parse_args()

  n,e,output = args.n,args.e,args.o

  rsaobj = RSA.construct((n,e))

  key = rsaobj.exportKey().decode('utf-8')

  print("\tThe corresponding RSA public key is : \n\n\t\t{}\n".format(key.replace('\n','\n\t\t')))

  if output is not None:

    out = open(output,'w+')

    out.write(key)

    out.close()

    print("\tThe key has been saved in {}\n".format(output))
"""
