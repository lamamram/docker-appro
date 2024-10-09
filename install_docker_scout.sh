
if [ ! -d "~/.docker" ]; then
  mkdir ~/.docker
fi
curl -sSfL https://raw.githubusercontent.com/docker/scout-cli/main/install.sh | sh -s --