from abc import abstractmethod, ABC
from typing import List

from app.models import List as ListContact


class ListInterface(ABC):
    @abstractmethod
    def get_all_lists(self) -> List[ListContact]:
        pass

    @abstractmethod
    def get_list_by_id(self, contact_id: int) -> ListContact:
        pass

    @abstractmethod
    def create_list(self, contact_data: dict) -> ListContact:
        pass

    @abstractmethod
    def update_list(self, contact_id: int, contact_data: dict) -> ListContact:
        pass

    @abstractmethod
    def delete_list(self, contact_id: int) -> bool:
        pass
