from datetime import datetime
from typing import List

import transaction

from app.models import DBSession, Contact, List as ListContact
from app.interfaces.contact_interface import ContactInterface


class ContactRepository(ContactInterface):
    def __init__(self):
        self.session = DBSession

    def get_all_contacts(self) -> List[Contact]:
        return self.session.query(Contact).all()

    def get_contact_by_id(self, contact_id: int) -> Contact:
        return self.session.query(Contact).get(contact_id)

    def create_contact(self, contact_data: dict) -> Contact:
        list_ids = contact_data.pop('lists', [])
        contact = Contact(**contact_data)
        lists = self.session.query(ListContact).filter(ListContact.id.in_(list_ids)).all()
        contact.lists = lists
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
                contact.updated_at = datetime.utcnow()
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

    def import_contacts(self, contact_data: List[dict]) -> bool:
        for data in contact_data:
            contact = Contact(**data)
            self.session.add(contact)
        transaction.commit()

        return True
