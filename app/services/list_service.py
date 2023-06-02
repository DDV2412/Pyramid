from typing import List

from app.repositories.list_repository import ListRepository
from app.models import List as ListContact


class ListService:
    def __init__(self):
        self.list_repository = ListRepository()

    def get_all_contacts(self) -> List[ListContact]:
        return self.list_repository.get_all_lists()

    def get_list_by_id(self, list_id: int) -> ListContact:
        return self.list_repository.get_list_by_id(list_id)

    def create_list(self, list_data: dict) -> ListContact:
        return self.list_repository.create_list(list_data)

    def update_list(self, list_id: int, list_data: dict) -> ListContact:
        return self.list_repository.update_list(list_id, list_data)

    def delete_list(self, list_id: int) -> bool:
        return self.list_repository.delete_list(list_id)
