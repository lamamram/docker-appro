## REM: pour réexécuter le build sans cache docker buildx prune -f --filter=1h 

## on prend un image de base de httpd
FROM httpd:2.4

## on documente notre image personnalisée
LABEL author="mlamamra"
LABEL created_at="2024-09-19"
LABEL created_at.year="2024"
LABEL stack="java"
LABEL stack.image="httpd"


## injecter une configuration princicpale personnalisée
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf

## créer un dossier "sites" dans le dossier /usr/local/apache2/conf pour abriter les vhost httpd
RUN mkdir /usr/local/apache2/conf/sites

## injecter le vhost de l'application java



## Déclarer les ports sur lesquels httpd va écouter
EXPOSE 80
# déclaration frauduleuse car httpd n'écoute pas sur 443 dans le httpd.conf !!!!
EXPOSE 443


## spécifier la commande de lancement de l'image personnalisée
# REM1: in faut toujours trouver la manière de lancer en avant-plan dans le conteneur
## CAS ENTRYPOINT
# ENTRYPOINT exécute une commande non substituable par le docker run
# ENTRYPOINT [ "httpd", "-D", "FOREGROUND" ]
# ENTRYPOINT [ "httpd-foreground" ]
# ENTRYPOINT [ "" ] peut neutraliser le ENTRYPOINT de l'image de base

## CAS CMD
# CMD exécute une commande substituable par le docker run
CMD [ "httpd", "-D", "FOREGROUND" ]

## CAS ENTRYPOINT + CMD
# httpd est toujours là dans le docker run mais on peut changer les options
# ENTRYPOINT [ "httpd"]
# CMD ["-D", "FOREGROUND"]