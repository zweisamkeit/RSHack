#!/usr/bin/python3
# -*- coding: utf-8 -*-

# RSA Private Key Constructor
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
  print ("\t Private Key Constructor ")
  print ("\t       Zweisamkeit       ")
  print ("\t    GNU GPL v3 License   ")
  print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("\n")

def bezout(a, b):

    if a == 0 and b == 0:

      return (0, 0, 0)

    if b == 0:

      return (a // abs(a), 0, abs(a))

    (u, v, p) = bezout(b, a % b)

    return (v, (u - v * (a // b)), p)

def inv_modulo(x, m):

  (u, _, p) = bezout(x, m)

  return (u % abs(m))

if __name__ == "__main__" :

  accueil()

  parser = argparse.ArgumentParser(description='This program allows to construct an RSA Public Key with its parameters')

  parser.add_argument('-p', dest='p',type=int,help='first element of the modulus factorization',required=True)
  parser.add_argument('-q', dest='q',type=int,help='second element of the modulus factorization',required=True)
  parser.add_argument('-e', dest='e',type=int,help='public exponent',required=True)

  args = parser.parse_args()

  p,q,e = args.p,args.q,args.e

  n = p*q
  phi = (p-1)*(q-1)
  d = inv_modulo(e,phi)

  print("\tn,p,q,e,d={}, {}, {}, {}, {}\n".format(n,p,q,e,d))

  key = RSA.construct((n,e,d,p,q))

  print("\tPrivate key: \n\n\t\t{}\n".format(RSA._RSAobj.exportKey(key).decode('utf-8').replace('\n','\n\t\t')))

