FROM mrismanaziz/man-userbot:slim-buster

RUN git clone https://github.com/Rewtio/Mikoo-Userbot.git /home/mikoo/ \
    && chmod 777 /home/mikoo \
    && mkdir /home/mikoo/bin/

WORKDIR /home/mikoo/

CMD [ "bash", "start" ]
