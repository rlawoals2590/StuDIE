FROM public.ecr.aws/docker/library/python:3.10.13

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get -y install libgl1-mesa-glx

ENV FLASK_APP=main
ENV FLASK_DEBUG=true

CMD ["flask", "db", "init"]
CMD ["flask", "db", "migrate"]
CMD ["flask", "db", "upgrade"]

CMD ["flask", "run", "--host=0.0.0.0"]