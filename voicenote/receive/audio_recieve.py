from voicenote.receive.base_receive import IReceive
from models.redis_cache import RedisCache
from models.voice_note_model import VoiceNoteModel


class AudioReceive(IReceive):
    def __init__(self, pilot_id):
        self.__pilot_id = pilot_id
        self.__errors = []

    def receive(self):
        try:
            result = RedisCache(self.__pilot_id).get()
        except Exception as e:
            result = []
            self.__errors.append(str(e))

        if len(result) == 0:
            result = VoiceNoteModel().get_by_pilot_id(self.__pilot_id)

        return result

    def get_errors(self):
        return self.__errors
