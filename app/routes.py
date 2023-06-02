def includeme(config):
    config.add_route('get_all_contact', '/contacts', request_method='GET')
    config.add_route('get_contact_by_id', '/contacts/{id}', request_method='GET')
    config.add_route('create_contact', '/contacts', request_method='POST')
    config.add_route('update_contact', '/contacts/{id}', request_method='PUT')
    config.add_route('delete_contact', '/contacts/{id}', request_method='DELETE')
    config.add_route('import_contacts', '/contacts/import', request_method='POST')

    config.add_route('get_all_list', '/lists', request_method='GET')
    config.add_route('get_list_by_id', '/lists/{id}', request_method='GET')
    config.add_route('create_list', '/lists', request_method='POST')
    config.add_route('update_list', '/lists/{id}', request_method='PUT')
    config.add_route('delete_list', '/lists/{id}', request_method='DELETE')

    config.add_route('get_all_mails', '/mails', request_method='GET')
    config.add_route('get_mail_by_id', '/mails/{id}', request_method='GET')
    config.add_route('create_mail', '/mails', request_method='POST')
    config.add_route('update_mail', '/mails/{id}', request_method='PUT')
    config.add_route('delete_mail', '/mails/{id}', request_method='DELETE')

    config.add_route('get_all_templates', '/templates', request_method='GET')
    config.add_route('get_template_by_id', '/templates/{id}', request_method='GET')
    config.add_route('create_template', '/templates', request_method='POST')
    config.add_route('update_template', '/templates/{id}', request_method='PUT')
    config.add_route('delete_template', '/templates/{id}', request_method='DELETE')

    config.add_route('create_bounce', '/bounce', request_method='POST')
    config.add_route('create_click', '/click', request_method='POST')
    config.add_route('create_open', '/open', request_method='POST')

    config.scan('app.controllers')
