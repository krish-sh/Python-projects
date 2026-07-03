import numpy as np
import sounddevice as sd
import time
import subprocess

THRESHOLD = 10000
MIN_DELAY = 0.2
MAX_DELAY = 1.0
CHUNK = 1024
DTYPE = 'int16'
CHANNEL = 1
RATE  = 44100

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
vscode_path = r"C:\Users\win 10\AppData\Local\Programs\Microsoft VS Code\Code.exe"

def open_chrome(url):
    subprocess.Popen([
        chrome_path,
        url
    ])

def open_youtube():
    open_chrome("https://www.youtube.com")

def open_vscode(vccode_path):
    subprocess.Popen([
        vscode_path
    ])


stream = sd.InputStream(
    samplerate = RATE,
    channels = CHANNEL,
    dtype = DTYPE,
    blocksize = CHUNK
)

stream.start()
