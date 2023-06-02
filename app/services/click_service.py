from app.repositories.click_repository import ClickRepository
from app.models import Click


class ClickService:
    def __init__(self):
        self.click_repository = ClickRepository()

    def create_click(self, click_data: dict) -> Click:
        return self.click_repository.create_click(click_data)
