
# The first stage
# Build React static files
FROM node:18.14-alpine AS build

WORKDIR /app/frontend
COPY ./frontend/package.json ./
RUN npm i --silent
COPY ./frontend/ ./
RUN npm run build

# The second stage
# Copy React static files and start nginx
FROM nginx:1.22.1-alpine

COPY --from=build /app/frontend/build /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]