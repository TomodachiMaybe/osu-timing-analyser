import librosa

def analyze_audio(file_path):
    y, sr = librosa.load(file_path, sr=None)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    offset = beat_times[0] if len(beat_times) > 0 else 0.0
    offset = offset * 1000

    print(f"BPM (Tempo): {tempo:.2f}")
    print(f"Offset (first beat): {offset:.3f} seconds")
analyze_audio(input("Input the filepath to the .mp3 file:    "))