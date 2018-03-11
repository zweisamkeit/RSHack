#!/usr/bin/python3
# -*- coding: utf-8 -*-

# RSA Common Modulus Attack
# Zweisamkeit - zweisamkeit.fr
# 03/05/17
# GNU GPL v3

from sys import setrecursionlimit
import codecs

class Comod(object):

    # Accueil

    def accueil(self):

      print ("\n")
      print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
      print ("\t\t  Common Modulus Attack  ")
      print ("\t\t       Zweisamkeit       ")
      print ("\t\t    GNU GPL v3 License   ")
      print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
      print ("\n")

    # Extended gdc

    setrecursionlimit(1000000)

    def xgcd(self, a, b):
      if a == 0:
        return (b, 0, 1)
      else:
        gcd, u, v = self.xgcd(b % a, a)
        return (gcd, v - (b // a) * u, u)

    def modinv(self, a, n):
      g, x, y = self.xgcd(a, n)
      return x % n

    def pow_mod(self, a, b, n):
      number = 1
      while b:
        if b & 1:
          number = number * a % n
        b >>= 1
        a = a * a % n
      return number

    def __init__(self, n, e1, e2, c1, c2):

      self.accueil()

      # Calcul des coefficients de Bachet Bézout

      egcd = self.xgcd(e1, e2)
      u, v = egcd[1], egcd[2]

      # Calcul du plaintext

      if u >= 0:

        p1 = self.pow_mod(c1,u,n)

      else:

        p1 = self.modinv(self.pow_mod(c1,-u,n),n)

      if v >= 0:

        p2 = self.pow_mod(c2,v,n)

      else:

        p2 = self.modinv(self.pow_mod(c2,(-v),n),n)

      res = (p1 * p2) % n

      # Affichage du résultat

      print ("\t[+] Decimal plaintext: ",res,"\n")

      try:

        plaintext = codecs.decode(hex(res)[2:].replace('L',''), "hex_codec").decode('utf-8')

        print ("\t[+] Interpreted plaintext: ",plaintext,"\n")

      except:

        print("\t[-] The plaintext isn't interpretable\n")
