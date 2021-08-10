# NOT IN USE

# An image for running a strawberry dev server.
# docker build --no-cache -t mvlancellotti/strawberry-graphql -f dev.Dockerfile . && docker run --rm -p 8777:8000 --volume src:/app --name strawberry-graphql-container mvlancellotti/strawberry-graphql

# Strawberry runs on python, so almost any python should do
FROM python:3.9.6-slim-buster

# install strawberry (with the debug-server option, for development)
RUN pip install strawberry-graphql[debug-server]

# set the working directory
WORKDIR /app

# copy file in, but MAKE SURE to use docker volumes ontop of this for development
# COPY src .

# run the dev server
# CMD ["strawberry", "server", "schema"]
CMD ["sleep", "999999"]
