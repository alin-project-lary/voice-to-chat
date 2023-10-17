from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # Import the CORS module
import openai
import io
from pydub import AudioSegment

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in your Flask app

# Configuration (Replace with your OpenAI API key)
OPENAI_API_KEY = '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'

def convert_blob_to_mp3(blob):
    # Load blob into pydub
    audio = AudioSegment.from_file(blob)

    # Convert to MP3
    mp3_buffer = io.BytesIO()
    audio.export(mp3_buffer, format="mp3")
    mp3_buffer.seek(0)
    return mp3_buffer

@app.route('/voice_to_chat', methods=['POST'])

def voice_to_chat():

    try: 
        openai.api_key = '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'

        x = request.files['file']

        transcript = openai.Audio.translate("whisper-1", convert_blob_to_mp3(x), response_format="vtt")

        print(transcript)
    except Exception as e:
        print(e)
        transcript = ''

    return jsonify(text=transcript)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
