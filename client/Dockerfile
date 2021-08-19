FROM node:alpine AS react-server

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
ENTRYPOINT ["npm", "start"]

FROM react-server AS react-build

RUN npm run build

FROM nginx:stable as nginx-server

COPY --from=react-build /app/build/ /www/
COPY nginx.conf /etc/nginx/conf.d
COPY certs/ /etc/letsencrypt/live/

CMD [ "sh", "-c", "nginx -g 'daemon off;'" ]