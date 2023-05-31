from typing import List

import transaction

from app.models import DBSession, Contact
from app.interfaces.contact_interface import ContactInterface


class ContactRepository(ContactInterface):
    def __init__(self):
        self.session = DBSession

    def get_all_contacts(self) -> List[Contact]:
        return self.session.query(Contact).all()

    def get_contact_by_id(self, contact_id: int) -> Contact:
        return self.session.query(Contact).get(contact_id)

    def create_contact(self, contact_data: dict) -> Contact:
        contact = Contact(**contact_data)
        self.session.add(contact)
        transaction.commit()
        contact = self.session.merge(contact)
        self.session.refresh(contact)
        return contact

    def update_contact(self, contact_id: int, contact_data: dict) -> Contact | None:
        contact = self.get_contact_by_id(contact_id)
        if contact:
            for key, value in contact_data.items():
                setattr(contact, key, value)
            transaction.commit()
            contact = self.session.merge(contact)
            self.session.refresh(contact)
            return contact
        return None

    def delete_contact(self, contact_id: int) -> bool:
        contact = self.get_contact_by_id(contact_id)
        if contact:
            self.session.delete(contact)
            transaction.commit()
            return True
        return False

    def import_contacts(self, file_path: str) -> List[Contact]:
        contacts = []
        with open(file_path, 'r') as file:
            for line in file:
                contact_data = line.strip().split(',')
                contact = Contact(*contact_data)
                self.session.add(contact)
                contacts.append(contact)
            transaction.commit()
        return contacts
