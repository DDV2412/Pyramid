from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('app.routes')
    config.include('app.models')
    config.scan()

    return config.make_wsgi_app()
