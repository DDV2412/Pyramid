from abc import abstractmethod, ABC
from app.models import Click


class ClickInterface(ABC):

    @abstractmethod
    def create_click(self, click_data: dict) -> Click:
        pass
