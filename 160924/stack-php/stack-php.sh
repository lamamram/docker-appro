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

docker cp vhost.conf stack-php-nginx:/etc/nginx/conf.d/vhost.conf
docker restart stack-php-nginx

docker run \
--name stack-php-8.3-fpm \
-d --restart unless-stopped \
bitnami/php-fpm:8.3-debian-12

docker cp index.php stack-php-8.3-fpm:/srv