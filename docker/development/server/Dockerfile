FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y libpq-dev \
  && apt-get install -y gettext \
  && apt-get install -y gcc curl

RUN curl https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -o /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

ENV DockerHOME=/home/app/webapp
RUN mkdir -p $DockerHOME
WORKDIR $DockerHOME

RUN pip install --no-cache-dir --upgrade pip
COPY ./requirements/requirements.dev.txt /requirements.dev.txt 
RUN pip install --no-cache-dir -r /requirements.dev.txt

COPY ./docker/development/server/entrypoint.sh /
COPY ./docker/development/server/start.sh /
RUN chmod +x /entrypoint.sh
RUN chmod +x /start.sh

COPY ./server $DockerHOME
ENTRYPOINT ["/entrypoint.sh"]
