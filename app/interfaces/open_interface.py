from abc import abstractmethod, ABC
from app.models import Open


class OpenInterface(ABC):

    @abstractmethod
    def create_open(self, open_data: dict) -> Open:
        pass
