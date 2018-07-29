FROM python:3
ADD api_consumer.py /
ADD requirements.txt /
RUN  pip install -r requirements.txt
CMD [ "python", "./api_consumer.py" ]