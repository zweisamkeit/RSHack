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

	* RSA Public Key parameters extraction
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

* Python 2.7 / 3.6
	
	* PyCrypto
	* gmpy2

## Todo

* More attacks (Discrete logarithm, factorization...)
* Python 3 only
* GUI? (v3.0)

## Versions

* Version 2.0 - Saturday, 10 June 2017

	* full POO
	* Multiplateform

## Overview

```
		~~~~~~~~~~~~~~~~~~~~~~~~~
		       RSHack v2.0
		       Zweisamkeit
		        GNU GPL v3
		~~~~~~~~~~~~~~~~~~~~~~~~~



	List of the available attacks:

		1. Wiener Attack
		2. Hastad Attack
		3. Fermat Attack
		4. Bleichenbacher Attack
		5. Common Modulus Attack
		6. Chosen Plaintext Attack

	List of the available tools:

		a. RSA Public Key parameters extraction
		b. RSA Private Key construction (PEM)
		c. RSA Public Key construction (PEM)
		d. RSA Ciphertext Decipher
		e. RSA Ciphertext Encipher

	[*] What attack or tool do you want to carry out?

```

## Credits

* PyCrypto
* Gmpy2

## Alternatives

If my tool does not suit your needs, I know some great tools you'll probrably find intersting:

* [attackrsa](https://github.com/rk700/attackrsa)
* [rsatool](https://github.com/ius/rsatool)
* [CTF-Crypto](https://github.com/ValarDragon/CTF-Crypto)
* [cryptools](https://github.com/sonickun/cryptools)
* [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)
