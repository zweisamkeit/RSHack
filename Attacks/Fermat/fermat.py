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

# Accueil

def accueil():

  print ("\n")
  print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("\t\t      Fermat Attack      ")
  print ("\t\t       Zweisamkeit       ")
  print ("\t\t    GNU GPL v3 License   ")
  print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("\n")

def carre_parfait(x):

  if x < 1:
 
    return(False)

  sqrt_x = math.sqrt(x)

  return (sqrt_x == int(math.floor(sqrt_x)))

# Factorisation de Fermat

def fermat(n):

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

def indicatrice_euler(p, q):

  return((p - 1) * (q - 1))

# Inverse modulaire 

def bezout(a, b):

    if a == 0 and b == 0:

      return (0, 0, 0)

    if b == 0:

      return (a // abs(a), 0, abs(a))

    (u, v, p) = bezout(b, a % b)

    return (v, (u - v * (a // b)), p)
 
def inv_modulo(x, m):

  (u, _, p) = bezout(x, m)

  return u % abs(m)

# Main

if __name__ == "__main__" :

  accueil()

  parser = argparse.ArgumentParser(description='This program allows to carry out a Fermat Factorization')
  parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
  parser.add_argument('-e', dest='e',type=int,help='RSA public key exponent',required=True)

  args = parser.parse_args()

  # On détermine la factorisation du module n

  (p, q) = fermat(args.n)

  print("\n\tn factorization:",p,"*",q,"\n")

  # On calcule l'indicatrice d'Euler pour reconstruire l'exposant privé d

  phi = indicatrice_euler(p,q)

  d = inv_modulo(args.e, phi)

  print("\tPrivate exponent:",d,"\n")

  # Reconstruction de la clé privée

  key = Crypto.PublicKey.RSA.construct((args.n,args.e,d,p,q))  

  print("\tPrivate key: \n\n\t\t",Crypto.PublicKey.RSA._RSAobj.exportKey(key).decode('utf-8').replace('\n','\n\t\t'),"\n")
