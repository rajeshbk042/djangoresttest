FROM node:14-alpine AS development
ENV NODE_ENV development
# Add a work directory
WORKDIR /app
# Cache and Install dependencies
COPY ./frontend /app

# install and cache app dependencies
COPY ./frontend/package.json /app/package.json
RUN npm install

# start app
CMD ["npm", "start"]