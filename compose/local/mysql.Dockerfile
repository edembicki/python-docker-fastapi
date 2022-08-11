FROM mariadb:10.5.8

ARG MYSQL_USER
ARG MYSQL_PASSWORD

CMD ["--default-authentication-plugin=mysql_native_password"]
