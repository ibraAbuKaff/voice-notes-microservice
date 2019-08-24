import os
from bson.json_util import dumps
from flask import Response


class Helpers:

    @staticmethod
    def create_dir_if_not_exists(file_path):
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        return file_path

    @staticmethod
    def respond_with(json_as_dict, status_code=200):
        return Response(dumps(json_as_dict), mimetype='application/json'), status_code
