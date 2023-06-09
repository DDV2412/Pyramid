from pyramid.response import Response
from pyramid.view import view_config
from app.services.mail_service import MailService
from app.schemas.mail_schema import CreateMailSchema, validate_data, validate_update
from app.utils.send_mail import send_email


class MailController:
    def __init__(self, request):
        self.request = request
        self.mail_service = MailService()

    @view_config(route_name='get_all_mails', renderer='json', request_method="GET")
    def get_all_mails(self):
        mails = self.mail_service.get_all_mails()
        return Response(json_body={
            'status': 'success',
            'data': [mail.to_dict() for mail in mails]
        }, status_code=200)

    @view_config(route_name='get_mail_by_id', renderer='json', request_method="GET")
    def get_mail_by_id(self):
        mail_id = int(self.request.matchdict['id'])
        mail = self.mail_service.get_mail_by_id(mail_id)
        if mail:
            return Response(json_body={
                'status': 'success',
                'data': mail.to_dict()
            }, status_code=200)
        else:
            return Response(json_body={
                'status': 'error',
                'message': 'Mail campaign not found'
            }, status_code=404)

    @view_config(route_name='create_mail', renderer='json', request_method="POST")
    def create_mail(self):
        mail_data = self.request.json_body
        schema = CreateMailSchema()
        is_valid, error = validate_data(mail_data, schema)

        if not is_valid:
            return Response(json_body={'error': 'Validation Error', 'message': error}, status_code=400)

        mail = self.mail_service.create_mail(mail_data)
        return Response(json_body={
            'status': 'success',
            'data': mail.to_dict()
        }, status_code=200)

    @view_config(route_name='update_mail', renderer='json', request_method="PUT")
    def update_mail(self):
        mail_id = int(self.request.matchdict['id'])
        mail_data = self.request.json_body
        is_valid, error = validate_update(mail_data)

        if not is_valid:
            return Response(json_body={'error': 'Validation Error', 'message': error}, status_code=400)

        mail = self.mail_service.update_mail(mail_id, mail_data)
        if mail:
            return Response(json_body={
                'status': 'success',
                'data': mail.to_dict()
            }, status_code=200)
        else:
            return Response(json_body={
                'status': 'error',
                'message': 'Mail campaign not found'
            }, status_code=404)

    @view_config(route_name='delete_mail', renderer='json', request_method="DELETE")
    def delete_mail(self):
        mail_id = int(self.request.matchdict['id'])
        success = self.mail_service.delete_mail(mail_id)
        if success:
            return Response(json_body={
                'status': 'success',
                'message': 'Mail campaign deleted successfully'
            }, status_code=200)
        else:
            return Response(json_body={
                'status': 'error',
                'message': 'List not found'
            }, status_code=404)

    @view_config(route_name='send_email', renderer='json', request_method="POST")
    def send_email(self):
        mail_data = self.request.json_body
        schema = CreateMailSchema()
        is_valid, error = validate_data(mail_data, schema)

        if not is_valid:
            return Response(json_body={'error': 'Validation Error', 'message': error}, status_code=400)

        mail = self.mail_service.create_mail(mail_data)

        option_data = {
            "mail_id": mail.id,
            "from_name": mail.from_name,
            "from_mail": mail.from_mail,
            "subject": mail.subject,
            "preview_line": mail.preview_line,
            'design': mail.design,
            "recipients": mail.recipients
        }

        send_email(option_data)

        return Response(json_body={
            'status': 'success',
            'message': 'Mail campaign sending successfully'
        }, status_code=200)
