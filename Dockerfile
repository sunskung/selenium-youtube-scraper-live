FROM node:12

WORKDIR /app

COPY  docker_test.py ./

RUN npm install

COPY . .

ENV PORT=8080