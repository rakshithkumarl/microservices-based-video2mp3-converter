FROM python:3.10-slim-bullseye 

RUN apt-get update \
&& apt-get install -y --no-install-recommends --no-install-suggests \
build-essential default-libmysqlclient-dev \ 
&& pip install --no-cache-dir --upgrade pip

# Creating a working dir to place source code: /app
WORKDIR /app

# Copying requirements.txt separately(rather than with the app code) because when we make changes to app code, we need not re-install the dependencies. We will let it load from cache.
COPY ./requirements.txt /app 
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app/

EXPOSE 5000

CMD ["python3", "server.py"]