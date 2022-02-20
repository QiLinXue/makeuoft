import board
import time
import analogio

path_name = 'song.txt'
song_a = 'C:\\Users\\Wasi\\Desktop\\MAKEUOFT_Audio\\FaceOff.mp3'
song_b = 'C:\\Users\\Wasi\\Desktop\\MAKEUOFT_Audio\\palette.mp3'
song_c = 'C:\\Users\\Wasi\\Desktop\\MAKEUOFT_Audio\\arudance.mp3'

hr_sensor_pin = board.GP26_A0
hr_sensor = analogio.AnalogIn(hr_sensor_pin)

# Sampling loop:
print("Running:")
SAMPLING_INTERVAL = 0.1
sensor_data = []

# peak signal detection algorithm
signal_up = False
bpm = 60
threshold = 5
counts = {"easy": 0 , "medium": 0 , "hard": 0}
current_mode = "easy"
prev_mode = "urmom"
while True:
    # read signal from input in pin 2 (currently PulseSensor.com)
    Signal = hr_sensor.value
    Signal = int(Signal / 655.35)
    
    if Signal >= 60:
        if not signal_up:
            sensor_data.append(1)
            signal_up = True
            print("UP")
        else:
            sensor_data.append(0)
            signal_up = False
    else:
        sensor_data.append(0)
        
    if len(sensor_data) > (20/60)*60/SAMPLING_INTERVAL:
        sensor_data.pop(0)
    bpm = sum(sensor_data)/len(sensor_data)*60/SAMPLING_INTERVAL
    print((Signal,))
    
    if bpm < 70:
        counts["easy"] += 1
        counts["medium"] = 0
        counts["hard"] = 0
    elif bpm < 80:
        counts["medium"] += 1
        counts["easy"] = 0
        counts["hard"] = 0
    else:
        counts["hard"] += 1
        counts["easy"] = 0
        counts["medium"] = 0
    
    if counts["easy"] > threshold:
        current_mode = "easy"
    elif counts["medium"] > threshold:
        current_mode = "medium"
    elif counts["hard"] > threshold:
        current_mode = "hard"
    
    if current_mode == "easy":
        with open(path_name, 'w') as f:
            f.write(song_c)
    if current_mode == "medium":
        with open(path_name, 'w') as f:
            f.write(song_b)
    if current_mode == "hard":
        with open(path_name, 'w') as f:
            f.write(song_a)
    
    # pause between samples
    time.sleep(SAMPLING_INTERVAL)