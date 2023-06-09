from pyramid.response import Response
from pyramid.view import view_config
from app.services.contact_service import ContactService
from app.schemas.contact_schema import CreateContactSchema, validate_data, validate_update
from app.utils.error_handlers import not_found, internal_server_error


class ContactController:
    def __init__(self, request):
        self.request = request
        self.contact_service = ContactService()

    @view_config(route_name='get_all_contact', renderer='json', request_method="GET")
    def get_all_contact(self):
        contacts = self.contact_service.get_all_contacts()
        return Response(json_body={
            'status': 'success',
            'data': [contact.to_dict() for contact in contacts]
        }, status_code=200)

    @view_config(route_name='get_contact_by_id', renderer='json', request_method="GET")
    def get_contact_by_id(self):
        try:
            contact_id = int(self.request.matchdict['id'])
            contact = self.contact_service.get_contact_by_id(contact_id)
            if contact:
                return Response(json_body={
                    'status': 'success',
                    'data': contact.to_dict()
                }, status_code=200)
            else:
                return not_found(self)
        except Exception:
            raise internal_server_error(self)

    @view_config(route_name='create_contact', renderer='json', request_method="POST")
    def create_contact(self):
        contact_data = self.request.json_body
        schema = CreateContactSchema()
        is_valid, error = validate_data(contact_data, schema)

        if not is_valid:
            return Response(json_body={'error': 'Validation Error', 'message': error}, status_code=400)

        contact = self.contact_service.create_contact(contact_data)
        return Response(json_body={
            'status': 'success',
            'data': contact.to_dict()
        }, status_code=200)

    @view_config(route_name='update_contact', renderer='json', request_method="PUT")
    def update_contact(self):
        contact_id = int(self.request.matchdict['id'])
        contact_data = self.request.json_body
        is_valid, error = validate_update(contact_data)

        if not is_valid:
            return Response(json_body={'error': 'Validation Error', 'message': error}, status_code=400)

        contact = self.contact_service.update_contact(contact_id, contact_data)
        if contact:
            return Response(json_body={
                'status': 'success',
                'data': contact.to_dict()
            }, status_code=200)
        else:
            return Response(json_body={
                'status': 'error',
                'message': 'Contact not found'
            }, status_code=404)

    @view_config(route_name='delete_contact', renderer='json', request_method="DELETE")
    def delete_contact(self):
        contact_id = int(self.request.matchdict['id'])
        success = self.contact_service.delete_contact(contact_id)
        if success:
            return Response(json_body={
                'status': 'success',
                'message': 'Contact deleted successfully'
            }, status_code=200)
        else:
            return Response(json_body={
                'status': 'error',
                'message': 'Contact not found'
            }, status_code=404)

    @view_config(route_name='import_contacts', renderer='json', request_method="POST")
    def import_contacts(self):
        contacts = self.request.json_body
        contact = self.contact_service.import_contacts(contacts)

        if contact:
            return Response(json_body={
                'status': 'success',
                'data': 'Contact imported successfully'
            }, status_code=200)
        else:
            return internal_server_error(self)

