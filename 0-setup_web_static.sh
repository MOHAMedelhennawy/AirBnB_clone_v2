#!/usr/bin/env bash
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
sudo ln -s /data/web_static/releases/test/ "$SYMLINK"
sudo chown -Rh ubuntu: /data/

NEW_STRING="server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/\n\t}"
FILE_PATH=/etc/nginx/sites-available/default
sudo sed -i "s|server_name _;|${NEW_STRING}|g" $FILE_PATH
sudo nginx -s reload
