FROM caddy:2.1.1-alpine

WORKDIR /app
VOLUME [ "/data", "/config" ] 

COPY . .

ENV HOST 0.0.0.0

EXPOSE 80
EXPOSE 443

CMD ["caddy", "run"]