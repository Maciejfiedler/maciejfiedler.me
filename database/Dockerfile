FROM redis:6.0.9-alpine

VOLUME [ "/data" ]

COPY ./redis.conf /etc/redis.conf

WORKDIR /data

ENV HOST 0.0.0.0

CMD ["redis-server", "/etc/redis.conf"]