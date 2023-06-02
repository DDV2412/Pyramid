from pyramid.view import view_config
from app.services.mail_service import MailService
from app.schemas.mail_schema import CreateMailSchema, UpdateMailSchema, validate_data, validate_update


class MailController:
    def __init__(self, request):
        self.request = request
        self.mail_service = MailService()

    @view_config(route_name='get_all_mails', renderer='json', request_method="GET")
    def get_all_mails(self):
        mails = self.mail_service.get_all_mails()
        return {
            'status': 'success',
            'data': [mail.to_dict() for mail in mails]
        }

    @view_config(route_name='get_mail_by_id', renderer='json', request_method="GET")
    def get_mail_by_id(self):
        mail_id = int(self.request.matchdict['id'])
        mail = self.mail_service.get_mail_by_id(mail_id)
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

    @view_config(route_name='create_mail', renderer='json', request_method="POST")
    def create_mail(self):
        mail_data = self.request.json_body
        schema = CreateMailSchema()
        is_valid, error = validate_data(mail_data, schema)

        if not is_valid:
            return {'error': 'Validation Error', 'message': error}

        mail = self.mail_service.create_mail(mail_data)
        return {
            'status': 'success',
            'data': mail.to_dict()
        }

    @view_config(route_name='update_mail', renderer='json', request_method="PUT")
    def update_mail(self):
        mail_id = int(self.request.matchdict['id'])
        mail_data = self.request.json_body
        schema = UpdateMailSchema()
        is_valid, error = validate_update(mail_data, schema)

        if not is_valid:
            return {'error': 'Validation Error', 'message': error}

        mail = self.mail_service.update_mail(mail_id, mail_data)
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

    @view_config(route_name='delete_mail', renderer='json', request_method="DELETE")
    def delete_mail(self):
        mail_id = int(self.request.matchdict['id'])
        success = self.mail_service.delete_mail(mail_id)
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
