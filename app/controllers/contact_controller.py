from pyramid.view import view_config
from app.services.contact_service import ContactService
from app.schemas.contact_schema import CreateContactSchema, UpdateContactSchema, validate_data


class ContactController:
    def __init__(self, request):
        self.request = request
        self.contact_service = ContactService()

    @view_config(route_name='get_all_contact', renderer='json', request_method="GET")
    def get_all_contact(self):
        contacts = self.contact_service.get_all_contacts()
        return {
            'status': 'success',
            'data': contacts
        }

    @view_config(route_name='get_contact_by_id', renderer='json', request_method="GET")
    def get_contact_by_id(self):
        contact_id = int(self.request.matchdict['id'])
        contact = self.contact_service.get_contact_by_id(contact_id)
        if contact:
            return {
                'status': 'success',
                'data': contact
            }
        else:
            return {
                'status': 'error',
                'message': 'Contact not found'
            }

    @view_config(route_name='create_contact', renderer='json', request_method="POST")
    def create_contact(self):
        contact_data = self.request.json_body
        schema = CreateContactSchema()
        is_valid, error = validate_data(contact_data, schema)

        if not is_valid:
            return {'error': 'Validation Error', 'message': error}

        contact = self.contact_service.create_contact(contact_data)
        return {
            'status': 'success',
            'data': contact
        }

    @view_config(route_name='update_contact', renderer='json', request_method="PUT")
    def update_contact(self):
        contact_id = int(self.request.matchdict['id'])
        contact_data = self.request.json_body
        schema = UpdateContactSchema()
        is_valid, error = validate_data(contact_data, schema)

        if not is_valid:
            return {'error': 'Validation Error', 'message': error}

        contact = self.contact_service.update_contact(contact_id, contact_data)
        if contact:
            return {
                'status': 'success',
                'data': contact
            }
        else:
            return {
                'status': 'error',
                'message': 'Contact not found'
            }

    @view_config(route_name='delete_contact', renderer='json', request_method="DELETE")
    def delete_contact(self):
        contact_id = int(self.request.matchdict['id'])
        success = self.contact_service.delete_contact(contact_id)
        if success:
            return {
                'status': 'success',
                'message': 'Contact deleted successfully'
            }
        else:
            return {
                'status': 'error',
                'message': 'Contact not found'
            }

    @view_config(route_name='import_contacts', renderer='json', request_method="POST")
    def import_contacts(self):
        file_path = self.request.json_body.get('file_path')
        contacts = self.contact_service.import_contacts(file_path)
        return {
            'status': 'success',
            'data': contacts
        }
