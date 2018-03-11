#!/usr/bin/python3
# -*- coding: utf-8 -*-

# RSA Private Key Constructor
# Zweisamkeit
# 05/07/17
# GNU/GPL v3

import sys
import argparse
from Crypto.PublicKey import RSA

class PrivkeyConstruct(object):

  # Accueil

  def accueil(self):

    print ("\n")
    print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\t Private Key Constructor ")
    print ("\t       Zweisamkeit       ")
    print ("\t    GNU GPL v3 License   ")
    print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n")

  def bezout(self, a, b):

      if a == 0 and b == 0:

        return (0, 0, 0)

      if b == 0:

        return (a // abs(a), 0, abs(a))

      (u, v, p) = self.bezout(b, a % b)

      return (v, (u - v * (a // b)), p)

  def inv_modulo(self, x, m):

    (u, _, p) = self.bezout(x, m)

    return (u % abs(m))

  def __init__(self, p, q, e, o):

    n = p*q
    phi = (p-1)*(q-1)
    d = self.inv_modulo(e,phi)

    print("\n\tRSA Private Key Paramaters: n, p, q, e, d = {}, {}, {}, {}, {}\n".format(n,p,q,e,d))

    key = RSA.construct((n,e,d,p,q))

    key = RSA._RSAobj.exportKey(key).decode('utf-8')

    print("\tPrivate key: \n\n\t\t{}\n".format(key.replace('\n','\n\t\t')))

    if o is not None:

      out = open(o,'w+')

      out.write(key)

      out.close()

      print("\tThe key has been saved in {}\n".format(o))
