# registry docker

## build

* gestion de TLS
* gestion d'une authentfication

* `docker login URL du registre https ou :5000 avec --username --password`
* `echo "password" | docker login 127.0.0.1:443 -u testuser --password-stdin`

## utilisations des images

1. il faut renommer une image en tant que référence pour pousser sur le registre
   l'image doit être préfixée par le **nom_de_domaine:port** et
   on peut crée des noms d'espace `<nom_de_domaine:port>/name/space/<basename>:<tag>`   
   `docker tag <image> <new_reference>`

2. pousser une fois qu'on sera autentifié
   `docker push <new_reference>`

   * ou build et push on un coup `docker build -t <nom_de_domaine:port>/name/space/<basename>:<tag> --push .`

3. utiliser l'image depuis `docker pull`

## utilisation du TLS

* warning pour un certif auto signé 
1. modifier ou créer le fichier `/etc/docker/daemon.json`

```
{
   "insecure-registries": ["formation.lan:443"]
}
# sudo systemctl daemon-reload
# sudo systemctl restart docker
```

ajouter le certificat côté client (autorité de certification locale)
```
cd /vagrant/registry
sudo mkdir -p /etc/docker/certs.d/formation.lan:443
sudo cp certs/registry.crt /etc/docker/certs.d/formation.lan:443/ca.crt
```

refabriquer un htpasswd utiliser un container httpd => 
`htpasswd -Bbn testuser password > htpasswd`