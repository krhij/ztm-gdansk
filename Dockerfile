FROM python:3.13-slim

#to zeby printy dzialaly ze skryptu
ENV PYTHONUNBUFFERED=1

#to zeby czas dzialal
ENV TZ=Europe/Warsaw
RUN apt-get update && \
    apt-get install -y --no-install-recommends tzdata && \
    ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python","script.py"]
