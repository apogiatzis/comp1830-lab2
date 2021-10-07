FROM gitpod/workspace-full:latest

COPY . /code

WORKDIR /code

RUN pip install -r requirements.txt