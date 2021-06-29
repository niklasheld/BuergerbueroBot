# Bürgerbürobot 🗃

## About

The [Bürgerbüro Pinneberg](https://www.pinneberg.de/index.php?id=522) currently has a waiting time of about two months for simple appointments to apply for documents such as passports and IDs. According to a city official it is possible that earlier appointments are cancelled and become available again.  
This bot scans for available appointments earlier than a set date and notify you with a telegram bot if one becomes available.

This bot should work for all agencies using [cleverQ](https://www.cleverq.de/) for their appointment management. The ``config-example.yaml`` file includes an example configuration for the city of Pinneberg.

## How to deploy

The easiest way to deploy this bot is using docker. Build a docker image using

``docker build -t buergerbuerobot:latest .``

and deploy it using

``docker run -d buergerbuerobot:latest``

You can configure the application by mounting a ``config.yaml``-file inside the ``/app``-directory of the container (see ``config-example.yaml`` for an example configuration) 

Alternatively, you can use this application by installing python and all pip-packages from the ``requirements.txt`` file and then executing ``bot.py`` 