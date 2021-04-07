FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN PATH="/usr/bin/pg_config:$PATH" && pip3 install -r requirement.txt
EXPOSE 5434
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]