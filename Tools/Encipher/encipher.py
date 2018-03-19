#!/usr/bin/python3
# -*- coding: utf-8 -*-

# RSA Encipher
# Zweisamkeit - zweisamkeit.fr
# 07/05/17
# GNU GPL v3

import sys
import argparse

class Encipher(object):

  # Accueil

  def accueil(self):

    print ("\n")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\t\t      RSA Encipher       ")
    print ("\t\t       Zweisamkeit       ")
    print ("\t\t    GNU GPL v3 License   ")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n")

  def __init__(self,n,e,p):

    c = pow(p,e,n)

    print("\t[+] The ciphertext is: {}\n".format(c))
  
