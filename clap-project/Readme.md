# Clap Working 

A minimal clap system that listens for claps to automatically open the application.

## Installation

Install the required Python packages with pip
```bash
py -m pip install numpy
```
```bash
py -m pip install sounddevice
```

## Usage

Start the listner from the terminal
```bash
py app.py
```

Wait for Terminal to print `Listening for 1 clap to open 'Chrome', 2 to open 'Vs Code', 3 to open 'Youtube' and Multiple claps to open all in a time`. Once running give Loud claps

*Note: After triggering the protocol, the listening gets paused to avoid audio feedback from music/videos. To completely stop the script, press `Ctrl+C` in your terminal.*

## How to customize Tasks

To change what happen when you clap, open `app.py` and in the top many functions are shown you can change it manually.

You can add or remove tasks inside this block. 

Or to change how much claps you want to open any application or website simply change in the if-else statemnt. Just choose how many claps you want to inject in a task
