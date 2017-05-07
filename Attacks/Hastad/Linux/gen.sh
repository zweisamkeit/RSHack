#!/bin/bash

for i in 0 1 2
do
  openssl genrsa -3 -out private$i.pem 2048
  openssl rsa -in private$i.pem -outform PEM -pubout -out public$i.pem
  echo -ne "Il etait paresseux, a ce que dit l'histoire,\nIl laissait trop secher l'encre dans l'ecritoire.\nIl voulait tout savoir mais il n'a rien connu.\n\n\t - Gerard de Nerval, Epitaphe\n                                                                                  " | openssl rsautl -encrypt -pubin -raw -inkey public$i.pem | base64 > m$i
done
