#!/bin/bash

if [ -d "/mnt/nfs-dir" ]; then
  exit 0
fi

# conf "vanilla" pas prod !!!
sudo apt-get update
sudo apt-get install -y nfs-kernel-server
sudo mkdir -p /mnt/nfs-dir/nginx-conf.d
sudo cp ./vhost.conf /mnt/nfs-dir/nginx-conf.d
sudo chown -R nobody:nogroup /mnt/nfs-dir
find /mnt/nfs-dir -type d -print0 | sudo xargs -0 chmod 0755
find /mnt/nfs-dir -type f -print0 | sudo xargs -0 chmod 0644
echo "/mnt/nfs-dir *(rw,sync,no_subtree_check,no_all_squash)" | sudo tee -a /etc/exports
sudo exportfs -a
sudo systemctl restart nfs-kernel-server