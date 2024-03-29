import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '.')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


class Config:

    @staticmethod
    def get(env_key):
        return os.getenv(env_key)
