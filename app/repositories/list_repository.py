from typing import List

import transaction

from app.models import DBSession, List as ListContact
from app.interfaces.list_interface import ListInterface


class ListRepository(ListInterface):
    def __init__(self):
        self.session = DBSession

    def get_all_lists(self) -> List[ListContact]:
        return self.session.query(ListContact).all()

    def get_list_by_id(self, list_id: int) -> ListContact:
        return self.session.query(ListContact).get(list_id)

    def create_list(self, list_data: dict) -> ListContact:
        contact = ListContact(**list_data)
        self.session.add(contact)
        transaction.commit()
        contact = self.session.merge(contact)
        self.session.refresh(contact)
        return contact

    def update_list(self, list_id: int, list_data: dict) -> ListContact | None:
        check_list = self.get_list_by_id(list_id)
        if check_list:
            for key, value in list_data.items():
                setattr(check_list, key, value)
            transaction.commit()
            check_list = self.session.merge(check_list)
            self.session.refresh(check_list)
            return check_list
        return None

    def delete_list(self, list_id: int) -> bool:
        list_data = self.get_list_by_id(list_id)
        if list_data:
            self.session.delete(list_data)
            transaction.commit()
            return True
        return False
