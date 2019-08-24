from abc import ABC


class IListen(ABC):
    def listen(self, voice_note_id):
        pass

    def get_errors(self):
        pass
