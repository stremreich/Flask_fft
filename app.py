from flask import Flask, render_template, request, jsonify
import make_fft
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio_data' in request.files:
        audio_file = request.files['audio_data']
        file_path = os.path.join('uploads', audio_file.filename)
        audio_file.save(file_path)

        # Process audio file
        waveform_data = make_fft.get_waveform(file_path)
        fft_data = make_fft.get_fft(file_path)

        return jsonify({'waveform': waveform_data, 'fft': fft_data})
    return jsonify({'error': 'No audio data received'})

if __name__ == '__main__':
    app.run(debug=True)
