OpenWeatherMap-Python-Docker
----------------------------

Is a simple application retrieving basic weather information from openweathermap.org API

Running locally
===============

    cd app/
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    OPENWEATHER_API_KEY=XXX CITY_NAME=Honolulu python3 getweather.py

Running in a local Docker container
===================================

    cd app/
    docker build -t weather:dev .
    docker run --rm -e OPENWEATHER_API_KEY=XXX -e CITY_NAME=Honolulu weather:dev

Provisioning fresh Ubuntu VM with a Docker via Ansible
======================================================

This setup by default configures Docker to log into a syslog instead of a json-file

    ansible-playbook -i 'IP_OR_NAME,' site.yml
    ssh IP_OR_NAME  # skip if provisioning localhost
    docker run --rm -e OPENWEATHER_API_KEY=XXX -e CITY_NAME=Honolulu weather:dev
    grep penweathermap /var/log/syslog
