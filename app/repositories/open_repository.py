import transaction

from app.models import DBSession, Open
from app.interfaces.open_interface import OpenInterface


class OpenRepository(OpenInterface):
    def __init__(self):
        self.session = DBSession

    def create_open(self, open_data: dict) -> Open:
        open_mail = Open(**open_data)
        self.session.add(open_mail)
        transaction.commit()
        open_mail = self.session.merge(open_mail)
        self.session.refresh(open_mail)
        return open_mail
