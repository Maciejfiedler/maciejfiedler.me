FROM caddy:2.1.1-alpine

VOLUME [ "/data", "/configs" ]

WORKDIR /app

COPY . .

ENV HOST 0.0.0.0

EXPOSE 80

CMD ["caddy", "run"]