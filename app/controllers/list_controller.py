from pyramid.view import view_config
from app.services.list_service import ListService
from app.schemas.list_schema import CreateListSchema, validate_data, validate_update
from pyramid.response import Response


class ListController:
    def __init__(self, request):
        self.request = request
        self.list_service = ListService()

    @view_config(route_name='get_all_list', renderer='json', request_method="GET")
    def get_all_list(self):
        lists = self.list_service.get_all_contacts()
        return Response(
            json_body={
                'status': 'success',
                'data': [list_data.to_dict() for list_data in lists]
            },
            status_code=200
        )

    @view_config(route_name='get_list_by_id', renderer='json', request_method="GET")
    def get_list_by_id(self):
        list_id = int(self.request.matchdict['id'])
        list_data = self.list_service.get_list_by_id(list_id)
        if list_data:
            return Response(json_body={
                'status': 'success',
                'data': list_data.to_dict()
            }, status_code=200)
        else:
            return Response(json_body={
                'status': 'error',
                'message': 'List not found'
            }, status_code=404)

    @view_config(route_name='create_list', renderer='json', request_method="POST")
    def create_list(self):
        list_data = self.request.json_body
        schema = CreateListSchema()
        is_valid, error = validate_data(list_data, schema)

        if not is_valid:
            return Response(json_body={
                'error': 'Validation Error', 'message': error
            }, status_code=400)

        list_new = self.list_service.create_list(list_data)
        return Response(json_body={
            'status': 'success',
            'data': list_new.to_dict()
        }, status_code=200)

    @view_config(route_name='update_list', renderer='json', request_method="PUT")
    def update_list(self):
        list_id = int(self.request.matchdict['id'])
        list_data = self.request.json_body
        is_valid, error = validate_update(list_data)

        if not is_valid:
            return Response(json_body={
                'error': 'Validation Error', 'message': error
            }, status_code=400)

        list_update = self.list_service.update_list(list_id, list_data)
        if list_update:
            return Response(json_body={
                'status': 'success',
                'data': list_update.to_dict()
            }, status_code=200)
        else:
            return Response(json_body={
                'status': 'error',
                'message': 'List not found'
            }, status_code=404)

    @view_config(route_name='delete_list', renderer='json', request_method="DELETE")
    def delete_list(self):
        list_id = int(self.request.matchdict['id'])
        success = self.list_service.delete_list(list_id)
        if success:
            return Response(json_body={
                'status': 'success',
                'message': 'List deleted successfully'
            }, status_code=200)
        else:
            return Response(json_body={
                'status': 'error',
                'message': 'List not found'
            }, status_code=404)
