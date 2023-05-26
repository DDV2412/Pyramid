from typing import List
from app.interfaces.contact_interface import ContactInterface
from app.models import Contact, StatusContact
from sqlalchemy.orm import Session


class ContactRepository(ContactInterface):
    def __init__(self, session: Session):
        self.session = session

    def get_contact_by_id(self, contact_id: int) -> Contact:
        contact = self.session.query(Contact).get(contact_id)
        return contact

    def create_contact(self, contact_data: dict) -> Contact:
        contact = Contact(**contact_data)
        self.session.add(contact)
        self.session.commit()
        return contact

    def update_contact(self, contact_data: dict, contact_id: int) -> Contact:
        contact = self.session.query(Contact).get(contact_id)
        if contact:
            if 'status' in contact_data:
                contact.status = StatusContact(contact_data['status'])
            for key, value in contact_data.items():
                setattr(contact, key, value)
            self.session.commit()

        return contact

    def delete_contact(self, contact_id: int) -> bool:
        contact = self.session.query(Contact).get(contact_id)
        if contact:
            self.session.delete(contact)
            self.session.commit()
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
                self.session.commit()
        return contacts
