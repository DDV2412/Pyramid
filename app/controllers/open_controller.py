from pyramid.view import view_config
from app.services.open_service import OpenService


class OpenController:
    def __init__(self, request):
        self.request = request
        self.open_service = OpenService()

    @view_config(route_name='create_open', renderer='json', request_method="POST")
    def create_open(self):
        open_data = self.request.json_body

        open_mail = self.open_service.create_open(open_data)
        return {
            'status': 'success',
            'data': open_mail.to_dict()
        }

