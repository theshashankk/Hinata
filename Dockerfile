FROM nikolaik/1python3.10-nodejs17-bullseye
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /app
WORKDIR /app

RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD ["python3", "main.py"]
