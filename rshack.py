#!/usr/bin/python3
# -*- coding: utf-8 -*-

# RSHack
# Zweisamkeit
# 16/03/17
# GNU/GPL v3

import subprocess
from os import getcwd

def accueil(arg):

  if arg == "first":

    print ("\n")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\t\t          RSHack         ")
    print ("\t\t       Zweisamkeit       ")
    print ("\t\t    Licence GNU GPL v3   ")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n\n")
    print("\tList of the available attacks:")
    print ("\n")
    print("\t\t1. Wiener Attack")
    print("\t\t2. Hastad Attack")
    print("\t\t3. Fermat Attack")
    print("\t\t4. Bleichenbacher Attack")
    print("\t\t5. Common Modulus Attack")
    print("\n\t\t6. RSA public key parameters extraction")
    return(input("\n\tWhat attack do you want to carry out? "))

  elif arg == "again":

    return(input("\n\tPlease enter the number of the attack you want to carry out: "))

def choose(arg):

  attack=accueil(arg)

  if attack == "1":

    print("\n\t\t\t ***** Wiener Attack *****")

    try:

      args=input("\n\t\t Arguments ([-h] -n modulus -e exponent): ").split()
      args=' '.join([str(i) for i in args])

    except:

      print("\n\t\t\tArgument Error: Please verify your inputs\n")
      exit()
    
    subprocess.call(["Attacks/Wiener/wiener.py "+args], shell=True)

  elif attack == "2":

    print("\n\t\t\t ***** Hastad Attack *****")

    try:

      args=input("\n\t\tArguments ([-h] -k0 path_to_key0 -k1 path_to_key1 -k2 path_to_key2 -c0 cipher1 -c1 cipher2 -c2 cipher3): ").split()

      if (args[0] != '-h'):

        for i in range (1,6,2):

          if (args[i][0] != '/'):

            args[i] = getcwd() + '/' + args[i]

      args=' '.join([str(i) for i in args])

    except:

      print("\n\t\t\tArgument Error: Please verify your inputs\n")
      exit()

    subprocess.call(["Attacks/Hastad/hastad.py "+args], shell=True)

  elif attack == "3":

    print("\n\t\t\t ***** Fermat Attack *****")

    try:

      args=input("\n\t\t Arguments ([-h] -n modulus -e exponent): ").split()
      args=' '.join([str(i) for i in args])

    except:

      print("\n\t\t\tArgument Error: Please verify your inputs\n")
      exit()

    subprocess.call(["Attacks/Fermat/fermat.py "+args], shell=True)

  elif attack == "4":

    print("\n\t\t\t ***** Bleichenbacher Attack *****")

    try:

      args=input("\n\t\t Arguments ([-h] -n modulus -e exponent -c ciphertext --host hostname -p port --error error padding message): ").split()
      args=' '.join([str(i) for i in args])

    except:

      print("\n\t\t\tArgument Error: Please verify your inputs\n")
      exit()

    subprocess.call(["Attacks/Bleichenbacher/bleichenbacher.py "+args], shell=True)

  elif attack == "5":

    print("\n\t\t\t ***** Common Modulus Attack *****")

    try:

      args=input("\n\t\t Arguments [-h] -n common modulus -e1 first exponent -e2 second exponent -c1 first cipher -c2 second cipher: ").split()
      args=' '.join([str(i) for i in args])

    except:

      print("\n\t\t\tArgument Error: Please verify your inputs\n")
      exit()

    subprocess.call(["Attacks/Common_Modulus/comod.py "+args], shell=True)

  elif attack == "6":

    print("\n\t\t\t ***** Parameters extraction *****")

    try:

      args=input("\n\t\tArgument ([-h] -k K): ").split()

    except:

      print("\n\t\t\tArgument Error: Please verify your inputs\n")
      exit()

    if (args[0] == '-k' and args[1]!='/'):

      args[1] = getcwd() + "/" + args [1]

    args=' '.join([str(i) for i in args])

    subprocess.call(["Attacks/Other/Extractor/extractor.py "+args], shell=True)

  else:
 
    choose("again")

if __name__ == "__main__":

  choose("first")
