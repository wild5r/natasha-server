FROM python:3.5.5-jessie

LABEL maintainer="<>"

USER root

RUN apt-get -y install wget git
RUN pip install -U natasha

EXPOSE 8080
COPY src/ /opt/
CMD ["/usr/local/bin/python3", "/opt/natasha_json_server.py"]
