from typing import List

import transaction

from app.models import DBSession, Mail
from app.interfaces.mail_interface import MailInterface


class MailRepository(MailInterface):
    def __init__(self):
        self.session = DBSession

    def get_all_mails(self) -> List[Mail]:
        return self.session.query(Mail).all()

    def get_mail_by_id(self, mail_id: int) -> Mail:
        return self.session.query(Mail).get(mail_id)

    def create_mail(self, mail_data: dict) -> Mail:
        mail = Mail(**mail_data)
        self.session.add(mail)
        transaction.commit()
        mail = self.session.merge(mail)
        self.session.refresh(mail)
        return mail

    def update_mail(self, mail_id: int, mail_data: dict) -> Mail | None:
        mail = self.get_mail_by_id(mail_id)
        if mail:
            for key, value in mail_data.items():
                setattr(mail, key, value)
            transaction.commit()
            mail = self.session.merge(mail)
            self.session.refresh(mail)
            return mail
        return None

    def delete_mail(self, mail_id: int) -> bool:
        mail_data = self.get_mail_by_id(mail_id)
        if mail_data:
            self.session.delete(mail_data)
            transaction.commit()
            return True
        return False
