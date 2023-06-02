from typing import List

from app.repositories.template_repository import TemplateRepository
from app.models import Template


class TemplateService:
    def __init__(self):
        self.template_repository = TemplateRepository()

    def get_all_templates(self) -> List[Template]:
        return self.template_repository.get_all_templates()

    def get_template_by_id(self, template_id: int) -> Template:
        return self.template_repository.get_template_by_id(template_id)

    def create_template(self, template_data: dict) -> Template:
        return self.template_repository.create_template(template_data)

    def update_template(self, template_id: int, template_data: dict) -> Template:
        return self.template_repository.update_template(template_id, template_data)

    def delete_template(self, template_id: int) -> bool:
        return self.template_repository.delete_template(template_id)
