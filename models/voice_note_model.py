from flask import current_app as app
from config import Config
from flask_pymongo import PyMongo
import datetime


class VoiceNoteModel(object):
    COLLECTION = 'voice_notes'

    def __init__(self):
        app.config["MONGO_URI"] = Config.get('MONGO_DATABASE_CONNECTION')
        self.collection = PyMongo(app).db[VoiceNoteModel.COLLECTION]

    def insert(self, data):
        data['created_at'] = datetime.datetime.utcnow()
        data['updated_at'] = datetime.datetime.utcnow()
        self.collection.insert_one(data)

    def get_by_pilot_id(self, pilot_id):
        result = self.collection.find({"pilot_id": pilot_id})
        voice_note_keys = []
        for document in result:
            voice_note_keys.append(document['voice_note_key'])

        return voice_note_keys

    def pilot_has_voice_note(self, pilot_id, voice_note_key):
        result = self.collection.find({"voice_note_key": voice_note_key, "pilot_id": pilot_id})

        return True if result.count() == 1 else False
