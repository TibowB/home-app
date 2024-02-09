# Removes nginx version in headers

server_tokens off;

# Extend supported mime-types

types {
  font/ttf                         ttf;
  font/otf                         otf;
}

# Expires map for cache-control directive

map $sent_http_content_type $expires {
    default                    off;
    text/html                epoch;
    text/css                   max;
    application/javascript     max;
    ~image/                    max;
    ~font/                     max;
}

# Nginx server

server {
  listen      80;

  # Cache control
  expires $expires;
  root   /usr/share/nginx/html;
  location / {
    index  index.html;
    try_files $uri /index.html $uri/ =404;
  }

  error_page   500 502 503 504  /50x.html;

  location = /50x.html {
    root   /usr/share/nginx/html;
  }
}