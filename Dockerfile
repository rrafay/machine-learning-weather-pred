FROM python:3.7.1

RUN pip install --upgrade pip
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r req.txt


EXPOSE 5000
CMD ["python", "/app/app.py"]
