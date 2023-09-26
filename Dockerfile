FROM python:3.10.5-alpine3.16

WORKDIR /usr/src/prj

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/prj/entrypoint.sh
RUN chmod +x /usr/src/prj/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/prj/entrypoint.sh"]