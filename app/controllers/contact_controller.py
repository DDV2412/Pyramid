from pyramid.view import view_config


@view_config(route_name='get_contact_by_id', renderer='json')
def get_contact_by_id(request):
    return {
        'status': 'error',
        'message': 'Contact not found'
    }