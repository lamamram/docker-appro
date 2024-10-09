BUILDER=$(sudo docker ps | grep buildkitd | cut -f1 -d' ')
sudo docker cp /etc/docker/certs.d/formation.lan:443/ca.crt $BUILDER:/usr/local/share/ca-certificates/ca.crt
sudo docker exec $BUILDER update-ca-certificates
sudo docker restart $BUILDER
