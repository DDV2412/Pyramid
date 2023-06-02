from typing import List

from app.repositories.mail_repository import MailRepository
from app.models import Mail


class MailService:
    def __init__(self):
        self.mail_repository = MailRepository()

    def get_all_mails(self) -> List[Mail]:
        return self.mail_repository.get_all_mails()

    def get_mail_by_id(self, mail_id: int) -> Mail:
        return self.mail_repository.get_mail_by_id(mail_id)

    def create_mail(self, mail_data: dict) -> Mail:
        return self.mail_repository.create_mail(mail_data)

    def update_mail(self, mail_id: int, mail_data: dict) -> Mail:
        return self.mail_repository.update_mail(mail_id, mail_data)

    def delete_mail(self, mail_id: int) -> bool:
        return self.mail_repository.delete_mail(mail_id)
