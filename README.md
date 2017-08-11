## Web FCSP

Web FCSP is a web frontend and REST API for [FCSP encoder](https://github.com/DmitryOlshansky/fcsp). 


## Installation

First we need to build and install fcsp encoder.

```shell
sudo apt-get install -y git scons build-essential libboost-dev \
	libboost-filesystem-dev libboost-system-dev libboost-program-options-dev
git clone https://github.com/DmitryOlshansky/fcsp.git
cd fcsp
scons
sudo scons install
cd ..
```

Secondly install the web-fcsp itself.

```shell
sudo apt-get install -y python-dev python-pip
git clone https://github.com/DmitryOlshansky/web-fcsp.git
cd web-fcsp
sudo pip install -r requirements.txt
```

An application server, the default startup script example uses uwsgi
but it's trivial to use anything else.

```shell
sudo pip install uwsgi
```

Optionally - tools for testing.
```shell
sudo pip install httpie
sudo apt-get install -y jq
```

## How to run

An example startup script will run Celery worker and application server.

A quick test:
```shell
./run.sh
./test.sh # should not produce any errors
```
Examine the log files in the current directory for troubleshoting.
