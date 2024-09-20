## scratch pour les images de distribution et applications compilées en un seul binaire
## FROM scratch

## nous allons utiliser une image centos 9: quay.io/centos/centos:stream9

FROM quay.io/centos/centos:stream9

## documenter l'image
LABEL author="mlamamra"
LABEL created_at="2024-09-19"
LABEL created_at.year="2024"
LABEL stack="java"
LABEL stack.image="tomcat"


## BONNES PRATIQUES
# 1. minimiser le nb de couches => instructions => Chaîner les RUN avec &&, ADD => RUN curl, ...
# 2. les actions de créations / modifications / suppressions devraient être mises dans les même couches
# => à cause du mécanisme de Copy On Write (COW)
## ajouter un dossier /opt/tomcat
## injecter le fichier https://downloads.apache.org/tomcat/tomcat-9/v9.0.95/bin/apache-tomcat-9.0.95.tar.gz dans ce dossier
## décomprésser dans ce dossier sans dossier intermédiaire
## et supprimer l'archive
RUN mkdir /opt/tomcat && \
    curl https://downloads.apache.org/tomcat/tomcat-9/v9.0.95/bin/apache-tomcat-9.0.95.tar.gz -o /opt/tomcat/ && \
    tar -xvzf /opt/tomcat/apache-tomcat-9.0.95.tar.gz -C /opt/tomcat --strip-components=1 && \
    rm -f /opt/tomcat/apache-tomcat-9.0.95.tar.gz

## installer java (yum)
## et nettoyer le dépôt yum après
## ajouter un utilisateur tomcat sans le dossier home et le groupe propriétaire
RUN yum update -q && yum install -y -q java && \
    yum clean all && rm -rf /var/cache/yum && \
    useradd -M -U tomcat
## changer le home de l'image vers /opt/tomcat/webapps
WORKDIR /opt/tomcat/webapps
## télécharger l'application sample https://tomcat.apache.org/tomcat-10.1-doc/appdev/sample/sample.war dans le dossier home 



## changer l'utilisateur à tomcat
USER tomcat
## persister le dossier /opt/tomcat/webapps pour accéder ou sauvegarder les apps
VOLUME [ "/opt/tomcat/webapps" ]
## pour communiquer avec httpd avec le port par défaut de tomcat  ???
EXPOSE 8080

CMD [ "/opt/tomcat/bin/catalina.sh", "run" ]

