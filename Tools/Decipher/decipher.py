#!/usr/bin/python3
# -*- coding: utf-8 -*-

# RSA Decipher
# Zweisamkeit - zweisamkeit.fr
# 07/05/17
# GNU GPL v3

import codecs

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

      p_text = codecs.decode(hex(p)[2:].replace('L',''), "hex_codec").decode('utf-8')

      print("\t[+] The interpreted plaintext: {}\n".format(p_text))

    except:

      print("\t[-] This plaintext is uninterpretable\n")
