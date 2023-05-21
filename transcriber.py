import whisper
import os, glob

def transcribe(stop_event, recordings_path, transcript_file):
    print('Transcribing...')

    model = whisper.load_model("base")
    recordings = os.path.join(recordings_path, '*.wav')

    while not stop_event.is_set():
        files = glob.glob(recordings);

        # check if folder contains files
        if not files:
            continue

        # get most recent wav recording in the recordings directory
        latest = max(files, key=os.path.getctime)
        
        # check file extension
        if not latest.endswith('.wav'):
            continue

        if os.path.exists(latest):
            audio = whisper.load_audio(latest)
            audio = whisper.pad_or_trim(audio)
            mel = whisper.log_mel_spectrogram(audio).to(model.device)
            options = whisper.DecodingOptions(language= 'en', fp16=False)

            result = whisper.decode(model, mel, options)

            if result.no_speech_prob < 0.5:
                print("Transcript: " + result.text)

                # append text to transcript file
                with open(transcript_file, 'a') as f:
                    f.write(result.text + '\n')
            
            # delete file
            os.remove(latest)
    
    print('Stopped transcribing')
