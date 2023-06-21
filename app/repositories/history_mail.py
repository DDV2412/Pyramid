from datetime import datetime
from typing import List
import transaction
from app.models import DBSession, Mail, HistoryEmail


class HistoryRepository:
    def __init__(self):
        self.session = DBSession

    def get_history_by_mail(self, mail_campaign_id: int) -> List[HistoryEmail]:
        return self.session.query(HistoryEmail).filter(HistoryEmail.mail_campaign_id == mail_campaign_id).all()

    def create_history(self, history_data: dict) -> HistoryEmail:
        history = HistoryEmail(**history_data)
        self.session.add(history)
        transaction.commit()
        contact = self.session.merge(history)
        self.session.refresh(contact)
        return history
