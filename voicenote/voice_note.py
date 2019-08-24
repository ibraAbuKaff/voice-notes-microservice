from voicenote.upload.audio_uploader import AudioUploader
from voicenote.receive.audio_recieve import AudioReceive
from voicenote.listen.audio_listen import AudioListen


class VoiceNote:
    def __init__(self, pilot_id=None):
        self.__pilot_id = pilot_id
        self.__errors = []

    def upload(self, audio_file):
        audio_uploader = AudioUploader(self.__pilot_id)
        generated_audio_file = audio_uploader.upload(audio_file)

        self.__errors = audio_uploader.get_errors()
        return generated_audio_file

    def receive(self):
        audio_receive = AudioReceive(self.__pilot_id)
        list_of_voice_notes = audio_receive.receive()

        self.__errors = audio_receive.get_errors()
        return list_of_voice_notes

    def listen(self, voice_note_id):
        audio_listen = AudioListen(self.__pilot_id)
        url = audio_listen.listen(voice_note_id)

        self.__errors = audio_listen.get_errors()
        return url

    def get_errors(self):
        return self.__errors
