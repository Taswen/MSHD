FROM python:3.7
WORKDIR /www

COPY requirements.txt ./
RUN pip install -r requirements.txt 

COPY . .

CMD ["gunicorn", "run:app", "-c", "./gunicorn.conf.py","--log-level","debug"]
