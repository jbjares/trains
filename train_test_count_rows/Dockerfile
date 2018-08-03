FROM lukaszimmermann/pht-train-api-python:latest
LABEL maintainer="luk.zim91@gmail.com"
COPY entrypoint.py /entrypoint.py
RUN chmod +x entrypoint.py
ENTRYPOINT [ "python", "/entrypoint.py"  ]

