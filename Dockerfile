FROM ubuntu:latest

#build date/time (unix format)
RUN date > /build_date.txt
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata

RUN apt-get install -o Dpkg::Options::="--force-confold" --force-yes -y imagemagick python3 python3-dev python3-setuptools python3-pip python3-numpy build-essential imagemagick protobuf-compiler python-pil python-lxml python-tk && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install tensorflow

ENV IN_DOCKER Yes

COPY ./ ./cvbot
WORKDIR ./cvbot

RUN pip3 install ./*.whl
RUN pip3 install -r ./requirements.txt
CMD ./run.py
