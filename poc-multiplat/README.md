### build &#171;multi-platforme &#187;

* méthode avec *Docker Engine + QEMU*

* prérequis (2 possibilités)
  +  utiliser le *dépôt d'images de containerd* (expériemental)
  + **OU**  créer un *builder custom*

* installation de l'émulation des architectures
```bash
docker run --privileged --rm \
tonistiigi/binfmt \
--install all | linux/amd64,linux/arm64...
```

### dépôt d'images de containerd

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

### exécuter le build multi-platforme

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