FROM python:3.8
WORKDIR /app
EXPOSE 80
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
WORKDIR /app
CMD python3 manage.py runserver