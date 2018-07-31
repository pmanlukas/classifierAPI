FROM python:3.6
MAINTAINER Lukas Pollmann "lukas.pollmann@outlook.com"

WORKDIR /classifier_api/
COPY requirements.txt /classifier_api/
RUN pip install -r ./requirements.txt

COPY classifier_api.py /classifier_api/
COPY encoder.pickle /classifier_api/
COPY model_svm_C.pickle /classifier_api/
COPY tf_transformer.pickle /classifier_api/

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["classifier_api.py"]