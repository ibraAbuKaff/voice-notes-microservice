from abc import ABC


class IUpload(ABC):
    def upload(self, file):
        pass

    def get_errors(self):
        pass
