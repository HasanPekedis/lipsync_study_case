from google.cloud import texttospeech
import os

class GenerateSound:
    def __init__(self, credentials_path):
        """
        Initializes the Google TTS client with authentication credentials.
        :param credentials_path: Path to the Google Cloud service account JSON key file.
        """
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
        self.client = texttospeech.TextToSpeechClient()
    
    def synthesize(self, text, output_filename):
        """
        Synthesizes speech from the given text and saves it as a WAV file.
        :param text: The text to convert into speech.
        :param output_filename: The output file where the speech audio will be saved.
        :return: The API response containing the audio content.
        """
        text_input = texttospeech.SynthesisInput(text=text)

        voice = texttospeech.VoiceSelectionParams(
            language_code="tr-TR",
            name="tr-TR-Chirp3-HD-Aoede"
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )

        response = self.client.synthesize_speech(
            input=text_input, voice=voice, audio_config=audio_config
        )

        # Save the audio response to a file
        with open(output_filename, "wb") as audio_file:
            audio_file.write(response.audio_content)

        print(f"Türkçe kadın sesi oluşturuldu: {output_filename}")
        return response
