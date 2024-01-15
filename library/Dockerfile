FROM python:3

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /sprint18

WORKDIR /sprint18

#CMD ["python","manage.py","runserver","0.0.0.0:8001"]
