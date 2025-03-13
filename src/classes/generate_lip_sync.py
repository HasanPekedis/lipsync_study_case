import os
import subprocess

def lip_sync(audio_path, output_path):
    """Call Wav2Lip to generate a talking avatar"""
    
    wav2lip_path = "src/Wav2Lip"  # Change this to the actual Wav2Lip directory
    os.chdir(wav2lip_path)  # Change directory to Wav2Lip
    
    # Run the inference script
    subprocess.run([
        "python3", "inference.py",
        "--checkpoint_path", "checkpoints/wav2lip_gan.pth",
        "--face", "../../static/images/model.jpg",
        "--audio", audio_path,
        "--outfile", output_path
    ])

    print(f"Generated lip-synced video: {output_path}")

