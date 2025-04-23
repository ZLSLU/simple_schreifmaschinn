import os
import torchaudio
import torch
import whisper_timestamped as whisper
from pathlib import Path

# === SETTINGS ===
AUDIO_DIR = "audio"
MODEL_PATH = "pytorch_model.bin"
CONFIG_PATH = "config.json"
SAMPLE_RATE = 16000


model = whisper.load_model(MODEL_PATH, device="cpu")


def convert_audio(input_path, output_path):
    waveform, sample_rate = torchaudio.load(input_path)

    if sample_rate != SAMPLE_RATE:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=SAMPLE_RATE)
        waveform = resampler(waveform)

    if waveform.shape[0] > 1:
        waveform = waveform.mean(dim=0, keepdim=True)

    torchaudio.save(output_path, waveform, SAMPLE_RATE)


def transcribe_folder(audio_dir):
    audio_dir = Path(audio_dir)
    for file_path in audio_dir.glob("*"):
        if file_path.suffix.lower() not in [".mp3", ".wav", ".flac", ".m4a", ".ogg"]:
            continue

        temp_wav = file_path.with_suffix(".temp.wav")
        convert_audio(file_path, temp_wav)

        print(f"Transcribing {file_path.name}...")
        result = model.transcribe(str(temp_wav))
        
        output_text_path = file_path.with_suffix(".txt")
        with open(output_text_path, "w", encoding="utf-8") as out_f:
            out_f.write(result["text"])

        temp_wav.unlink()
        print(f"Saved to {output_text_path.name}")

    print("All files transcribed.")


if __name__ == "__main__":
    transcribe_folder(AUDIO_DIR)
