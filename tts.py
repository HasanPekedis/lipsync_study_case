from google.cloud import texttospeech
import os

# Google Cloud Kimlik Doğrulama
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "leafy-container-453009-a1-bc7ea0a1461f.json"  # JSON dosyanın yolunu buraya yaz

client = texttospeech.TextToSpeechClient()

text_input = texttospeech.SynthesisInput(text="""Merhaba, benim adım Ayşe. Bugün hava çok güzel.""")

voice = texttospeech.VoiceSelectionParams(
    language_code="tr-TR",  
    name="tr-TR-Chirp3-HD-Aoede"  
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16  
)

response = client.synthesize_speech(input=text_input, voice=voice, audio_config=audio_config)

# Çıktıyı MP3 dosyasına kaydet
with open("test_google_api.wav", "wb") as audio_file:
    audio_file.write(response.audio_content)

print("Türkçe kadın sesi oluşturuldu: turkce_kadin_sesi.mp3")
