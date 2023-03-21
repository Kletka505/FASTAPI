FROM python

ENV PYTHONBUFFERED 1

EXPOSE 8000

WORKDIR .

COPY . .
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt