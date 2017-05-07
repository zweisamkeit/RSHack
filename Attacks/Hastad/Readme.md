# Attaque de Hastad


* This exploit allows to carry out an Hastad Attack

* Bash script (Linux Only)

	* For now, it needs the binary bdcalc: http://www.di-mgt.com.au/bdcalc.html

	* The script gen.sh allows to test the exploit on an example: ./hastad public[012].pem m[012]

	* The public exponent must be 3

* Python script

	* Usage: -k0 path_to_key0 -k1 path_to_key1 -k2 path_to_key2 -c0 cipher0 -c1 cipher0 -c2 cipher2

* More information: https://zweisamkeit.fr/attaque-de-hastad/
