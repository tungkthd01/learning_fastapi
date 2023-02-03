FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV PYTHONPATH /

WORKDIR /

RUN apt update \
    && apt-get -y install gcc libmariadb-dev \
    && apt install -y default-mysql-client \
    && apt-get install -y default-libmysqlclient-dev \
    && apt install --no-install-recommends -y tzdata \
    && apt-get install -y git \
    && apt clean

COPY /requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt --no-cache-dir

CMD ["uvicorn", "main:app", '--reload' ,"--host", "0.0.0.0", "--port", "80"]
# RUN uvicorn main:app --reload --port=9000 --host=0.0.0.0
COPY . .

EXPOSE 9000