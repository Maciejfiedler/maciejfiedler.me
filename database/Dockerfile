FROM redis:6.0.9-alpine

VOLUME [ "/data" ]

WORKDIR /data

COPY redis.conf /etc/redis.conf

ENV HOST 0.0.0.0

CMD ["redis-server", "/etc/redis.conf"]