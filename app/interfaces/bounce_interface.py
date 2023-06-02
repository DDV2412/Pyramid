from abc import abstractmethod, ABC
from app.models import Bounce


class BounceInterface(ABC):

    @abstractmethod
    def create_bounce(self, brounce_data: dict) -> Bounce:
        pass
