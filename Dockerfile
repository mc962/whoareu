FROM python:3.9.1-alpine3.12
LABEL maintainer="11969409+mc962@users.noreply.github.com"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run"]

