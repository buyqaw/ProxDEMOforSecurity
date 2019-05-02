FROM python:3-onbuild
RUN mkdir /alpha
WORKDIR /alpha
COPY . .
EXPOSE 7777 
CMD ["python3", "-u", tcp_server.py"]