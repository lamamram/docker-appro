#!/bin/bash

########################### SUPPRESSIONS ################################
# test de l'existence des conteneurs si c'est vrai je supprime les conteneurs
# -q: affiche uniquement les identifiants
[[ -z $(docker ps -aq --filter "name=stack-php-*") ]] || docker rm -f $(docker ps -aq -f "name=stack-php-*")


docker network ls | grep stack-php
if [ $? -eq 0 ]; then
    docker network rm stack-php
fi


# création du réseau ad hoc de type bridge avec la conf 172.18.0.0/16 (gateway sur le .0.1)
# nommé stack-php
docker network create \
--driver=bridge \
--subnet=172.18.0.0/16 \
--gateway=172.18.0.1 \
stack-php



docker run \
--name stack-php-8.3-fpm \
-d --restart unless-stopped \
--network stack-php \
-v ./index.php:/srv/index.php \
bitnami/php-fpm:8.3-debian-12

# plus de besoin de cp puisque le "bind mount" -v dans le run est déjà fait
# docker cp index.php stack-php-8.3-fpm:/srv

docker run \
--name stack-php-nginx \
-d --restart unless-stopped \
--network stack-php \
-p 8080:80 \
-v ./vhost.conf:/etc/nginx/conf.d/vhost.conf \
nginx:1.27.1-alpine-slim

# plus besoin non plus !
# docker cp vhost.conf stack-php-nginx:/etc/nginx/conf.d/vhost.conf
# docker restart stack-php-nginx