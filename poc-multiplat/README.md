### build &#171;multi-platforme &#187;

* méthode avec *Docker Engine + QEMU*

* prérequis (2 possibilités)
  +  utiliser le *dépôt d'images de containerd* (expériemental)
  + **OU** créer un *builder custom*

* installation de l'émulation des architectures via QEMU
```bash
docker run --privileged --rm \
tonistiigi/binfmt \
--install all | linux/amd64,linux/arm64...

cat /proc/sys/fs/binfmt_misc/qemu-arm | grep "F"  # OK!!
```

---

### dépôt d'images de containerd (I)

```json
// dans la CONFIG SERVEUR de docker  /etc/daemon.json
{
  ...
  "features": {
    ...
    "containerd-snapshotter": true
  }
}
```
* `sudo systemctl restart docker`: redémarre le service docker

---

### exécuter le build multi-platforme (I)

```bash
docker buildx ls
NAME/NODE   DRIVER/ENDPOINT  STATUS   BUILDKIT   PLATFORMS
default*    docker
 \_ default  \_ default      running  v0.16.0    linux/amd64, linux/arm64
```

```Dockerfile
FROM alpine
RUN uname -m > /arch
```

* l'architecture d'un conteneur d'une image multi-plateforme est **ajustée à l'hôte**

```bash
docker build --platform linux/amd64,linux/arm64 -t multiplat .
docker run --rm multiplat cat /arch  # x86_64
```

---

### créer un builder custom (II)

```bash
# en utilisant l'image moby/buildkit:buildx-stable-1
docker buildx create \
       --name multiplat \
       --driver docker-container \
       --bootstrap \               # lancer 
       --use                       # utiliser

## ce builder ne peut pas utiliser le dépôt d'image 
## => build dans une archive OU LE REGISTRY
## le builder DOIT pouvoir se connecter en TLS dans le REGISTRY
BUILDER=$(sudo docker ps | grep buildkitd | cut -f1 -d' ')
sudo docker cp \
     /etc/docker/certs.d/formation.lan:443/ca.crt \
     $BUILDER:/usr/local/share/ca-certificates/ca.crt
sudo docker exec $BUILDER update-ca-certificates
sudo docker restart $BUILDER
```
---

### exécuter le build multi-platforme (II)

```bash
docker buildx ls
NAME/NODE   DRIVER/ENDPOINT  ...
multiplat*    docker-container  ...
 \_ mutliplat0  \_ unix:///var/run/docker.sock  ...

## option1
[docker buildx use miltiplat]
docker buildx build \
       --platform linux/amd64,linux/arm64 -t formation.lan:443/multiplat . \
       --push

## option2
docker build \
       --builder multiplat \
       --platform linux/amd64,linux/arm64 -t formation.lan:443/multiplat . \
       --push

docker run --rm multiplat cat /arch  # x86_64
```

---

### remarques

1. `docker push` et `docker build --push` n'ont pas le même comportement avec le TLS !!!