FROM python:3.7.3
WORKDIR /home/app
COPY requirements.txt ./
RUN pip3 install --no-cache -r requirements.txt
COPY . .
EXPOSE 7777
ENTRYPOINT ["python3", "tcp_server.py"]