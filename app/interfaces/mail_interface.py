from abc import abstractmethod, ABC
from typing import List

from app.models import Mail


class MailInterface(ABC):
    @abstractmethod
    def get_all_mails(self) -> List[Mail]:
        pass

    @abstractmethod
    def get_mail_by_id(self, mail_id: int) -> Mail:
        pass

    @abstractmethod
    def create_mail(self, mail_data: dict) -> Mail:
        pass

    @abstractmethod
    def update_mail(self, mail_id: int, mail_data: dict) -> Mail:
        pass

    @abstractmethod
    def delete_mail(self, mail_id: int) -> bool:
        pass
