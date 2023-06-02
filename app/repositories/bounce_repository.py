import transaction

from app.models import DBSession, Bounce
from app.interfaces.bounce_interface import BounceInterface


class BounceRepository(BounceInterface):
    def __init__(self):
        self.session = DBSession

    def create_bounce(self, brounce_data: dict) -> Bounce:
        brounce = Bounce(**brounce_data)
        self.session.add(brounce)
        transaction.commit()
        brounce = self.session.merge(brounce)
        self.session.refresh(brounce)
        return brounce
