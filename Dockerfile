FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN ["chmod", "+x", "run.sh"]
RUN pip install --upgrade pip
CMD ["sh", "run.sh"]
