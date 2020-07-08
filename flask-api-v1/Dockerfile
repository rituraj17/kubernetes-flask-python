FROM python:3.6.1-alpine

#MAINTANER Your Name "krishnarituraj17@gmail.com"

# RUN apt-get update -y && \
#     apt-get install -y python3-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
COPY ./main.py /app/main.py

WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]