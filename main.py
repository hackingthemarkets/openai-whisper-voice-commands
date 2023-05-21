import threading
import recorder
import transcriber
import keyboard
import os

# Define global variables
stop_event = threading.Event()
data_dir = 'data'
transcript_path = os.path.join(data_dir, 'transcript.txt')
recordings_path = os.path.join(data_dir, 'recordings')

# Make dirs if they don't exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)
if not os.path.exists(recordings_path):
    os.makedirs(recordings_path, exist_ok=True)

# Define thread functions
def listen_thread():
    recorder.listen(stop_event, recordings_path)

def transcribe_thread():
    transcriber.transcribe(stop_event, recordings_path, transcript_path)

# Start the threads
thread1 = threading.Thread(target=listen_thread)
thread2 = threading.Thread(target=transcribe_thread)
# TODO add thread3 for interpreter
# TODO add thread4 for commands & speaker

thread1.start()
thread2.start()

print("Press 's' to stop")
keyboard.wait('s')
print("Stopping...")
stop_event.set()
thread1.join()
thread2.join()
