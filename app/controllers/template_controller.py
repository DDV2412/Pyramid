from pyramid.response import Response
from pyramid.view import view_config
from app.services.template_service import TemplateService
from app.schemas.template_schema import CreateTemplateSchema, validate_data, validate_update


class TemplateController:
    def __init__(self, request):
        self.request = request
        self.template_service = TemplateService()

    @view_config(route_name='get_all_templates', renderer='json', request_method="GET")
    def get_all_templates(self):
        templates = self.template_service.get_all_templates()
        return Response(json_body={
            'status': 'success',
            'data': [template.to_dict() for template in templates]
        }, status_code=200)

    @view_config(route_name='get_template_by_id', renderer='json', request_method="GET")
    def get_template_by_id(self):
        template_id = int(self.request.matchdict['id'])
        template = self.template_service.get_template_by_id(template_id)
        if template:
            return Response(json_body={
                'status': 'success',
                'data': template.to_dict()
            }, status_code=200)
        else:
            return Response(json_body={
                'status': 'error',
                'message': 'Template not found'
            }, status_code=404)

    @view_config(route_name='create_template', renderer='json', request_method="POST")
    def create_template(self):
        template_data = self.request.json_body
        schema = CreateTemplateSchema()
        is_valid, error = validate_data(template_data, schema)

        if not is_valid:
            return Response(json_body={'error': 'Validation Error', 'message': error}, status_code=400)

        mail = self.template_service.create_template(template_data)
        return Response(json_body={
            'status': 'success',
            'data': mail.to_dict()
        }, status_code=200)

    @view_config(route_name='update_template', renderer='json', request_method="PUT")
    def update_template(self):
        template_id = int(self.request.matchdict['id'])
        template_data = self.request.json_body
        is_valid, error = validate_update(template_data)

        if not is_valid:
            return Response(json_body={'error': 'Validation Error', 'message': error}, status_code=400)

        mail = self.template_service.update_template(template_id, template_data)
        if mail:
            return Response(json_body={
                'status': 'success',
                'data': mail.to_dict()
            }, status_code=200)
        else:
            return Response(json_body={
                'status': 'error',
                'message': 'Template not found'
            }, status_code=404)

    @view_config(route_name='delete_template', renderer='json', request_method="DELETE")
    def delete_template(self):
        template_id = int(self.request.matchdict['id'])
        success = self.template_service.delete_template(template_id)
        if success:
            return Response(json_body={
                'status': 'success',
                'message': 'Template deleted successfully'
            }, status_code=200)
        else:
            return Response(json_body={
                'status': 'error',
                'message': 'Template not found'
            }, status_code=404)
