from abc import ABC


class IReceive(ABC):
    def receive(self):
        pass

    def get_errors(self):
        pass
