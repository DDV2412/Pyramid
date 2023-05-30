def includeme(config):
    config.add_route('get_all_contact', '/contacts', request_method='GET')
    config.scan()
