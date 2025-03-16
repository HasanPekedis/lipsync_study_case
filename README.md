# LipSync Study Case

This repository contains a study case for a lip-syncing application based on Wav2Lip. The project synchronizes lip movements of a target face image with a given audio file.

## Features

- Automatically syncs lip movements in image to match a given audio
- Uses Wav2Lip GAN-based model for high-quality lip-sync generation
- Simple web interface

## Prerequisites

- Python 3.6
- `virtualenv` (or `venv`)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/HasanPekedis/lipsync_study_case
cd lipsync_study_case
```

### 2. Create and Activate Virtual Environment

Make sure you are using **Python 3.6**.

```bash
python3.6 -m venv wav2lip_env
source wav2lip_env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Download Pre-trained Model

You will need the pre-trained Wav2Lip GAN model (`wav2lip_gan.pth`) to run this project.

- Download the model from the following link:

[Wav2Lip GAN Model (.pth file)](https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fradrabha%5Fm%5Fresearch%5Fiiit%5Fac%5Fin%2FDocuments%2FWav2Lip%5FModels%2Fwav2lip%5Fgan%2Epth&parent=%2Fpersonal%2Fradrabha%5Fm%5Fresearch%5Fiiit%5Fac%5Fin%2FDocuments%2FWav2Lip%5FModels&ga=1)

- After downloading, place the file in the following directory:

```
src/Wav2Lip/checkpoints/
```

The final path should look like:

```
src/Wav2Lip/checkpoints/wav2lip_gan.pth
```

---

## 5. Ensure Key File

Make sure there is a leafy container `.json` key file in the **root directory** of the project. This key file is necessary for authentication or configuration depending on the implementation of TTS system.


---

## 6. Run the Flask App

```bash
python3 app.py
```

The app will start using Flask's default settings:

- Host: `127.0.0.1` (localhost)
- Port: `5000`

You can access the web interface at:

```
http://127.0.0.1:5000/
```

---

## Notes

- This project is built on top of the [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) model by Rudrabha Mukhopadhyay et al.
- For best results, ensure that the input face video has a clear view of the mouth region.

---
