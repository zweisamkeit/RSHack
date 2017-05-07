#!/bin/bash

# Attaque de Hastad
# Zweisamkeit
# 28/11/16

#clear

echo -e "\n"
echo -e "\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo -e "\t           Hastad Attack          "
echo -e "\t        Zweisamkeit -- 2016       "
echo -e "\t          License GNU/GPL         "
echo -e "\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo -e "\n"

# Gestion des erreurs d'arguments

if [ $# -ne 6 ]
then
  echo -e "  Argument error: ./hastad.sh key0.pem key1.pem key2.pem message0 message1 message2\n"
  exit
fi

# Récupération des modules de chaque clé publique

echo -e "\tModulus extraction..."

n0=$(openssl rsa -pubin -in $1 -modulus 2>/dev/null | head -n 1 | cut -d '=' -f2)
n0=$(echo "ibase=16;$n0" | BC_LINE_LENGTH=0 bc)

n1=$(openssl rsa -pubin -in $2 -modulus 2>/dev/null | head -n 1 | cut -d '=' -f2)
n1=$(echo "ibase=16;$n1" | BC_LINE_LENGTH=0 bc)

n2=$(openssl rsa -pubin -in $3 -modulus 2>/dev/null | head -n 1 | cut -d '=' -f2)
n2=$(echo "ibase=16;$n2" | BC_LINE_LENGTH=0 bc)

# Transformation des messages en entiers

echo -e "\tModulus extraction done"

echo -e "\n\tMessages processing..."

m0=$(cat $4 | base64 -d | xxd -ps | tr -d "\n" | tr [a-z] [A-Z])
m0=$(echo "ibase=16;$m0" | BC_LINE_LENGTH=0 bc)

m1=$(cat $5 | base64 -d | xxd -ps | tr -d "\n" | tr [a-z] [A-Z])
m1=$(echo "ibase=16;$m1" | BC_LINE_LENGTH=0 bc)

m2=$(cat $6 | base64 -d | xxd -ps | tr -d "\n" | tr [a-z] [A-Z])
m2=$(echo "ibase=16;$m2" | BC_LINE_LENGTH=0 bc)

echo -e "\tMessages processing done"

# Récupération de l'unique exposant des clés publiques

echo -e "\n\tPublic exponent extraction..."

e=$(openssl rsa -in $1 -pubin -text -noout | tail -n 1 | cut -d ' ' -f2)

echo -e "\tPublic exponent extraction done"

echo -e " \n\tCongruences system: \n"

echo -e "\t\tx^e = m0 mod n0"
echo -e "\t\tx^e = m1 mod n1"
echo -e "\t\tx^e = m2 mod n2"

# On se restreint au cas où e=3

# Algorithme d'Euclide Étendu - Inverse modulaire

function xpgcd {
  u0=1;v0=0;u1=0;v1=1
  b=$1;n=$2
  while [ $n != 0 ]
  do
   read -r q b n <<< "$(echo "$b / $n" | BC_LINE_LENGTH=0 bc) $n $(echo "$b % $n" | BC_LINE_LENGTH=0 bc)"
   read -r u0 u1 <<< "$u1 $(echo "$u0 - ($q * $u1)" | BC_LINE_LENGTH=0 bc)"
   read -r v0 v1 <<< "$v1 $(echo "$v0 - ($q * $v1)" | BC_LINE_LENGTH=0 bc)"
  done;
  export res=$v0
}

# Coefficients de Bachet-Bézout

echo -e "\n\tModular inverse calculation..."

xpgcd ${n0} $(echo "${n1} * ${n2}" | BC_LINE_LENGTH=0 bc)
b0=$res
xpgcd ${n1} $(echo "${n0} * ${n2}" | BC_LINE_LENGTH=0 bc)
b1=$res
xpgcd ${n2} $(echo "${n0} * ${n1}" | BC_LINE_LENGTH=0 bc)
b2=$res

echo -e "\tModular inverse calculation done"

# Cube de la solution du système de congruences

echo -e "\n\tSystem solution cube calculation..."

m=$(echo "($b0 * $m0 * $n1 * $n2) + ($b1 * $m1 * $n0 * $n2) + ($b2 * $m2 * $n0 * $n1)" | BC_LINE_LENGTH=0 bc)
m=$(echo "$m % ($n0 * $n1 * $n2)" | BC_LINE_LENGTH=0 bc)

echo -e "\tSystem solution cube calculation done"

# Calcul de la racine cubique de m, soit la solution du système de congruences

echo -e "\n\tSystem solution calculation..."

x=$(echo "cbrt($m)" | ./bdcalc 2>/dev/null)

if [ $? -ne 0 ]
then
  echo "Error: Put the bdcalc binary in the current folder"
  exit
fi

echo -e "\tSystem solution calculation done"

echo -e "\n\tSolution conversion..."
# Conversion en hexadécimal

x_hex=$(echo "ibase=10;obase=16; $x" | BC_LINE_LENGTH=0 bc)

# Conversion en ascii

P=$(echo $x_hex | xxd -r -p)

echo -e "\tSolution converted"

echo -e "\n\n\t\tThe plaintext is:\n\n$P\n\n"
