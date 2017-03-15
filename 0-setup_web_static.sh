#!/usr/bin/env bash
# Prepares web servers for deployment
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Holberton" | sudo tee /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "37i\ \n\n\tlocation /hbnb_static/ {\n\talias\t/data/web_static/current/;\n\tautoindex off;\n}" /etc/nginx/sites-enabled/default
sudo service nginx restart
