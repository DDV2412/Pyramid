from typing import List

import transaction

from app.models import DBSession, Template
from app.interfaces.template_interface import TemplateInterface


class TemplateRepository(TemplateInterface):
    def __init__(self):
        self.session = DBSession

    def get_all_templates(self) -> List[Template]:
        return self.session.query(Template).all()

    def get_template_by_id(self, template_id: int) -> Template:
        return self.session.query(Template).get(template_id)

    def create_template(self, template_data: dict) -> Template:
        template = Template(**template_data)
        self.session.add(template)
        transaction.commit()
        template = self.session.merge(template)
        self.session.refresh(template)
        return template

    def update_template(self, template_id: int, template_data: dict) -> Template | None:
        template = self.get_template_by_id(template_id)
        if template:
            for key, value in template_data.items():
                setattr(template, key, value)
            transaction.commit()
            template = self.session.merge(template)
            self.session.refresh(template)
            return template
        return None

    def delete_template(self, template_id: int) -> bool:
        template = self.get_template_by_id(template_id)
        if template:
            self.session.delete(template)
            transaction.commit()
            return True
        return False
