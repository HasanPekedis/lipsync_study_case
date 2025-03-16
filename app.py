from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
import uuid
from src.classes.generator  import  Generator 
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/main.html")

@app.route("/generate", methods=['GET',"POST"])
def generate():
    text = request.form.get("textInput")
    
    if not text:
        return jsonify({"error": "Text cannot be empty"}), 400
    
    guid = str(uuid.uuid4()) 

    generator = Generator(guid, text)
    generator.start()

    return redirect(url_for("video", guid=guid))

@app.route("/video/<guid>")
def video(guid):
    return render_template("/main.html", guid=guid)

if __name__ == "__main__":
    app.run(debug=True)
