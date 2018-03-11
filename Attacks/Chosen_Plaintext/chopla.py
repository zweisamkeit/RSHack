#!/usr/bin/python3
# -*- coding: utf-8 -*-

# RSA Chosen Plaintext Attack
# Zweisamkeit - zweisamkeit.fr
# 07/05/17
# GNU GPL v3

import codecs

class Chopla(object):

  # Accueil

  def accueil(self):

    print ("\n")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\t\t Chosen Plaintext Attack ")
    print ("\t\t       Zweisamkeit       ")
    print ("\t\t    GNU GPL v3 License   ")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n")

  def __init__(self, n, e, c):

    self.accueil()

    c_bis = c * pow(2,e,n) % n

    print("\t[*] Please send the following ciphertext to the server: {}\n".format(c_bis))

    out = int(input("\t[*] What's the result? "))

    p = out // 2

    print("\t[+] The plaintext is: {}\n".format(p))

    try:

      p_text = codecs.decode(hex(p)[2:].replace('L',''), "hex_codec").decode('utf-8')

      print("\n\t[+] The interpreted plaintext: {}\n".format(p_text))

    except:

      print("\t[-] The plaintext is not interpretable\n")
