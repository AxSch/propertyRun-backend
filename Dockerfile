FROM python:latest
LABEL authors="AxSch"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_ROOT_USER_ACTION=ignore
WORKDIR /backend
COPY requirements.txt /backend/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /backend