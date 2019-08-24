import os
from uuid import uuid1
from flask import current_app as app
from voicenote.upload.base_upload import IUpload
from config import Config
from werkzeug.utils import secure_filename
from common.helpers import Helpers
from cloud_storage.s3 import S3
from models.voice_note_model import VoiceNoteModel
from models.redis_cache import RedisCache


class AudioUploader(IUpload):
    def __init__(self, pilot_id):
        self.__temp_audio_folder = ''
        self.__errors = []
        self.__set_upload_config()

        self.pilot_id = pilot_id

    def upload(self, audio_file):
        try:
            file_key_uuid = self.__save_locally(audio_file)
            if file_key_uuid == '':
                return ''

            S3().put(file_key_uuid)
            AudioUploader.delete_temp_file(file_key_uuid)

            VoiceNoteModel().insert({
                'pilot_id': self.pilot_id,
                'voice_note_key': file_key_uuid
            })

            try:
                RedisCache(self.pilot_id).put(file_key_uuid)
            except Exception:
                pass

            return file_key_uuid
        except Exception as e:
            self.__errors.append(str(e))
            return ''

    def get_errors(self):
        return self.__errors

    def __save_locally(self, audio_file):
        if not self.__can_upload(audio_file):
            return ''

        try:
            file_name = AudioUploader.__generate_new_file_name(audio_file)
            audio_file.save(os.path.join(self.__temp_audio_folder, file_name))

            return file_name
        except Exception as e:
            self.__errors.append(str(e))

    def __can_upload(self, audio_file):
        if AudioUploader.__is_empty_file(audio_file):
            self.__errors.append('file is empty')
            return False

        if not AudioUploader.__allowed_file(audio_file.filename):
            self.__errors.append('file type is not allowed, only the following are allowed :{}'.format(
                Config.get('AUDIO_ALLOWED_EXTENSIONS')))
            return False

        return True

    @staticmethod
    def __allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.get('AUDIO_ALLOWED_EXTENSIONS').split(
            ',')

    @staticmethod
    def __is_empty_file(audio_file):
        return audio_file == {}

    @staticmethod
    def delete_temp_file(file_key_uuid):
        os.remove("{}/{}".format(Config.get('AUDIO_TEMP_UPLOAD_FOLDER'), file_key_uuid))

    def __set_upload_config(self):
        app.config['MAX_CONTENT_LENGTH'] = int(Config.get('AUDIO_AUDIO_SIZE_MB')) * 1024 * 1024
        app.config['UPLOAD_FOLDER'] = self.__temp_audio_folder = Helpers.create_dir_if_not_exists(
            Config.get('AUDIO_TEMP_UPLOAD_FOLDER'))

    @staticmethod
    def __generate_new_file_name(audio_file):
        name, ext = os.path.splitext(secure_filename(audio_file.filename))
        new_file_name = '{}{}'.format(uuid1(), ext)

        return new_file_name
