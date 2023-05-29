def includeme(config):
    config.add_route('get_contact_by_id', '/contact')
    config.scan()
