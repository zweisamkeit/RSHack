#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# Hastad Attack
# Zweisamkeit
# 05/07/17
# GNU/GPL v3

import sys
import argparse
from Crypto.PublicKey import RSA
import gmpy2

# Accueil

def accueil():

  print ("\n")
  print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("\t      Hastad Attack      ")
  print ("\t       Zweisamkeit       ")
  print ("\t    GNU GPL v3 License   ")
  print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("\n")


sys.setrecursionlimit(1000000)

def xgcd(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    gcd, u, v = xgcd(b % a, a)
    return (gcd, v - (b // a) * u, u)

def root(a,e):
	return (gmpy2.iroot(a,e))

if __name__ == "__main__" :

  accueil()

  parser = argparse.ArgumentParser(description='This program allows to carry out an Hastad Attack')
  parser.add_argument('-k0', dest='k0',type=str,help='path of the first RSA public key',required=True)
  parser.add_argument('-k1', dest='k1',type=str,help='path of the second RSA public key',required=True)
  parser.add_argument('-k2', dest='k2',type=str,help='path of the third RSA public key',required=True)
  parser.add_argument('-c0', dest='c0',type=int,help='first ciphertext (decimal)',required=True)
  parser.add_argument('-c1', dest='c1',type=int,help='second ciphertext (decimal)',required=True)
  parser.add_argument('-c2', dest='c2',type=int,help='third ciphertext (decimal)',required=True)

  args = parser.parse_args()

  k0,k1,k2,c0,c1,c2 = args.k0,args.k1,args.k2,args.c0,args.c1,args.c2

  print("\n\tKeys paramters extraction...")

  key0=RSA.importKey(open(k0, 'r'))
  key1=RSA.importKey(open(k1, 'r'))
  key2=RSA.importKey(open(k2, 'r'))

  n0, n1, n2 = key0.n, key1.n, key2.n

  e = key0.e

  print("\n\tModular inverse calculation...")

  b0,b1,b2 = xgcd(n0,n1*n2)[2], xgcd(n1,n0*n2)[2], xgcd(n2,n0*n1)[2]

  print("\tModular inverse calculation done...")

  print("\n\tSystem solution cube calculation...")

  m=(b0 * c0 * n1 * n2) + (b1 * c1 * n0 * n2) + (b2 * c2 * n0 * n1)
  m %= (n0 * n1 * n2)

  print("\tSystem solution cube calculation done")

  print("\n\tSystem solution calculation...")

  x = root(m,e)[0]

  print("\tSystem solution calculation done")

  print("\n\tSolution interpretation...")

  p = hex(x)[2:].replace('L','').decode('hex')

  print("\tSolution interpretation done")

  print("\n\t\tThe plaintext is: "+p.replace('\n','\n\t\t'))
