# Python Music Player

## Overview
This project is a basic music player application developed using Python.  
It provides a simple graphical interface that allows users to play, pause, and navigate through audio tracks using on-screen controls.

## Features
- Play and pause audio playback  
- Navigate to the previous or next track  
- Automatically loads and plays audio files on launch  
- Simple and lightweight design  

## Controls
The interface includes four buttons:
- **Play**
- **Pause**
- **Previous**
- **Next**

Button image files must be located in the same directory as the Python source code.

## Supported Audio Formats
- MP3  
- WAV  

> Other audio formats are not supported.

## Project Structure
For the application to function correctly, files must be organized as follows:
```text
project-folder/
│
├── main.py
├── play.png
├── pause.png
├── next.png
├── previous.png
│
└── music/
    ├── song1.mp3
    ├── song2.wav
    └── song3.mp3
