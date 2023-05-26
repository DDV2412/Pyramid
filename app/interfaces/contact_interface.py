from abc import abstractmethod, ABC
from typing import List

from app.models import Contact


class ContactInterface(ABC):

    @abstractmethod
    def get_contact_by_id(self, contact_id: int) -> Contact:
        pass

    @abstractmethod
    def create_contact(self, contact_data: dict) -> Contact:
        pass

    @abstractmethod
    def update_contact(self, contact_data: dict, contact_id: int) -> Contact:
        pass

    @abstractmethod
    def delete_contact(self, contact_id: int) -> bool:
        pass

    @abstractmethod
    def import_contacts(self, file_path: str) -> List[Contact]:
        pass
