FROM python:3.7
WORKDIR /www

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "scanner.run"]
