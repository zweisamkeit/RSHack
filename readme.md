# RSHack for CTF

RSHack is a tool written in python which allows to carry out some attacks on RSA, and offer a few tools to manipulate RSA keys.

## Features

* Attacks:

	* Wiener Attack
	* Hastad Attack
	* Fermat Attack
	* Bleichenbacher Attack
	* Common Modulus Attack
	* Chosen Plaintext Attack

* Tools:

	* RSA Public Key parameters extraction (PEM)
	* RSA Private Key parameters extraction (PEM)
	* RSA Private Key construction (PEM)
	* RSA Public Key construction (PEM)
	* RSA Ciphertext Decipher
	* RSA Ciphertext Encipher
	
* More informations: https://zweisamkeit.fr/rshack/ (fr)

## Usage

```
$ git clone https://github.com/zweisamkeit/RSHack.git
$ cd RSHack
$ ./rshack.py
```

## Requirements

* Python3
	
	* PyCrypto
	* gmpy2

```
$ pip3 install -r requirements.txt # please install the python3-pip package if necessary
```

## Todo

* More attacks

## Versions

* Version 2.0 - Saturday, 10 June 2017

	* full POO
	* Multiplateform
	
* Version 2.1 - Sunday, 11 March 2018

	* Full Python 3

## Overview

```
		#########################
		#      RSHack v2.1      #
		#      Zweisamkeit      #
		#      GNU GPL v3       #
		#########################



	List of the available attacks:

		1. Wiener Attack
		2. Hastad Attack
		3. Fermat Attack
		4. Bleichenbacher Attack
		5. Common Modulus Attack
		6. Chosen Plaintext Attack

	List of the available tools:

		a. RSA Public Key parameters extraction
		b. RSA Private Key parameters extraction
		c. RSA Private Key construction (PEM)
		d. RSA Public Key construction (PEM)
		e. RSA Ciphertext Decipher
		f. RSA Ciphertext Encipher

	[*] What attack or tool do you want to carry out?

```

## Credits

* PyCrypto
* Gmpy2

## Alternatives

If my tool does not suit your needs, I know some other tools you'll probrably find intersting:

* [attackrsa](https://github.com/rk700/attackrsa)
* [rsatool](https://github.com/ius/rsatool)
* [CTF-Crypto](https://github.com/ValarDragon/CTF-Crypto)
* [cryptools](https://github.com/sonickun/cryptools)
* [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)
