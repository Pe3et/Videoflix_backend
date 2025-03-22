# Videoflix (Backend)

Table of Contents
=================

* [Introduction](#introduction)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Getting Started](#getting-started)
* [Features](#features)

## Introduction

Videoflix is a full stack video streaming platform for demonstration purposes. The platform allows superusers to upload videos and 'normal' users to register (including email activation) and watch the catgorized videos.

## Prerequisites

* Python
* Redis
* FFmpeg

## Installation

### On Linux

1. Install the latest Python, Redis and FFmpeg version.
2. Clone the repository.
3. Navigate into the cloned folder and activate the environment.
```
python3 -m venv env
source env/bin/activate
```
4. Install the required packages using pip.
```
python3 pip install -r requirements.txt
```

### On Windows

(Caution: unfinished instructions)

1. Install the latest Python and FFmpeg version.
2. Install and set up WSL.
```
wsl --install
```
3. Install Redis on WSL.
```
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update
sudo apt-get install redis
```
4. Clone the repository.
5. Navigate into the cloned folder and activate the environment.
```
python -m venv env
env\Scripts\activate.bat
```
6. Install the requirements.
```
pip install -r .\requirements.txt

```

## Getting Started

Start the Script for running the Backend localhost, redis and celery services using the start_services.sh (linux) or start_services.bat(windows) script.

Also host the [frontend](https://github.com/Pe3et/Videoflix_frontend) part locally. 

In order to receive a required registration email and being able to test the password reset functionality, you first need to add email credentials in order to receive emails from that added account.
You can do this by filling out the three lines in the .env file.

How to upload new videos:

1. Create a superuser.
```
python manage.py createsuperuser
```
2. Login to the [admin interface](http://127.0.0.1:8000/videoflix/admin/video_app/video/) for uploading videos.
3. Fill in title, description, category, upload a video file and a thumbnail picture.

This process will convert the video to different resolutions as a background process in the database.
You can then register a user on the frontend, login and watch the videos on the hosted frontend.

## Mentionable Features

* Reset Password via email
* Changing resolutions in video player 