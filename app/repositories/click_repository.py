import transaction

from app.models import DBSession, Click
from app.interfaces.click_interface import ClickInterface


class ClickRepository(ClickInterface):
    def __init__(self):
        self.session = DBSession

    def create_click(self, click_data: dict) -> Click:
        click = Click(**click_data)
        self.session.add(click)
        transaction.commit()
        click = self.session.merge(click)
        self.session.refresh(click)
        return click
