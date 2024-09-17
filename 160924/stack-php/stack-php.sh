#!/bin/bash

########################### SUPPRESSIONS ################################
# test de l'existence des conteneurs si c'est vrai je supprime les conteneurs
# -q: affiche uniquement les identifiants
[[ -z $(docker ps -aq --filter "name=stack-php-*") ]] || docker rm -f $(docker ps -aq -f "name=stack-php-*")

docker run \
--name stack-php-nginx \
-d --restart unless-stopped \
-p 8080:80 \
nginx:1.27.1-alpine-slim