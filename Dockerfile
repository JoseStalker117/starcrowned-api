FROM python:3.13.5-alpine3.22
WORKDIR /app
COPY requirements.txt .
RUN pip install -r "requirements.txt"
COPY . .
EXPOSE 7777
CMD [ "python3", "main.py"]