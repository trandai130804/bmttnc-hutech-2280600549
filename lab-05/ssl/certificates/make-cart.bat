mkdir certificates
openssl req -new -x509 -days 365 -nodes -out certificates/server-cert.crt -keyout certificates/server-key.key