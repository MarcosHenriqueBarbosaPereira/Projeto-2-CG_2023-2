
from TTS.api import TTS
import os

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
#wav = tts.tts(text="oi gente, boa noite, tudo certinho com vocês?", speaker_wav="audio_teste.mp3", language="pt")
# Text to speech to a file

def generate(text, speaker_wav, tts):
    print(text)
    print(speaker_wav)

    #try to delete output_result.wav if exists
    try:
        os.remove("output_result.wav")
    except:
        pass

    tts.tts_to_file(text=text, speaker_wav=speaker_wav, language="pt", file_path="output_result.wav")
