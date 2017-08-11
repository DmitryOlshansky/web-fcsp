#!/bin/bash
nohup celery -l INFO -A encoder worker > celery.log 2>&1 &
nohup uwsgi --ini uwsgi.ini > web-fcsp.log 2>&1 &

