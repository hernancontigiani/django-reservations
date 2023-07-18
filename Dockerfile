FROM python:3.10.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /opt/back

COPY ./reservations /opt/back

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]