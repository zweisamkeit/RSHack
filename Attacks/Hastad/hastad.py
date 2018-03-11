#!/usr/bin/env python
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

  def __init__(self, k0, k1, k2, c0, c1, c2):

    self.accueil()

    print("\n\t[+] Keys paramters extraction...")

    key0=RSA.importKey(open(k0, 'r').read())
    key1=RSA.importKey(open(k1, 'r').read())
    key2=RSA.importKey(open(k2, 'r').read())

    n0, n1, n2 = key0.n, key1.n, key2.n

    if (key0.e != key1.e or key0.e != key2.e or key1.e != key2.e):

      print("\n\t[+] These keys are not good candidates for this attack")

    e = key0.e

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
