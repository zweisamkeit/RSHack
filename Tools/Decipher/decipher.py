#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# RSA Decipher
# Zweisamkeit - zweisamkeit.fr
# 07/05/17
# GNU GPL v3

import sys
import argparse

class Decipher(object):

  # Accueil

  def accueil():

    print ("\n")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\t\t      RSA Decipher       ")
    print ("\t\t       Zweisamkeit       ")
    print ("\t\t    GNU GPL v3 License   ")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n")

  def __init__(self, n, d, c):

    p = pow(c,d,n)

    print("\t[+] The plaintext is: {}\n".format(p))

    try:

      p_text = hex(p)[2:].replace('L','').decode('hex')

      print("\t[+] The interpreted plaintext: {}\n".format(p_text))

    except:

      print("\t[-] This plaintext is uninterpretable\n")

"""
if __name__ == "__main__" :

  accueil()

  parser = argparse.ArgumentParser(description='This simple program allows to decipher a RSA ciphertext')
  parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
  parser.add_argument('-d', dest='d',type=int,help='RSA private key exponent',required=True)
  parser.add_argument('-c', dest='c',type=int,help='ciphertext',required=True)

  args = parser.parse_args()

  n,d,c = args.n,args.d,args.c

  p = pow(c,d,n)

  print("\t[+] The plaintext is: {}\n".format(p))

  try:

    p_text = hex(p)[2:].replace('L','').decode('hex')

    print("\t[+] The interpreted plaintext: {}\n".format(p_text))

  except:

    print("\t[-] This plaintext is uninterpretable\n")
"""