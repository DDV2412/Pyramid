from app.repositories.bounce_repository import BounceRepository
from app.models import Bounce


class BounceService:
    def __init__(self):
        self.brounce_repository = BounceRepository()

    def create_bounce(self, brounce_data: dict) -> Bounce:
        return self.brounce_repository.create_bounce(brounce_data)
