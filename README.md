# README

Table of Contents
=================

* [Introduction](#introduction)
* [Getting Started](#getting-started)
* [Features](#features)

## Introduction

 Brief introduction to the project.

## Getting Started

skript starten
front end hosten

beschreibung wie man Videos hochlädt

### Prerequisites
***
List of prerequisites to run the project.
* python
* redis
* (ffmpeg)

### Installation
***
Step-by-step installation instructions.
1. install and set up WSL
```
$ wsl --install
```
2. install redis
```
$ curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
$ echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
$ sudo apt-get update
$ sudo apt-get install redis
```
3. clone git project
4. install python
5. pip install -r .\requirements.txt
6. create admin interface
```
$ python manage.py createsuperuser
```
* login
* go to videos
* upload and fill in all required information e.g. picture for thumbnail, video file, category

## Features

* List of features of the project.