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

# création et / ou de modification de variables d'environnement 
# exploitables dans le DOCKER RUN
ENV USER=tomcat

# création d'arguments exploitables dans le DOCKER BUILD
ARG TOMCAT_VERSION_MAJOR=9
ARG TOMCAT_VERSION_FULL

## BONNES PRATIQUES
# 1. minimiser le nb de couches => instructions => Chaîner les RUN avec &&, ADD => RUN curl, ...
# 2. les actions de créations / modifications / suppressions devraient être mises dans les même couches
# 3. privilégier les actions utilisant les flux ( | ) aux actions utilisant des fichiers ( && )
# 4. privilégier les paquets les plus légers (ex java jdk -> jre)
# => à cause du mécanisme de Copy On Write (COW)
## ajouter un dossier /opt/tomcat
## injecter le fichier https://downloads.apache.org/tomcat/tomcat-9/v9.0.95/bin/apache-tomcat-9.0.95.tar.gz dans ce dossier
## décomprésser dans ce dossier sans dossier intermédiaire
## et supprimer l'archive
## installer java (yum)
## et nettoyer le dépôt yum après
## ajouter un utilisateur tomcat sans le dossier home et le groupe propriétaire
## télécharger l'application sample https://tomcat.apache.org/tomcat-10.1-doc/appdev/sample/sample.war dans le dossier home 
RUN mkdir /opt/tomcat && \
    curl https://downloads.apache.org/tomcat/tomcat-${TOMCAT_VERSION_MAJOR}/v${TOMCAT_VERSION_FULL}/bin/apache-tomcat-${TOMCAT_VERSION_FULL}.tar.gz | \
    tar -xvz -C /opt/tomcat --strip-components=1 && \
    yum update -q && yum install -y -q java-1.8.0-openjdk-headless && \
    yum clean all && rm -rf /var/cache/yum && \
    useradd -M -U tomcat && \
    curl https://tomcat.apache.org/tomcat-10.1-doc/appdev/sample/sample.war -o /opt/tomcat/webapps/sample.war && \
    chown -R tomcat:tomcat /opt/tomcat

## changer le home de l'image vers /opt/tomcat/webapps
WORKDIR /opt/tomcat/webapps
## changer l'utilisateur à tomcat
USER ${USER}
## persister le dossier /opt/tomcat/webapps pour accéder ou sauvegarder les apps
VOLUME [ "/opt/tomcat/webapps" ]
## pour communiquer avec httpd avec le port par défaut de tomcat  ???
EXPOSE 8080
## catalina => foreground, run sur la même session
CMD [ "/opt/tomcat/bin/catalina.sh", "run" ]

# warning: le CMD de HEALTHCHECK est allérgique du lancement de type tokens ["", ""]
# après le lancement du CMD précédent (docker run),
# on attent 3s (start-period)
# pour lancer CMD du HEALTHCHECK avec un timeout de 5s,
# si le CMD est vrai (exit-code 0) => le docker ps donne un STATUS (healthy),
# sinon on peut réessayer 3x (retries), avec une durée d'attente de 3s(interval)
HEALTHCHECK \
            --start-period=3s \
            --timeout=5s \
            --retries=3 \
            --interval=3s \
            CMD grep "Server startup" /opt/tomcat/logs/catalina.*.log