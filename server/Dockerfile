FROM public.ecr.aws/docker/library/python:3.10.13

WORKDIR /app

COPY . ./

RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y


ENV FLASK_APP=main
ENV FLASK_DEBUG=true

CMD ["/bin/bash", "/app/docker-entrypoint.sh"]
