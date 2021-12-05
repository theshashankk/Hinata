FROM nikolaik/python-nodejs:python3.10-nodejs17
RUN apt-get update \
    && apt-get install -y \
    && apt-get install ffmpeg -y /*
COPY . /app
WORKDIR /app

RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD ["python3", "main.py"]
