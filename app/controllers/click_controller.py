from pyramid.view import view_config
from app.services.click_service import ClickService


class ClickController:
    def __init__(self, request):
        self.request = request
        self.click_service = ClickService()

    @view_config(route_name='create_click', renderer='json', request_method="POST")
    def create_click(self):
        click_data = self.request.json_body

        click = self.click_service.create_click(click_data)
        return {
            'status': 'success',
            'data': click.to_dict()
        }

