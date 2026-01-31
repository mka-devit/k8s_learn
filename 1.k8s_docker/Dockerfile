FROM python:3.12

RUN groupadd -r userflusk && useradd -r -g userflusk userflusk

RUN pip install --upgrade pip
RUN pip install flask psycopg2-binary

WORKDIR /app
COPY ./flusksite/ .  

EXPOSE 4000
USER userflusk
CMD [ "python", "site.py" ]
