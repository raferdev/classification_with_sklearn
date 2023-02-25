FROM python:latest

RUN apt-get -y update &&  apt -y update
RUN pip3 install -U scikit-learn

WORKDIR /app

COPY . .

CMD [ "python","./classification_101.py" ]