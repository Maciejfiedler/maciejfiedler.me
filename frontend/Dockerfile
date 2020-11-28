
FROM node:15.1.0-alpine3.10

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ENV HOST 0.0.0.0

# Dev
# CMD ["npm", "run", "dev"]

# Prod
RUN npm run build
CMD ["npm", "run", "start"]