from pyramid.view import view_config

from app.models.contact import Contact


@view_config(route_name='get_all_contact', renderer='json', request_method="GET")
def get_all_contact(request):
    contacts = request.dbsession.query(Contact).all()
    return {
        'data': [contact.email for contact in contacts]
    }



