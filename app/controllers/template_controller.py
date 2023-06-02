from pyramid.view import view_config
from app.services.template_service import TemplateService
from app.schemas.template_schema import CreateTemplateSchema, UpdateTemplateSchema, validate_data, validate_update


class TemplateController:
    def __init__(self, request):
        self.request = request
        self.template_service = TemplateService()

    @view_config(route_name='get_all_templates', renderer='json', request_method="GET")
    def get_all_templates(self):
        templates = self.template_service.get_all_templates()
        return {
            'status': 'success',
            'data': [template.to_dict() for template in templates]
        }

    @view_config(route_name='get_template_by_id', renderer='json', request_method="GET")
    def get_template_by_id(self):
        template_id = int(self.request.matchdict['id'])
        template = self.template_service.get_template_by_id(template_id)
        if template:
            return {
                'status': 'success',
                'data': template.to_dict()
            }
        else:
            return {
                'status': 'error',
                'message': 'List not found'
            }

    @view_config(route_name='create_template', renderer='json', request_method="POST")
    def create_template(self):
        template_data = self.request.json_body
        schema = CreateTemplateSchema()
        is_valid, error = validate_data(template_data, schema)

        if not is_valid:
            return {'error': 'Validation Error', 'message': error}

        mail = self.template_service.create_template(template_data)
        return {
            'status': 'success',
            'data': mail.to_dict()
        }

    @view_config(route_name='update_template', renderer='json', request_method="PUT")
    def update_template(self):
        template_id = int(self.request.matchdict['id'])
        template_data = self.request.json_body
        schema = UpdateTemplateSchema()
        is_valid, error = validate_update(template_data, schema)

        if not is_valid:
            return {'error': 'Validation Error', 'message': error}

        mail = self.template_service.update_template(template_id, template_data)
        if mail:
            return {
                'status': 'success',
                'data': mail.to_dict()
            }
        else:
            return {
                'status': 'error',
                'message': 'List not found'
            }

    @view_config(route_name='delete_template', renderer='json', request_method="DELETE")
    def delete_template(self):
        template_id = int(self.request.matchdict['id'])
        success = self.template_service.delete_template(template_id)
        if success:
            return {
                'status': 'success',
                'message': 'List deleted successfully'
            }
        else:
            return {
                'status': 'error',
                'message': 'List not found'
            }
