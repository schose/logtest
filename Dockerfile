FROM python:3.8

# set the working directory in the container
WORKDIR /app

# copy the content of the local src directory to the working directory
COPY app/ .

ADD entrypoint.sh /sbin/entrypoint.sh
ENTRYPOINT ["/sbin/entrypoint.sh"]