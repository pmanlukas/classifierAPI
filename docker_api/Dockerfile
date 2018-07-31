FROM python:3.6
MAINTAINER Lukas Pollmann "lukas.pollmann@outlook.com"

WORKDIR /classifier_api/
COPY requirements.txt /app/
RUN pip install -r ./requirements.txt

COPY classifier_api /app/
COPY encoder.pickle /app/
COPY model_svm_C.pickle /app/
COPY tf_transformer.pickle /app/

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["classifier_api.py"]