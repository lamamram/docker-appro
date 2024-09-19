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

## ajouter un dossier /opt/tomcat
RUN mkdir /opt/tomcat
## injecter le fichier https://downloads.apache.org/tomcat/tomcat-9/v9.0.95/bin/apache-tomcat-9.0.95.tar.gz dans ce dossier
ADD https://downloads.apache.org/tomcat/tomcat-9/v9.0.95/bin/apache-tomcat-9.0.95.tar.gz /opt/tomcat/
## décomprésser dans ce dossier sans dossier intermédiaire =
RUN tar -xvzf /opt/tomcat/apache-tomcat-9.0.95.tar.gz -C /opt/tomcat --strip-components=1
## et supprimer l'archive
RUN rm -f /opt/tomcat/apache-tomcat-9.0.95.tar.gz

## installer java (yum)
RUN yum update -q && yum install -y -q java
## et nettoyer le dépôt yum après
RUN yum clean all && rm -rf /var/cache/yum
## ajouter un utilisateur tomcat avec le dossier /opt/tomcat comme home et le groupe propriétaire
## changer le home de l'image vers /opt/tomcat/webapps

## télécharger l'application sample https://tomcat.apache.org/tomcat-10.1-doc/appdev/sample/sample.war dans le dossier home 

## spécifier le propriétaire et groupe à tomcat 
## changer l'utilisateur à tomcat

## persister le dossier home pour accéder ou sauvegarder les apps

## pour communiquer avec httpd avec le port par défaut de tomcat  ???

## exécuter de manière statique (sans substitution) le binaire en foreground catalina.sh vs startup.sh ???

## ajouter la sous commande pour lancer en one shot run ou start ???

