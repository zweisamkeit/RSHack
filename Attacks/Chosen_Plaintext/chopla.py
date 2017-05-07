#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# RSA Chosen Plaintext Attack
# Zweisamkeit - zweisamkeit.fr
# 07/05/17
# GNU GPL v3

import sys
import argparse

# Accueil

def accueil():

  print ("\n")
  print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("\t\t Chosen Plaintext Attack ")
  print ("\t\t       Zweisamkeit       ")
  print ("\t\t    GNU GPL v3 License   ")
  print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("\n")


if __name__ == "__main__" :

  accueil()

  parser = argparse.ArgumentParser(description='This program allows to carry out a Chosen Plaintext Attack')
  parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
  parser.add_argument('-e', dest='e',type=int,help='first RSA public key exponent',required=True)
  parser.add_argument('-c', dest='c',type=int,help='ciphertext',required=True)

  args = parser.parse_args()

  n,e,c=args.n,args.e,args.c

  # Calcul du chiffré choisi

  c_bis = c * pow(2,e,n) % n

  print("\tPlease send the following ciphertext to the server: %i\n"%c_bis)

  out = input("\tWhat's the result? ")

  p = out / 2

  print("\tThe plaintext is: %i\n" % p)

  try:

    p_text = hex(p)[2:].replace('L','').decode('hex')

    print("\tThe interpreted plaintext: %s\n" % p_text)

  except:

    print("\tThe plaintext is not interpretable\n")
