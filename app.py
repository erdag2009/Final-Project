from flask import Flask, render_template, request, jsonify
import librosa

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('music.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio_file' not in request.files:
        return jsonify([]), 400

    audio_file = request.files['audio_file']

    try:
        notes = extract_notes(audio_file)
        return jsonify(notes)
    except Exception as e:
        return jsonify({"error": "Transcription failed", "message": str(e)}), 500
    
durations = {
    1: 'quarter', 
    1.5: 'dotted-quarter',   
    0.5: 'eighth',   
    0.25: 'sixteenth',
    2: 'half',
    3: 'dotted-half',    
    4: 'whole'      
}

def extract_notes(audio_file):
    print("[extract_notes] Start extracting notes from the audio file...")

    # Load audio file with librosa
    y, sr = librosa.load(audio_file)
    print(f"[extract_notes] Audio file loaded. y shape = {y.shape}, sample rate = {sr}")

    # Detect pitch using librosa piptrack
    pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
    print(f"[extract_notes] Pitches shape: {pitches.shape}, Magnitudes shape: {magnitudes.shape}")

    # Detect onsets (the start of each note)
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)
    print(f"[extract_notes] Detected onsets: {onset_times}")

    detected_notes = []

    # assigning frequencies to notes
    pitch_to_note = {
        (164.0, 166.0): "E3",
        (174.0, 176.0): "F3",
        (185.0, 187.0): "F#3",
        (196.0, 198.0): "G3",
        (207.0, 208.0): "G#3",
        (220.0, 222.0): "A3",
        (233.0, 235.0): "A#3",
        (246.0, 248.0): "B3",
        (261.0, 263.0): "C4",
        (277.0, 279.0): "C#4",
        (293.0, 295.0): "D4",
        (311.0, 313.0): "D#4",
        (329.0, 331.0): "E4",
        (349.0, 351.0): "F4",
        (369.0, 371.0): "F#4",
        (392.0, 394.0): "G4",
        (415.0, 417.0): "G#4",
        (439.0, 441.0): "A4",
        (466.0, 468.0): "A#4",
        (493.0, 495.0): "B4",
        (523.0, 525.0): "C5",
        (554.0, 556.0): "C#5",
        (587.0, 589.0): "D5",
        (622.0, 624.0): "D#5",
        (659.0, 661.0): "E5",
        (698.0, 700.0): "F5",
        (740.0, 742.0): "F#5",
        (784.0, 786.0): "G5",
    }

    # checks over detected onsets
    for i, time_idx in enumerate(onset_frames):
        pitch = pitches[:, time_idx]
        mag = magnitudes[:, time_idx]

        # check if it is a valid pitch
        if mag.any() > 0.1:
            idx = mag.argmax()
            note_pitch = pitch[idx]

            if note_pitch > 0:
                print(f"[extract_notes] Detected raw pitch: {note_pitch} Hz")

                #detects the note name
                note_name = None
                for pitch_range, note in pitch_to_note.items():
                    if pitch_range[0] < note_pitch < pitch_range[1]:
                        note_name = note
                        break

                if note_name is None:
                    note_name = librosa.hz_to_note(note_pitch)

                #detect the duration
                if i < len(onset_times) - 1:
                    duration_seconds = onset_times[i + 1] - onset_times[i]
                else:
                    duration_seconds = len(y) / sr - onset_times[i]  

                note_duration = calculate_note_duration(duration_seconds)

                print(f"[extract_notes] Detected pitch: {note_pitch} Hz, Note name: {note_name}, Duration: {note_duration}")

                detected_notes.append({
                    'note': note_name,
                    'duration': note_duration
                })

    #transcribe the notes
    print(f"[extract_notes] Detected notes: {detected_notes}")
    return detected_notes


def calculate_note_duration(duration_seconds):
    #assuming all files' tempo is 60 bpm
    closest_duration = min(durations.keys(), key=lambda x: abs(duration_seconds - x))
    return durations[closest_duration]

if __name__ == '__main__':
    app.run(debug=True)
