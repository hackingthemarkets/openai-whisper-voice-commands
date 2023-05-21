# Python AI Voice Command Interpreter

This repository contains a Python 3.11-based AI project that can interpret and execute vocal commands. The program records vocal inputs, transcribes them, and then processes the transcriptions using another AI to parse the spoken commands.

## Installation

To use this voice command interpreter, please follow these steps:

1. Clone this repository to your local machine using the following command:

```haskell
git clone https://github.com/AuracleTech/command-vocal-interpreter.git
```

2. Navigate to the project directory:

```haskell
cd voice-command-interpreter
```

3. Install the required dependencies by running the following command:

```haskell
pip install -r requirements.txt
```

## Usage

1. Run the main.py file using Python 3.11:

```haskell
python main.py
```

The voice command interpreter will now simultaneously run four threads:

1. Record vocal commands and save them to the recordings folder.
2. Transcribe the recordings and save the transcriptions to the transcriptions folder.
3. Interpret the commands and save the interpreted commands to the commands folder.
4. Execute the commands and vocalize the results.

## Configuration

You can modify the behavior of the voice command interpreter by editing the configuration file located at config.py. The available configuration options include:

- **Recording Settings:** Configure the audio recording settings such as sample rate, duration, and audio format.

- **Transcription Settings:** Configure the transcription process, including the language model and transcription format.
  Command Processing Settings: Configure the AI model used for command interpretation and any additional processing steps.
  Make sure to save the changes and restart the program for the new configuration to take effect.
