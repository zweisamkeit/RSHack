#!/usr/bin/python3
# -*- coding: utf-8 -*-

# RSA Public Key Constructor
# Zweisamkeit
# 05/07/17
# GNU/GPL v3

import sys
import argparse
from Crypto.PublicKey import RSA

class PubkeyConstruct(object):

  # Accueil

  def accueil():

    print ("\n")
    print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\t  Public Key Constructor ")
    print ("\t       Zweisamkeit       ")
    print ("\t    GNU GPL v3 License   ")
    print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n")

  def __init__(self, n, e, o):

    rsaobj = RSA.construct((n,e))

    key = rsaobj.exportKey().decode('utf-8')

    print("\tThe corresponding RSA public key is : \n\n\t\t{}\n".format(key.replace('\n','\n\t\t')))

    print(o)

    if o is not None: 

      out = open(o,'w+')

      out.write(key)

      out.close()

      print("\tThe key has been saved in {}\n".format(o))