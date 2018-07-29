FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /classifier_api
WORKDIR /classifier_api
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["classifier_api.py"]