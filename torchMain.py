
from TTS.api import TTS
import os

def generate(text, speaker_wav, tts):
    print(text)
    print(speaker_wav)

    try:
        os.remove("output_result.wav")
    except:
        pass

    tts.tts_to_file(text=text, speaker_wav=speaker_wav, language="pt", file_path="output_result.wav")
