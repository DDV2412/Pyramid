from app.repositories.open_repository import OpenRepository
from app.models import Open


class OpenService:
    def __init__(self):
        self.open_repository = OpenRepository()

    def create_open(self, open_data: dict) -> Open:
        return self.open_repository.create_open(open_data)
