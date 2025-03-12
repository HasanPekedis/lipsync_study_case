from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import subprocess
import uuid
from src.classes.generator import  Generator 

app = Flask(__name__)

# Paths
AVATAR_IMAGE = "../../assets/images/model.jpg"
OUTPUT_VIDEO = "../../assets/videos/"
WAV2LIP_PATH = "../Wav2Lip/inference.py"  # Change this to your Wav2Lip directory

@app.route("/")
def index():
    return render_template("app/templates/main.html")

@app.route("/generate", methods=["POST"])
def generate():
    text = request.form.get("text")
    
    if not text:
        return jsonify({"error": "Text cannot be empty"}), 400
    
    guid = uuid.uuid4()  

    generator = Generator(guid, text)
    generator.start()


    
    

    




if __name__ == "__main__":
    app.run(debug=True)
