#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# RSA Common Modulus Attack
# Zweisamkeit - zweisamkeit.fr
# 03/05/17
# GNU GPL v3

import sys
import argparse

# Accueil

def accueil():

  print ("\n")
  print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("\t\t  Common Modulus Attack  ")
  print ("\t\t       Zweisamkeit       ")
  print ("\t\t    GNU GPL v3 License   ")
  print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("\n")

# Extended gdc 

sys.setrecursionlimit(1000000)

def xgcd(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    gcd, u, v = xgcd(b % a, a)
    return (gcd, v - (b // a) * u, u)

def modinv(a, n):
  g, x, y = xgcd(a, n)
  return x % n

def pow_mod(a, b, n):
  number = 1
  while b:
    if b & 1:
      number = number * a % n
    b >>= 1
    a = a * a % n
  return number

# Main

if __name__ == "__main__" :

  accueil()

  parser = argparse.ArgumentParser(description='This program allows to carry out a Common Modulus Attack')
  parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
  parser.add_argument('-e1', dest='e1',type=int,help='First RSA public key exponent',required=True)
  parser.add_argument('-e2', dest='e2',type=int,help='Second RSA public key exponent',required=True)
  parser.add_argument('-c1', dest='c1',type=int,help='First ciphered text',required=True)
  parser.add_argument('-c2', dest='c2',type=int,help='Second ciphered text',required=True)

  args = parser.parse_args()


  # Calcul des coefficients de Bachet Bézout

  egcd = xgcd(args.e1, args.e2)

  u, v = egcd[1], egcd[2]

  # Calcul du plaintext

  if u >= 0:

    p1 = pow_mod(args.c1,u,args.n)

  else:

   p1 = modinv(pow_mod(args.c1,-u,args.n),args.n)

  if v >= 0:

    p2 = pow_mod(args.c2,v,args.n)

  else:

    p2 = modinv(pow_mod(args.c2,(-v),args.n),args.n)

  res = (p1 * p2) % args.n

  # Affichage du résultat

  print "\tDecimal plaintext: ",res,"\n"

  plaintext = hex(res)[2:].replace('L','').decode('hex')

  print "\tInterpreted plaintext: ",plaintext,"\n"
