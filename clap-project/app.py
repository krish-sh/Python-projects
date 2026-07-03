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

def open_vscode():
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

print("Listening for 1 clap to open 'Chrome', 2 to open 'Vs Code', 3 to open 'Youtube' and Multiple claps to open all in a time (Press Ctrl+C to stop)")

last_clap_time = 0
clap_count = 0

try:
    while True:
        data, overflowed = stream.read(CHUNK)
        peak = np.abs(data).max()
        current_time = time.time()

        if peak > THRESHOLD and (current_time - last_clap_time) > MIN_DELAY:
            clap_count += 1
            last_clap_time= current_time
            print(f"Clap detected! (Count: {clap_count})")

        if clap_count > 0 and (current_time - last_clap_time) > MAX_DELAY:

            if clap_count == 1:
                    print("Single clap detected! Opening Chrome...")
                    open_chrome("https://www.google.com")
                    
            elif clap_count == 2:
                    print("Double clap detected! Opening VS Code...")
                    open_vscode()
                    
            elif clap_count == 3:
                    print("Triple clap detected! Opening Youtube...")
                    open_youtube()
                   
            else:
                print("Multiple claps detected! Opening everything...")
                open_chrome("https://www.google.com")
                open_vscode()
                open_youtube()
            
            clap_count = 0
            print("Workspace active. Pausing Friday microphone so music doesn't trigger it...")
            time.sleep(14400)

except KeyboardInterrupt:
    print("Friday is shutting down...")
finally:
    stream.stop()
    stream.close()
