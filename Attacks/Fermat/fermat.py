#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Attaque RSA par factorisation de Fermat
# Zweisamkeit
# 29/12/16
# Gnu/GPL v3

import sys
import math
import Crypto.PublicKey.RSA
import fractions
import random
import argparse

class Fermat(object):

    # Accueil

    def accueil(self):

      print ("\n")
      print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
      print ("\t\t      Fermat Attack      ")
      print ("\t\t       Zweisamkeit       ")
      print ("\t\t    GNU GPL v3 License   ")
      print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n")

    def carre_parfait(self, x):

      if x < 1:

        return(False)

      sqrt_x = math.sqrt(x)

      return (sqrt_x == int(math.floor(sqrt_x)))

    # Factorisation de Fermat

    def fermat(self,n):

      a = 2*math.ceil(math.sqrt(n)) + 1

      aux = 2 * a +1 # Conservation de la valeur pour l'optimisation des calculs

      n4 = 4 * n

      # On incrémente a jusqu'à ce que a² - N soit un carré parfait

      c = pow(a, 2) - n4

      while not carre_parfait(c):

        c += aux

        a += 1

        aux += 2

      b = int(math.sqrt(c))

      p = (a - b) // 2

      q = (a + b) // 2

      if (p*q != n):

        print("Error!")
        exit(0)

      return (p, q)

    # Calcul de l'indicatrice d'euler du module n = pq

    def indicatrice_euler(self, p, q):

      return((p - 1) * (q - 1))

    # Inverse modulaire

    def bezout(self, a, b):

        if a == 0 and b == 0:

          return (0, 0, 0)

        if b == 0:

          return (a // abs(a), 0, abs(a))

        (u, v, p) = self.bezout(b, a % b)

        return (v, (u - v * (a // b)), p)

    def inv_modulo(self, x, m):

      (u, _, p) = self.bezout(x, m)

      return u % abs(m)

    # Main pour RSHack

    def __init__(self, n, e):

        self.accueil()

        try:

            (p, q) = self.fermat(n, e)

        except:

            print("\n\t[-] This RSA public key isn't a valide candidate for a Fermat Attack\n")
            exit()

        print("\n\t[+] Factorization:{} * {}\n".format(p,q))

        # On calcule l'indicatrice d'Euler pour reconstruire l'exposant privé d

        phi = indicatrice_euler(p,q)

        self.d = inv_modulo(e, phi)

        print("\t[+] Private exponent: {}\n".format(d))
