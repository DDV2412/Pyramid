from abc import abstractmethod, ABC

from app.models import List


class ListInterface(ABC):

    @abstractmethod
    def get_list_by_id(self, list_id: int) -> List:
        pass

    @abstractmethod
    def create_list(self, list_data: dict) -> List:
        pass

    @abstractmethod
    def update_list(self, list_data: dict, list_id: int) -> List:
        pass

    @abstractmethod
    def delete_list(self, list_id: int) -> bool:
        pass

