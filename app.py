from flask import Flask, request
from common.helpers import Helpers
from voicenote.voice_note import VoiceNote
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/v1/pilots/<int:pilot_id>/voicenotes", methods=['POST'])
def upload(pilot_id):
    audio_file = request.files['file'] if 'file' in request.files else {}
    voice_note_instance = VoiceNote(pilot_id)
    return Helpers.respond_with({
        'voice_note_id': voice_note_instance.upload(audio_file),
        'errors': voice_note_instance.get_errors()
    })


@app.route("/api/v1/pilots/<int:pilot_id>/voicenotes", methods=['GET'])
def receive(pilot_id):
    voice_note_instance = VoiceNote(pilot_id)

    return Helpers.respond_with({
        'voice_note_ids': voice_note_instance.receive(),
        'errors': voice_note_instance.get_errors()
    })


@app.route("/api/v1/pilots/<int:pilot_id>/voicenotes/<string:voice_note_id>", methods=['GET'])
def listen(voice_note_id, pilot_id):
    voice_note_instance = VoiceNote(pilot_id)

    return Helpers.respond_with({
        'voice_note_url': voice_note_instance.listen(voice_note_id),
        'errors': voice_note_instance.get_errors()
    })


@app.route("/")
def hello():
    return "Voice note micro-service"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
