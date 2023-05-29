from typing import List

from app.repositories.contact_repository import ContactRepository
from app.models import Contact


class ContactService:
    def __init__(self):
        self.contact_repository = ContactRepository()

    def get_all_contacts(self) -> List[Contact]:
        return self.contact_repository.get_all_contacts()

    def get_contact_by_id(self, contact_id: int) -> Contact:
        return self.contact_repository.get_contact_by_id(contact_id)

    def create_contact(self, contact_data: dict) -> Contact:
        return self.contact_repository.create_contact(contact_data)

    def update_contact(self, contact_id: int, contact_data: dict) -> Contact:
        return self.contact_repository.update_contact(contact_id, contact_data)

    def delete_contact(self, contact_id: int) -> bool:
        return self.contact_repository.delete_contact(contact_id)

    def import_contacts(self, file_path: str) -> List[Contact]:
        return self.contact_repository.import_contacts(file_path)
