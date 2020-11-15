
FROM node:15.1.0-alpine3.10

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build
CMD ["npm", "run", "start"]