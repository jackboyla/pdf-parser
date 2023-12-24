FROM python:3.8-bullseye

WORKDIR /srv

RUN pip install --upgrade pip

ADD pdf_parser ./pdf_parser
ADD requirements.txt ./
ADD VERSION ./
ADD setup.py ./
ADD Makefile ./

RUN make dev

CMD make run
