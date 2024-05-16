#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

if ! which nginx  > /dev/null; then
        sudo apt-get update
        sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/{releases/test,shared}

FILE="/data/web_static/releases/test/index.html"
sudo tee "$FILE" > /dev/null <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

SYMLINK="/data/web_static/current"
[ -e "$SYMLINK" ] && sudo rm -f "$SYMLINK"
sudo ln -sf /data/web_static/releases/test/ "$SYMLINK"
sudo chown -hR ubuntu: /data/

NEW_STRING="server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
FILE_PATH=/etc/nginx/sites-available/default
sudo cat -n /etc/nginx/sites-enabled/default | grep -C 5 "}" | grep -C 5 "location /hbnb_static"
sudo sed -i "s|server_name _;|${NEW_STRING}|g" $FILE_PATH
service nginx restart
