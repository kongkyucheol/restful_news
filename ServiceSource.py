from abc import *


class ServiceData:
    httpUri = ""
    thumbnailUri = ""
    title = ""
    description = ""
    datetime = ""
    fromSource = ""

    def __str__(self):
        return self.title


class ServiceSource(metaclass=ABCMeta):
    @abstractmethod
    def request(self):
        pass
