FROM python:3-stretch

RUN mkdir /code && \
    pip install prometheus_client

COPY metrics.py /code

WORKDIR /code

EXPOSE 8000

EXPOSE 8001


# CMD ["python", "-m", "http.server", "8001"]
CMD ["python", "metrics.py"]
