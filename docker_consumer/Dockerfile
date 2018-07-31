FROM python:3.6
MAINTAINER Lukas Pollmann "lukas.pollmann@outlook.com"
ADD api_consumer.py /
ADD requirements.txt /
RUN  pip install -r requirements.txt
CMD [ "python", "./api_consumer.py" ]