from pyramid.response import Response
from pyramid.view import view_config
from app.services.bounce_service import BounceService


class OpenController:
    def __init__(self, request):
        self.request = request
        self.bounce_service = BounceService()

    @view_config(route_name='create_bounce', renderer='json', request_method="POST")
    def create_bounce(self):
        bounce_data = self.request.json_body

        bounce = self.bounce_service.create_bounce(bounce_data)

        return Response(json_body={
            'status': 'success',
            'data': bounce.to_dict()
        }, status_code=200)

