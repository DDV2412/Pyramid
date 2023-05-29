def includeme(config):
    config.add_route('get_all_contact', '/contacts', request_method='GET')
    config.add_route('get_contact_by_id', '/contacts/{id}', request_method='GET')
    config.add_route('create_contact', '/contacts', request_method='POST')
    config.add_route('update_contact', '/contacts/{id}', request_method='PUT')
    config.add_route('delete_contact', '/contacts/{id}', request_method='DELETE')
    config.add_route('import_contacts', '/contacts/import', request_method='POST')
    config.scan('.controllers')
