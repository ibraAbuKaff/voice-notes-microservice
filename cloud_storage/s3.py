from cloud_storage.base_cloud_storage import BaseCloudStorage
import boto3
from config import Config


class S3(BaseCloudStorage):

    def __init__(self):
        super().__init__()
        self.client = boto3.client('s3', aws_access_key_id=Config.get('AWS_S3_ACCESS_KEY'),
                                   aws_secret_access_key=Config.get('AWS_S3_SECRET_KEY'),
                                   region_name=Config.get('S3_REGION_NAME'))

    def put(self, filename):
        bucket_name = Config.get('S3_BUCKET_NAME')
        self.client.upload_file('{}/{}'.format(Config.get('AUDIO_TEMP_UPLOAD_FOLDER'), filename), bucket_name, filename,
                                {'ACL': 'public-read'})

    def get(self, file_key):
        return 'http://{}.s3.amazonaws.com/{}'.format(Config.get('S3_BUCKET_NAME'), file_key)
