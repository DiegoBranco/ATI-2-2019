FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r ./requirements.txt

COPY . .

EXPOSE 5001

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
