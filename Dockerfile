FROM python:3.7
WORKDIR /www

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["gunicorn", "run:app", "-c", "./gunicorn.conf.py"]