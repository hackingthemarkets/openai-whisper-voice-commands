import sounddevice as sd
import wavio as wv
import datetime
import os

def listen(stop_event, recordings_path):
    # Make dir if it doesn't exist
    if not os.path.exists(recordings_path):
        os.makedirs(recordings_path, exist_ok=True)

    # Get the sample frequency of the sound device
    freq = sd.query_devices(None, 'input')['default_samplerate']

    # Set the duration of the recording
    duration = 5 # seconds

    # Calculate the number of samples per duration
    rec_samples = int(freq * duration)

    print('Listening...')
    while not stop_event.is_set():
        ts = datetime.datetime.now()
        filename = ts.strftime("%Y-%m-%d_%H-%M-%S")

        # Start recorder with the given values of duration and sample frequency
        # PTL Note: I had to change the channels value in the original code to fix a bug
        recording = sd.rec(rec_samples, samplerate=freq, channels=2)

        # Record audio for the given number of seconds
        sd.wait()

        # Convert the NumPy array to audio file
        wv.write(os.path.join(recordings_path, filename + '.wav'), recording, freq, sampwidth=2)

    print('Stopped listening')