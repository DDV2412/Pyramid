from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from app.models import DBSession, Base


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
