FROM public.ecr.aws/docker/library/python:3.10.13

WORKDIR /app

RUN * /app

RUN pip3 install -r requirements.txt

RUN export FLASK_APP=main && \
    export FLASK_DEBUG=true

RUN flask db init && \
    flask db migrate && \
    flask db upgrade

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]