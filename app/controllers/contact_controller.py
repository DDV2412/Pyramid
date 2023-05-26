from app.services.contact_service import ContactService
from app.schema.contact_schema import CreateContactSchema, validate_data, UpdateContactSchema, validate_update
from pyramid.response import Response


class ContactController:
    def __init__(self, contact_service: ContactService):
        self.contact_service = contact_service

    def get_contact_by_id(self, request):
        contact_id = request.matchdict.get('contact_id')
        contact = self.contact_service.get_contact_by_id(contact_id)
        if contact:
            # Mengembalikan response sukses dengan data kontak
            return Response(json={
                'status': 'success',
                'data': {
                    'id': contact.id,
                    'email': contact.email,
                    'firstname': contact.firstname,
                    'lastname': contact.lastname,
                    'status': contact.status
                }
            })
        else:
            # Mengembalikan response error jika kontak tidak ditemukan
            return Response(json={
                'status': 'error',
                'message': 'Contact not found'
            })

    def create_contact(self, request):
        contact_data = request.json
        schema = CreateContactSchema()
        is_valid, error = validate_data(contact_data, schema)

        if is_valid:
            contact = self.contact_service.create_contact(contact_data)
            # Mengembalikan response sukses dengan data kontak yang baru dibuat
            return Response(json={
                'status': 'success',
                'data': {
                    'id': contact.id,
                    'email': contact.email,
                    'firstname': contact.firstname,
                    'lastname': contact.lastname,
                    'status': contact.status
                }
            })

        else:
            return Response(json={'error': 'Validation Error', 'message': error}, status=400)

    def update_contact(self, request):
        contact_id = request.matchdict.get('contact_id')
        contact_data = request.json
        schema = UpdateContactSchema()
        is_valid, error = validate_update(contact_data, schema)

        if not is_valid:
            return Response(json={'error': 'Validation Error', 'message': error}, status=400)

        contact = self.contact_service.update_contact(contact_data, contact_id)

        if contact:
            # Mengembalikan response sukses dengan data kontak yang telah diperbarui
            return Response(json={
                'status': 'success',
                'data': {
                    'id': contact.id,
                    'email': contact.email,
                    'firstname': contact.firstname,
                    'lastname': contact.lastname,
                    'status': contact.status
                }
            })
        else:
            # Mengembalikan response error jika kontak tidak ditemukan
            return Response(json={
                'status': 'error',
                'message': 'Contact not found'
            })

    def delete_contact(self, request):
        contact_id = request.matchdict.get('contact_id')
        success = self.contact_service.delete_contact(contact_id)
        if success:
            # Mengembalikan response sukses jika kontak berhasil dihapus
            return Response(json={
                'status': 'success',
                'message': 'Contact deleted successfully'
            })
        else:
            # Mengembalikan response error jika kontak tidak ditemukan
            return Response(json={
                'status': 'error',
                'message': 'Contact not found'
            })

    def import_contacts(self, request):
        file_path = request.json.get('file_path')
        contacts = self.contact_service.import_contacts(file_path)
        # Mengembalikan response sukses dengan data kontak yang berhasil diimpor
        return Response(json={
            'status': 'success',
            'data': contacts
        })
