#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import getcwd

import argparse

from subprocess import call

from attacks import Attack
from tools import Tool

import readline

# Accueil

def accueil(arg):

	if arg == "first":

		call(["clear"], shell=True)

		print("\n")
		print("\t\t#########################")
		print("\t\t#      RSHack v2.1      #")
		print("\t\t#      Zweisamkeit      #")
		print("\t\t#      GNU GPL v3       #")
		print("\t\t#########################")
		print("\n\n")
		print("\tList of the available attacks:\n")
		print("\t\t1. Wiener Attack")
		print("\t\t2. Hastad Attack")
		print("\t\t3. Fermat Attack")
		print("\t\t4. Bleichenbacher Attack")
		print("\t\t5. Common Modulus Attack")
		print("\t\t6. Chosen Plaintext Attack")
		print("\n\tList of the available tools:\n")
		print("\t\ta. RSA Public Key parameters extraction")
		print("\t\tb. RSA Private Key parameters extraction")
		print("\t\tc. RSA Private Key construction (PEM)")
		print("\t\td. RSA Public Key construction (PEM)")
		print("\t\te. RSA Ciphertext Decipher")
		print("\t\tf. RSA Ciphertext Encipher")

		return input("\n\t[*] What attack or tool do you want to carry out? ")

	elif arg == "again":

		return input("\n\t[*] Please enter the number of the attack you want to carry out: ")

# Fonction de traitement et de lancement

def choose(arg):

	attack = str(accueil(arg))

	if attack == "1":

		print("\n\t\t\t ***** Wiener Attack *****")

		args = input("\n\t\t[*] Arguments ([-h] -n modulus -e exponent):\n\n\t\t\t").split()

		parser = argparse.ArgumentParser(description='This program allows to carry out a Wiener Attack')
		parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
		parser.add_argument('-e', dest='e',type=int,help='RSA public key exponent',required=True)

		params=parser.parse_args(args)

		attack_object = Attack(params)
		attack_object.wiener()

	elif attack == "2":

		print("\n\t\t\t ***** Hastad Attack *****")

		try:

			args = input("\n\t\t[*] Arguments ([-h] -n0 modulus_key0 -n1 modulus_key1 -n2 modulus_key2 -e public_exponent -c0 cipher1 -c1 cipher2 -c2 cipher3):\n\n\t\t\t").split()

		except:

			print("\n\t\t\t[-] Argument Error: Please verify your inputs\n")
			exit()


		parser = argparse.ArgumentParser(description='This program allows to carry out an Hastad Attack')
		parser.add_argument('-n0', dest='n0',type=int,help='Modulus of the first RSA pulic key (decimal)',required=True)
		parser.add_argument('-n1', dest='n1',type=int,help='Modulus of the second RSA pulic key (decimal)',required=True)
		parser.add_argument('-n2', dest='n2',type=int,help='Modulus of the third RSA pulic key (decimal)',required=True)
		parser.add_argument('-e', dest='e',type=int,help='Common public exponent (decimal)',required=True)
		parser.add_argument('-c0', dest='c0',type=int,help='first ciphertext (decimal)',required=True)
		parser.add_argument('-c1', dest='c1',type=int,help='second ciphertext (decimal)',required=True)
		parser.add_argument('-c2', dest='c2',type=int,help='third ciphertext (decimal)',required=True)
		params=parser.parse_args(args)

		attack_object = Attack(params)
		attack_object.hastad()

	elif attack == "3":

		print("\n\t\t\t ***** Fermat Attack *****")

		try:

			args = input("\n\t\t[*] Arguments ([-h] -n modulus -e exponent):\n\n\t\t\t").split()

		except:

			print("\n\t\t\t[-] Argument Error: Please verify your inputs\n")
			exit()

		parser = argparse.ArgumentParser(description='This program allows to carry out a Fermat Factorization')
		parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
		parser.add_argument('-e', dest='e',type=int,help='RSA public key exponent',required=True)

		params=parser.parse_args(args)

		attack_object = Attack(params)
		attack_object.fermat()

	elif attack == "4":

		print("\n\t\t\t ***** Bleichenbacher Attack *****")

		try:

			args = input("\n\t\t[*] Arguments ([-h] -n modulus -e exponent -c ciphertext --host hostname -p port --error error padding message):\n\n\t\t\t").split()

		except:

			print("\n\t\t\t[-] Argument Error: Please verify your inputs\n")
			exit()

		parser = argparse.ArgumentParser(description='This program allows to carry out a Bleichenbacher Attack')
		parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus (int)',required=True)
		parser.add_argument('-e', dest='e',type=int,help='RSA public key exponent (int)',required=True)
		parser.add_argument('-c', dest='c',type=int,help='ciphertext (int)',required=True)
		parser.add_argument('--host', dest='host',type=str,help='hostname',required=True)
		parser.add_argument('-p', dest='port',type=int,help='port',required=True)
		parser.add_argument('--error', dest='error',type=str,help='Oracle Padding Error',required=True)
		params=parser.parse_args(args)

		attack_object = Attack(params)
		attack_object.bleichenbacher()

	elif attack == "5":

		print("\n\t\t\t ***** Common Modulus Attack *****")

		try:

			args = input("\n\t\t[*] Arguments [-h] -n common modulus -e1 first exponent -e2 second exponent -c1 first cipher -c2 second cipher:\n\n\t\t\t").split()

		except:

			print("\n\t\t\t[-] Argument Error: Please verify your inputs\n")
			exit()

		parser = argparse.ArgumentParser(description='This program allows to carry out a Common Modulus Attack')
		parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
		parser.add_argument('-e1', dest='e1',type=int,help='First RSA public key exponent',required=True)
		parser.add_argument('-e2', dest='e2',type=int,help='Second RSA public key exponent',required=True)
		parser.add_argument('-c1', dest='c1',type=int,help='First ciphered text',required=True)
		parser.add_argument('-c2', dest='c2',type=int,help='Second ciphered text',required=True)

		params=parser.parse_args(args)

		attack_object = Attack(params)
		attack_object.comod()


	elif attack == "6":

		print("\n\t\t\t ***** Chosen Plaintext Attack *****")

		try:

			args = input("\n\t\t[*] Arguments ([-h] -n modulus -e public_exponent -c ciphertext):\n\n\t\t\t").split()

		except:

			print("\n\t\t\t[-] Argument Error: Please verify your inputs\n")
			exit()

		parser = argparse.ArgumentParser(description='This program allows to carry out a Chosen Plaintext Attack')
		parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
		parser.add_argument('-e', dest='e',type=int,help='first RSA public key exponent',required=True)
		parser.add_argument('-c', dest='c',type=int,help='ciphertext',required=True)
		params=parser.parse_args(args)
		params=parser.parse_args(args)

		attack_object = Attack(params)
		attack_object.chopla()

	elif attack == "a":

		print("\n\t\t\t ***** RSA Public Key parameters extraction *****")

		try:

			args = input("\n\t\t[*] Argument ([-h] -k K):\n\n\t\t\t").split()

		except:

			print("\n\t\t\t[-] Argument Error: Please verify your inputs\n")
			exit()

		if args[0] == '-k' and args[1]!='/':

			args[1] = getcwd() + "/" + args [1]

		parser = argparse.ArgumentParser(description='This program allows to extract the modulus and the exponent of an RSA public key (PEM)')

		parser.add_argument('-k', dest='k',type=str,help='path of the RSA public key',required=True)
		params=parser.parse_args(args)

		tool_object = Tool(params)
		tool_object.pubex()

	elif attack == "b":

		print("\n\t\t\t ***** RSA Private Key paramters extraction *****")

		try:

			args = input("\n\t\t[*] Argument ([-h] -k K):\n\n\t\t\t").split()

		except:

			print("\n\t\t\t[-] Argument Error: Please verify your inputs\n")
			exit()

		if args[0] == '-k' and args[1]!='/':

			args[1] = getcwd() + "/" + args [1]

		parser = argparse.ArgumentParser(description='This program allows to extract the parameters of an RSA private key (PEM)')

		parser.add_argument('-k', dest='k',type=str,help='path of the RSA private key',required=True)
		params=parser.parse_args(args)

		tool_object = Tool(params)
		tool_object.privex()


	elif attack == "c":

		print("\n\t\t\t ***** RSA Private Key constructor *****")

		try:

			args = input("\n\t\t[*] Argument ([-h] -p first_factorization_element -q second_factorization_element -e public_exponent [-o output_file]):\n\n\t\t\t").split()

		except:

			print("\n\t\t\t[-] Argument Error: Please verify your inputs\n")
			exit()


		parser = argparse.ArgumentParser(description='This program allows to construct an RSA Private Key with its parameters')

		parser.add_argument('-p', dest='p',type=int,help='first element of the modulus factorization',required=True)
		parser.add_argument('-q', dest='q',type=int,help='second element of the modulus factorization',required=True)
		parser.add_argument('-e', dest='e',type=int,help='public exponent',required=True)
		parser.add_argument('-o',dest='o',type=str,help='output file')
		params=parser.parse_args(args)

		tool_object = Tool(params)
		tool_object.privkeyconstruct()

	elif attack == "d":

		print("\n\t\t\t ***** RSA Public Key constructor *****")

		try:

			args = input("\n\t\t[*] Argument ([-h] -n modulus -e public_exponent [-o output_file]):\n\n\t\t\t").split()

		except:

			print("\n\t\t\t[-] Argument Error: Please verify your inputs\n")
			exit()

		parser = argparse.ArgumentParser(description='This program allows to construct an RSA Public Key with its parameters')

		parser.add_argument('-n', dest='n',type=int,help='modulus',required=True)
		parser.add_argument('-e', dest='e',type=int,help='public exponent',required=True)
		parser.add_argument('-o',dest='o',type=str,help='output file')
		params=parser.parse_args(args)

		tool_object = Tool(params)
		tool_object.pubkeyconstruct()


	elif attack == "e":

		print("\n\t\t\t ***** RSA Decipher *****")

		try:

			args = input("\n\t\t[*] Argument ([-h] -n modulus -d private_exponent -c ciphertext):\n\n\t\t\t").split()

		except:

			print("\n\t\t\t[-] Argument Error: Please verify your inputs\n")
			exit()

		parser = argparse.ArgumentParser(description='This simple program allows to decipher a message using RSA')
		parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
		parser.add_argument('-d', dest='d',type=int,help='RSA private key exponent',required=True)
		parser.add_argument('-c', dest='c',type=int,help='ciphertext',required=True)
		params=parser.parse_args(args)

		tool_object = Tool(params)
		tool_object.decipher()

	elif attack == "f":

		print("\n\t\t\t ***** RSA Encipher *****")

		try:

			args = input("\n\t\t[*] Argument ([-h] -n modulus -e public_exponent -p plaintext):\n\n\t\t\t").split()

		except:

			print("\n\t\t\t[-] Argument Error: Please verify your inputs\n")
			exit()

		parser = argparse.ArgumentParser(description='This simple program allows to encipher a message using RSA')
		parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
		parser.add_argument('-e', dest='e',type=int,help='RSA public key exponent',required=True)
		parser.add_argument('-p', dest='p',type=int,help='plaintext',required=True)
		params=parser.parse_args(args)

		tool_object = Tool(params)
		tool_object.encipher()

	else:

		choose("again")

# Main

if __name__ == "__main__":

	choose("first")
