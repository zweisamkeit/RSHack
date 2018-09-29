#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Hastad Attack
# Zweisamkeit
# 05/07/17
# GNU/GPL v3

import sys
from Crypto.PublicKey import RSA
import gmpy2
import codecs

class Hastad(object):

  # Accueil

  def accueil(self):

    print ("\n")
    print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\t      Hastad Attack      ")
    print ("\t       Zweisamkeit       ")
    print ("\t    GNU GPL v3 License   ")
    print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n")


  sys.setrecursionlimit(1000000)

  def xgcd(self, a, b):
    if a == 0:
      return (b, 0, 1)
    else:
      gcd, u, v = self.xgcd(b % a, a)
      return (gcd, v - (b // a) * u, u)

  def root(self, a, e):
  	return (gmpy2.iroot(a,e))

  def __init__(self, n0, n1, n2, e, c0, c1, c2):

    self.accueil()

    print("\n\t[+] Modular inverse calculation...")

    b0,b1,b2 = self.xgcd(n0,n1*n2)[2], self.xgcd(n1,n0*n2)[2], self.xgcd(n2,n0*n1)[2]

    print("\t[+] Modular inverse calculation done...")

    print("\n\t[+] System solution cube calculation...")

    m=(b0 * c0 * n1 * n2) + (b1 * c1 * n0 * n2) + (b2 * c2 * n0 * n1)
    m %= (n0 * n1 * n2)

    print("\t[+] System solution cube calculation done")

    print("\n\t[+] System solution calculation...")

    x = self.root(m,e)[0]

    print("\t[+] System solution calculation done")

    print("\n\t[+] Solution interpretation...")

    p = codecs.decode(hex(x)[2:].replace('L',''),"hex_codec").decode('utf-8')

    print("\t[+] Solution interpretation done")

    print("\n\t\t[+] The plaintext is: {}".format(p.replace('\n','\n\t\t')))
