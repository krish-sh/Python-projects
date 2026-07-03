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

stream = sd.InputStream(
    samplerate = RATE,
    channels = CHANNEL,
    dtype = DTYPE,
    blocksize = CHUNK
)

stream.start()
