FROM python:3.9.0-alpine
WORKDIR /usr/src/app
COPY requirements.txt api.py rsa.py ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["hypercorn", "api:app", "--reload", "-b", "0.0.0.0:9000"]