FROM python:alpine

LABEL maintainer="srimel@pdx.edu"

COPY . /app

WORKDIR /app

RUN pip install --no-cache -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]