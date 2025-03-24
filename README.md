# Videoflix (Backend)

Table of Contents
=================

* [Introduction](#introduction)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Getting Started](#getting-started)
* [How to upload new videos](#how-to-upload-new-videos)
* [API Documentation](#api-documentation)
* [Features](#features)

## Introduction

Videoflix is a full stack video streaming platform for demonstration purposes. The platform allows superusers to upload videos and 'normal' users to register (including email activation) and watch the catgorized videos.

## Prerequisites

* Python
* Redis
* FFmpeg

## Installation

This is a backend to host on Linux (like most backends), so if you are not already using Linux and want to test this project on Windows, you have to use a Linux emulator of your choice.

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

## Getting Started

Start the script for running the backend localhost, redis and celery services using the given script:
```
./start_services.sh
```

Also host the [frontend](https://github.com/Pe3et/Videoflix_frontend) part locally. 

In order to receive a required registration email to be able to test the logged in and password reset functionality, you first need to add existing email credentials in order to receive emails from that added account.
You can do this by filling out the three lines in the .env file.

## How to upload new videos

1. Create a superuser.
```
python manage.py createsuperuser
```
2. Login to the [admin interface](http://127.0.0.1:8000/videoflix/admin/video_app/video/) for uploading videos.
3. Fill in title, description, category, upload a video file and a thumbnail picture.

This process will convert the video to different resolutions as a background process in the database.
You can then register a user on the frontend, login and watch the videos on the hosted frontend.

## API Documentation

When you hosted the project, you can see the documentation here: 
http://127.0.0.1:8000/videoflix/schema/swagger-ui/

## Mentionable Features

* Reset Password via email
* Changing resolutions in video player 