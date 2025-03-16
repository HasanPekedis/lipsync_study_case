from .generate_sound import GenerateSound
from .generate_lip_sync import lip_sync
import os

class Generator:
    def __init__(self, guid, text):
        self.guid = guid
        self.text = text
       
    def start(self):

        sound_path = f"static/sounds/{self.guid}.wav"
        video_path = f"static/videos/{self.guid}.mp4"

        generate_sound = GenerateSound("leafy-container-453009-a1-a2f7e8069251.json")
        
        os.makedirs(os.path.dirname(sound_path), exist_ok=True)

        generate_sound.synthesize(self.text, sound_path)
        
        lip_sync("../../" + sound_path,"../../" + video_path)








