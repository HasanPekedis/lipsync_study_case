from google.cloud import texttospeech
import os
import subprocess

class GenerateSound:
    def __init__(self, credentials_path):
        """
        Initializes the Google TTS client with authentication credentials.
        :param credentials_path: Path to the Google Cloud service account JSON key file.
        """
        self.client = None
        self.credentials_path = credentials_path
        self._initialize_client()

    def _initialize_client(self):
        """Initialize the TTS client and ensure credentials are set."""
        try:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.credentials_path
            self.client = texttospeech.TextToSpeechClient()

        except Exception as e:
            new_dir = "../../"  # Change this to your desired path
            os.chdir(new_dir)
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.credentials_path
            self.client = texttospeech.TextToSpeechClient()
        
        print(f"Google TTS client initialized using credentials from {self.credentials_path}.")
        
    def synthesize(self, text, output_filename):
        """
        Synthesizes speech from the given text and saves it as a WAV file.
        :param text: The text to convert into speech.
        :param output_filename: The output file where the speech audio will be saved.
        :return: The API response containing the audio content.
        """
        try:
            print(f"Synthesizing speech for text: {text[:50]}...")  # Logging first 50 chars for context

            # Prepare the synthesis request
            text_input = texttospeech.SynthesisInput(text=text)

            voice = texttospeech.VoiceSelectionParams(
                language_code="tr-TR",
                name="tr-TR-Chirp3-HD-Aoede"
            )

            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.LINEAR16
            )

            # Call the API to synthesize speech
            response = self.client.synthesize_speech(
                input=text_input, voice=voice, audio_config=audio_config
            )

            # Save the audio response to a file
            with open(output_filename, "wb") as audio_file:
                audio_file.write(response.audio_content)

            print(f"Sound file created: {output_filename}")
            return response
        except Exception as e:
            print(f"Error during speech synthesis: {e}")
            raise  # Re-raise to notify the caller of the error

    def cleanup(self):
        """
        Cleans up resources, including removing environment variables.
        """
        try:
            # Clean up the GOOGLE_APPLICATION_CREDENTIALS environment variable
            if "GOOGLE_APPLICATION_CREDENTIALS" in os.environ:
                del os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
                print("Removed GOOGLE_APPLICATION_CREDENTIALS from environment.")
        except Exception as e:
            print(f"Error during cleanup: {e}")
    
    def reset(self):
        """Reset the client, useful for re-initialization between successive calls."""
        self.cleanup()  # Ensure cleanup of credentials
        self._initialize_client()  # Re-initialize client for the next run
