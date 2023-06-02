from abc import abstractmethod, ABC
from typing import List

from app.models import Template


class TemplateInterface(ABC):
    @abstractmethod
    def get_all_templates(self) -> List[Template]:
        pass

    @abstractmethod
    def get_template_by_id(self, template_id: int) -> Template:
        pass

    @abstractmethod
    def create_template(self, template_data: dict) -> Template:
        pass

    @abstractmethod
    def update_template(self, template_id: int, template_data: dict) -> Template:
        pass

    @abstractmethod
    def delete_template(self, template_id: int) -> bool:
        pass
