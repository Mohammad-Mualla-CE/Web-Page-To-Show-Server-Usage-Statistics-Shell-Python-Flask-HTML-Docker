FROM centos:7

WORKDIR /application

COPY . ./

USER root

RUN yum install -y python3

RUN /bin/pip3 install --upgrade pip

RUN yum -y install cronie

RUN yum install sysstat -y

ADD cron /etc/cron.d/cron_statistics

RUN chmod 0644 /etc/cron.d/cron_statistics

RUN crontab /etc/cron.d/cron_statistics

RUN chmod +x /application/selectstatistics.py

RUN pip3 install -r requirements.txt

CMD ["sh", "-c" ,"sleep 100s ; python3 ./app.py"]
