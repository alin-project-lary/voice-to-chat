from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # Import the CORS module
import openai
import io
from pydub import AudioSegment
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in your Flask app

# Configuration (Replace with your OpenAI API key)
OPENAI_API_KEY = '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'


@app.route('/voice_to_chat', methods=['POST'])

def voice_to_chat():

    try: 
        raw_data = request.get_data()

        # Assuming the raw_data is in JSON format, you can decode it to a Python dictionary
        json_data = raw_data.decode('utf-8')
        data = json.loads(json_data)

        # Extract 'url' parameter from the JSON data
        url = data.get('url', '')
        openai.api_key = OPENAI_API_KEY

        with requests.get(url) as response:
            with io.BytesIO(response.content) as file:
                file.name = "audio.m4a"
                transcript = openai.Audio.transcribe(
                    file=file,
                    model="whisper-1",
                    response_format="verbose_json",
                )
                print(transcript)

    except Exception as e:
        print(e)
        transcript = ''

    return jsonify(text=transcript)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
