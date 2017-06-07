# RSHack for CTF

## About

* This tool written in python allows to carry out one of the available attacks on RSA in this repository:

	* Wiener Attack
	* Hastad Attack
	* Fermat Attack
	* Bleichenbacher Attack
	* Common Modulus Attack
	* Chosen Plaintext Attack

* It can also extract the modulus and the exponent of an RSA public key (decimal value), create an RSA Private Key using its parameters (pem format), and some other features.

* More informations: https://zweisamkeit.fr/rshack/ (fr)

## Requirements

* GNU/Linux (All OS soon, bash comands will be replace by full python scripts)
* Python 3

## FAQ

* How to use it?

You just have to start the following command: ./rshack.py

## Todo

* Replace bash commands (rshack.py) by full python scripts
* Object Oriented Programming only
* Discrete logarithme
* Factorisation (using sage?)
