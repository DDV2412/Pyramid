from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('Hello, World!')


def main(global_config, **settings):
    config = Configurator(settings=settings)
    
    # Routing
    config.add_route('hello', '/')
    
    # Views
    config.add_view(hello_world, route_name='hello')
    
    app = config.make_wsgi_app()
    return app
