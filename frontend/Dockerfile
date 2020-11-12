
FROM node:15.1.0-alpine3.10

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ENV HOST 0.0.0.0

RUN npm run build
CMD ["npm", "run", "start"]