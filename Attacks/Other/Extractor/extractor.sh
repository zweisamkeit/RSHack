#!/bin/bash

# Zweisamkeit
# 05/06/17
# Modulus and exponent extractor

echo -e "\n"
echo -e "\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo -e "\t         RSA key Extractor        "
echo -e "\t        Zweisamkeit -- 2017       "
echo -e "\t          License GNU/GPL         "
echo -e "\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo -e "\n"

if [ $# -ne 1 ]
then
  echo -e "\tArgument error: ./extractor.sh public_key_path\n"
  exit
fi

if [ ! -f $1 ]
then
  echo -e "\tFile not found\n"
  exit
fi



modulus=$(hex=$(openssl rsa -pubin -in $1 -modulus 2>/dev/null | grep Modulus | cut -d '=' -f 2) && echo "ibase=16; $hex" | BC_LINE_LENGTH=0 bc)
exponent=$(hex=$(openssl rsa -in $1 -pubin -text -noout 2>/dev/null | grep Exponent | cut -d ':' -f 2 | cut -d ' ' -f 2) && echo "ibase=16; $hex" | BC_LINE_LENGTH=0 bc)

echo -e "\tModulus: $modulus\n\n\tPublic exponent: $exponent\n"


