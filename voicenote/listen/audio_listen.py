from voicenote.listen.base_listen import IListen
from models.voice_note_model import VoiceNoteModel
from cloud_storage.s3 import S3


class AudioListen(IListen):

    def __init__(self, pilot_id):
        self.__pilot_id = pilot_id
        self.__errors = []

    def listen(self, voice_note_id):
        if VoiceNoteModel().pilot_has_voice_note(self.__pilot_id, voice_note_id):
            url = S3().get(voice_note_id)
            return url

        self.__errors.append("Pilot with id {} does not have {}".format(self.__pilot_id, voice_note_id))

    def get_errors(self):
        return self.__errors
